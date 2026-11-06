"""Local launch control server. Run: python3 -m control.server --repo ."""
import argparse
import hmac
import json
import os
import secrets
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse
from control.engine import Engine
from control import rules


def serve(engine, port=8787, interval=15, notifier=None):
    token = secrets.token_urlsafe(32)
    static = Path(__file__).parent / "static"

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass

        def send(self, code, body, content_type="application/json"):
            data = (json.dumps(body) if content_type == "application/json" else body).encode()
            self.send_response(code)
            self.send_header("Content-Type", content_type + "; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.send_header("Content-Security-Policy", "default-src 'self'; style-src 'self'; script-src 'self'; connect-src 'self'; frame-ancestors 'none'")
            self.end_headers()
            self.wfile.write(data)

        def do_GET(self):
            if self.headers.get("Host") not in (f"localhost:{port}", f"127.0.0.1:{port}"):
                return self.send(403, {"error": "Local access only."})
            path = urlparse(self.path).path
            if path == "/api/state":
                event_file = engine.repo / "control/event.json"
                event = json.loads(event_file.read_text()) if event_file.is_file() else None
                selected = engine.selected_checklist()
                if event and event.get("checklist") != selected:
                    event = None
                return self.send(200, dict(**engine.state(), csrf=token, watch_seconds=interval, discord=bool(notifier), event=event, checklists=rules.available(engine.repo), selected_checklist=selected))
            files = {"/": ("index.html", "text/html"), "/app.js": ("app.js", "text/javascript"), "/style.css": ("style.css", "text/css")}
            if path not in files:
                return self.send(404, {"error": "Not found"})
            name, mime = files[path]
            self.send(200, (static / name).read_text(), mime)

        def do_POST(self):
            if not hmac.compare_digest(self.headers.get("X-Ship-Check", ""), token):
                return self.send(403, {"error": "Reload the dashboard before changing state."})
            try:
                length = int(self.headers.get("Content-Length", "0"))
                if not 0 < length < 16384:
                    raise ValueError("Invalid request size")
                data = json.loads(self.rfile.read(length))
                path = urlparse(self.path).path
                if path == "/api/audit":
                    result = engine.audit()
                    if notifier:
                        notifier(result)
                elif path == "/api/decision":
                    result = engine.decide(data["run"], data["fix"], data["decision"], "Local owner")
                elif path == "/api/pr":
                    result = engine.create_pr(data["run"])
                elif path == "/api/checklist":
                    result = engine.select_checklist(data["path"])
                    if notifier:
                        notifier(result)
                elif path == "/api/rule-review":
                    result = engine.review_rule(data["run"], data["rule"], data["status"], data["evidence"], "Local owner")
                    if notifier:
                        notifier(result)
                else:
                    return self.send(404, {"error": "Not found"})
                self.send(200, result)
            except (ValueError, KeyError, json.JSONDecodeError) as error:
                self.send(409, {"error": str(error)})
            except Exception:
                self.send(500, {"error": "Operation failed. Check local service logs and GitHub authentication, then retry."})

    def watch():
        while True:
            time.sleep(interval)
            try:
                current = engine.state()["run"]
                if not current or current["fingerprint"] != engine.fingerprint():
                    state = engine.audit("Repository changed")
                    if notifier:
                        notifier(state)
            except Exception as error:
                engine.event("error", "Automatic recheck failed: " + str(error)[:180])

    if not engine.state()["run"]:
        engine.audit("Initial audit")
    threading.Thread(target=watch, daemon=True).start()
    print(f"Ship Check running at http://127.0.0.1:{port}", flush=True)
    ThreadingHTTPServer(("127.0.0.1", port), Handler).serve_forever()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    parser.add_argument("--port", type=int, default=8787)
    parser.add_argument("--interval", type=int, default=15)
    parser.add_argument("--database")
    args = parser.parse_args()
    if args.interval < 2:
        parser.error("interval must be at least 2 seconds")
    import hashlib
    database = args.database or str(Path.home() / ".ship-check" / (hashlib.sha256(str(Path(args.repo).resolve()).encode()).hexdigest()[:16] + ".sqlite3"))
    engine = Engine(args.repo, database)
    notifier = None
    if os.environ.get("DISCORD_BOT_TOKEN"):
        from control.discord_bot import start
        notifier = start(engine)
    serve(engine, args.port, args.interval, notifier)


if __name__ == "__main__":
    main()
