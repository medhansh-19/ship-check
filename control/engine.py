"""Persistent evidence and approvals. Standard library only; no repository code executes."""
import hashlib
import json
import re
import sqlite3
import subprocess
import threading
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path


def now():
    return datetime.now(timezone.utc).isoformat()


class Engine:
    def __init__(self, repo, database, demo_url=""):
        self.repo = Path(repo).resolve()
        self.database = str(database)
        Path(database).parent.mkdir(parents=True, exist_ok=True)
        self.demo_url = demo_url
        self.lock = threading.RLock()
        with self.db() as db:
            db.executescript("CREATE TABLE IF NOT EXISTS runs(id INTEGER PRIMARY KEY, created TEXT, fingerprint TEXT, data TEXT); CREATE TABLE IF NOT EXISTS events(id INTEGER PRIMARY KEY, created TEXT, kind TEXT, detail TEXT); CREATE TABLE IF NOT EXISTS decisions(run INTEGER, fix TEXT, decision TEXT, actor TEXT, created TEXT, PRIMARY KEY(run,fix)); CREATE TABLE IF NOT EXISTS pull_requests(run INTEGER PRIMARY KEY, url TEXT);")

    @contextmanager
    def db(self):
        connection = sqlite3.connect(self.database, timeout=20)
        try:
            with connection:
                yield connection
        finally:
            connection.close()

    def git(self, *args):
        return subprocess.check_output(["git", "-C", str(self.repo), *args], text=True, stderr=subprocess.STDOUT, timeout=30).strip()

    def fingerprint(self):
        files = self.git("ls-files", "--cached", "--others", "--exclude-standard").splitlines()
        digest = hashlib.sha256(self.git("rev-parse", "HEAD").encode())
        for name in sorted(files):
            path = self.repo / name
            if path.is_file() and not path.is_symlink():
                digest.update(name.encode())
                digest.update(path.read_bytes())
        return digest.hexdigest()

    def event(self, kind, detail):
        with self.db() as db:
            db.execute("INSERT INTO events(created,kind,detail) VALUES(?,?,?)", (now(), kind, detail))

    def audit(self, reason="Manual audit"):
        with self.lock:
            fingerprint = self.fingerprint()
            readme = self.repo / "README.md"
            text = readme.read_text(errors="replace") if readme.exists() else ""
            license_path = self.repo / "LICENSE"
            submission = self.repo / "SUBMISSION.md"
            checks = []
            def check(key, title, passed, evidence, proposal=None):
                checks.append(dict(id=key, title=title, status="passed" if passed else "blocked", evidence=evidence, proposal=proposal if not passed else None))
            check("readme", "Project introduction", len(text.strip()) > 80, "README.md contains %s characters." % len(text.strip()))
            check("setup", "Setup instructions", bool(re.search(r"(?im)^#{1,3} .*setup|^#{1,3} .*getting started|^#{1,3} .*installation", text)), "README setup heading inspected.")
            missing = [p for p in re.findall(r"pip install -r ([\w./-]+)", text) if not (self.repo / p).is_file()]
            proposal = None
            if missing:
                old = text
                new = text
                for name in missing:
                    new = new.replace("python3 -m pip install -r " + name, "# No external dependencies are declared; verify imports before running.")
                proposal = dict(id="setup-reference", path="README.md", before=old, after=new, summary="Replace a setup command referencing a missing requirements file. Review imports before accepting.")
            check("references", "Setup file references", not missing, "Missing referenced files: " + ", ".join(missing) if missing else "All pip requirements files referenced by README exist; commands have not been executed.", proposal)
            check("license", "Project license", license_path.is_file() and license_path.stat().st_size > 100, "LICENSE exists and has content." if license_path.exists() else "No root LICENSE file found.")
            brief = submission.read_text(errors="replace") if submission.is_file() else ""
            draft = any(marker in brief for marker in ("Describe what the project does", "Explain the working implementation", "TODO", "YOUR_PROJECT"))
            check("submission", "Submission brief", len(brief.strip()) > 80 and not draft, "Submission brief still contains draft placeholders." if draft else ("SUBMISSION.md inspected." if submission.exists() else "No SUBMISSION.md found."), None if submission.exists() else dict(id="submission-brief", path="SUBMISSION.md", before="", after="# Submission\n\n## Project\n\nDescribe what the project does and who it helps.\n\n## Implementation\n\nExplain the working implementation and include evidence links.\n\n## Demo\n\nAdd a playable demo video URL before submitting.\n", summary="Create a submission outline. This remains a draft requiring your project details."))
            combined = text + "\n" + (submission.read_text(errors="replace") if submission.exists() else "")
            urls = re.findall(r"https://(?:www\.)?(?:youtu\.be/|youtube\.com/watch\?|loom\.com/share/|vimeo\.com/)[^\s)<>]+", combined)
            if self.demo_url:
                urls.append(self.demo_url)
            check("video", "Demo video URL", bool(urls), "Video URL found: " + urls[0] + ". Playback requires human verification." if urls else "No supported video URL in README or SUBMISSION.md. Add YouTube, Loom or Vimeo.")
            passed = sum(c["status"] == "passed" for c in checks)
            data = dict(repo=self.repo.name, branch=self.git("branch", "--show-current"), commit=self.git("rev-parse", "--short", "HEAD"), checks=checks, passed=passed, total=len(checks), score=round(passed / len(checks) * 100), reason=reason, scope="Static repository checks. Setup execution, event rules, eligibility and video playback require separate evidence.")
            with self.db() as db:
                cursor = db.execute("INSERT INTO runs(created,fingerprint,data) VALUES(?,?,?)", (now(), fingerprint, json.dumps(data)))
                run_id = cursor.lastrowid
            self.event("audit", f"{reason}: {passed}/{len(checks)} checks passed (run {run_id}).")
            return self.state()

    def state(self):
        with self.db() as db:
            row = db.execute("SELECT id,created,fingerprint,data FROM runs ORDER BY id DESC LIMIT 1").fetchone()
            events = [dict(created=r[0], kind=r[1], detail=r[2]) for r in db.execute("SELECT created,kind,detail FROM events ORDER BY id DESC LIMIT 30")]
            if not row:
                return dict(run=None, events=events)
            run = json.loads(row[3])
            run.update(id=row[0], created=row[1], fingerprint=row[2])
            decisions = {r[0]: dict(decision=r[1], actor=r[2], created=r[3]) for r in db.execute("SELECT fix,decision,actor,created FROM decisions WHERE run=?", (row[0],))}
            for check in run["checks"]:
                if check["proposal"]:
                    check["proposal"]["decision"] = decisions.get(check["proposal"]["id"])
            return dict(run=run, events=events)

    def decide(self, run_id, fix_id, decision, actor):
        if decision not in ("approved", "rejected"):
            raise ValueError("Decision must be approved or rejected.")
        with self.lock:
            run = self.state()["run"]
            if not run or run["id"] != int(run_id) or run["fingerprint"] != self.fingerprint():
                raise ValueError("Repository changed. Run a new audit before approving.")
            fixes = [c["proposal"] for c in run["checks"] if c["proposal"]]
            if fix_id not in [f["id"] for f in fixes]:
                raise ValueError("Unknown fix for this audit.")
            with self.db() as db:
                db.execute("INSERT OR REPLACE INTO decisions VALUES(?,?,?,?,?)", (run_id, fix_id, decision, actor, now()))
            self.event("approval", f"{actor} {decision} {fix_id} on run {run_id}.")
            return self.state()

    def create_pr(self, run_id):
        """Apply approved exact bytes in an isolated worktree; leave user's checkout intact."""
        import tempfile
        with self.lock:
            run = self.state()["run"]
            if not run or run["id"] != int(run_id) or run["fingerprint"] != self.fingerprint():
                raise ValueError("Audit is stale. Run it again.")
            with self.db() as db:
                existing = db.execute("SELECT url FROM pull_requests WHERE run=?", (run_id,)).fetchone()
            if existing:
                return dict(url=existing[0])
            if self.git("status", "--porcelain"):
                raise ValueError("Commit or stash repository changes before creating a PR.")
            if not run["branch"]:
                raise ValueError("Check out a named branch before creating a PR.")
            fixes = [c["proposal"] for c in run["checks"] if c["proposal"] and (c["proposal"].get("decision") or {}).get("decision") == "approved"]
            if not fixes:
                raise ValueError("Approve at least one fix first.")
            branch = f"codex/ship-check-{run_id}-{int(datetime.now().timestamp())}"
            target = Path(tempfile.mkdtemp(prefix="ship-check-pr-")) / "checkout"
            self.git("worktree", "add", "-b", branch, str(target), "HEAD")
            def command(*args):
                return subprocess.check_output(args, cwd=target, text=True, stderr=subprocess.STDOUT, timeout=90).strip()
            try:
                for fix in fixes:
                    path = target / fix["path"]
                    if path.is_symlink() or (path.exists() and path.read_text() != fix["before"]):
                        raise ValueError("Proposed file no longer matches reviewed contents.")
                    path.write_text(fix["after"])
                command("git", "add", "--", *[f["path"] for f in fixes])
                command("git", "commit", "-m", "Apply approved Ship Check fixes")
                command("git", "push", "-u", "origin", branch)
                url = command("gh", "pr", "create", "--base", run["branch"], "--head", branch, "--title", "Apply approved launch-readiness fixes", "--body", "Applies only the exact changes approved in Ship Check audit " + str(run_id) + ".\n\nFixes: " + ", ".join(f["id"] for f in fixes) + ".\n\nStatic checks only; review before merging.")
                self.event("pull_request", url)
                with self.db() as db:
                    db.execute("INSERT INTO pull_requests(run,url) VALUES(?,?)", (run_id, url))
                return dict(url=url)
            finally:
                self.git("worktree", "remove", "--force", str(target))
