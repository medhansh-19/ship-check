"""Start the existing Switch-backed runner with its private Vercel relay key."""
import os
from pathlib import Path

config = Path.home() / ".ship-check/vercel-relay.env"
if not config.is_file():
    raise SystemExit("Vercel relay settings are missing; use control.switch_local for local-only mode.")
for line in config.read_text().splitlines():
    if "=" in line:
        key, value = line.split("=", 1)
        if key == "SHIP_CHECK_RELAY_SECRET":
            os.environ[key] = value
from control.switch_local import main
main()
