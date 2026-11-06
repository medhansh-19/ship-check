"""Use this Mac's existing Switch Discord connection without copying its token.

Optional local convenience launcher; normal deployments use environment variables.
"""
import asyncio
import json
import os
import sys
from pathlib import Path


def main():
    root = Path.home() / "Library/Application Support/switchdash/local-switch-server/native"
    bundles = sorted((root / "toolchain").glob("bundle-*"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not bundles:
        raise SystemExit("Switch's bundled runtime was not found. Use control.server with Discord environment variables instead.")
    bundle = bundles[0]
    runtime = bundle / "python/bin/python3"
    if Path(sys.executable).resolve() != runtime.resolve():
        os.execv(str(runtime), [str(runtime), "-m", "control.switch_local", *sys.argv[1:]])
    sys.path[:0] = [str(bundle / "switch/site-packages"), str(bundle / "switch/src/core")]
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--bridge", required=True)
    parser.add_argument("--channel", required=True)
    parser.add_argument("--owner", required=True)
    parser.add_argument("--repo", default=".")
    parser.add_argument("--port", default="8787")
    args = parser.parse_args()
    settings = {}
    for line in (root / "run/switch-core.env").read_text().splitlines():
        if "=" in line and not line.startswith("#"):
            key, value = line.split("=", 1)
            settings[key] = value
    import asyncpg
    from switch_core.keys import Keyring

    async def read_connection():
        connection = await asyncpg.connect(host=settings["DB_HOST"], port=int(settings["DB_PORT"]), user=settings["DB_OWNER_USER"], password=settings["DB_OWNER_PASSWORD"], database=settings["DB_NAME"])
        try:
            row = await connection.fetchrow("SELECT type, connection_config FROM collaboration_bridges WHERE id=$1", args.bridge)
            if not row or row["type"] != "discord":
                raise ValueError("Select an existing Discord bridge.")
            raw = row["connection_config"]
            value = json.loads(raw) if isinstance(raw, str) else raw
            if "_enc" in value:
                value = json.loads(Keyring.parse(settings["SECRET_KEYS"], legacy_secret=settings.get("JWT_SECRET_KEY")).decrypt(value["_enc"]))
            return value["bot_token"]
        finally:
            await connection.close()

    os.environ["DISCORD_BOT_TOKEN"] = asyncio.run(read_connection())
    os.environ["DISCORD_CHANNEL_ID"] = args.channel
    os.environ["DISCORD_OWNER_ID"] = args.owner
    sys.argv = ["control.server", "--repo", args.repo, "--port", args.port]
    from control.server import main as server_main
    server_main()


if __name__ == "__main__":
    main()
