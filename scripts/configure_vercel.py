"""Configure this linked Vercel project's relay. Never prints credential values."""
import argparse
import json
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

parser = argparse.ArgumentParser()
parser.add_argument("backend", help="HTTPS URL of the running secure tunnel")
args = parser.parse_args()
if urlparse(args.backend).scheme != "https" or not urlparse(args.backend).hostname:
    parser.error("An HTTPS backend URL is required.")
root = Path(__file__).resolve().parents[1]
project = json.loads((root / ".vercel/project.json").read_text())
auth = json.loads((Path.home() / "Library/Application Support/com.vercel.cli/auth.json").read_text())
private = Path.home() / ".ship-check"
relay = (private / "vercel-relay.env").read_text().strip().split("=", 1)[1]
owner = (private / "vercel-owner-key.txt").read_text().strip()
values = {"SHIP_CHECK_BACKEND_URL": args.backend, "SHIP_CHECK_RELAY_SECRET": relay, "SHIP_CHECK_OWNER_KEY": owner}
data = [{"key": key, "value": value, "type": "encrypted", "target": ["production", "preview"]} for key, value in values.items()]
url = f"https://api.vercel.com/v10/projects/{project['projectId']}/env?teamId={project['orgId']}&upsert=true"
request = urllib.request.Request(url, data=json.dumps(data).encode(), headers={"Authorization": "Bearer " + auth["token"], "Content-Type": "application/json", "User-Agent": "ShipCheckDeployment/2.0"})
with urllib.request.urlopen(request, timeout=30):
    print("Configured three encrypted Vercel variables. Redeploy to apply them.")
