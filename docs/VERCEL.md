# Vercel dashboard

Production: https://ship-check-ivory.vercel.app

Vercel serves the dashboard and an API gateway. The existing Python runner stays
on the owner's Mac, where it can inspect files, watch Git changes, retain SQLite
history and coordinate Discord. The gateway reaches it through an authenticated
HTTPS tunnel. This is a hosted frontend with a local backend, not an always-on
cloud audit runner: **live data and actions require the Mac, runner and tunnel
to remain online**. Switch also needs to be running for its agents.

The production dashboard currently points at the deliberately faulty Launch Ledger
checkout on `codex/demo-switch-faulty`, using only Flip the Switch event rules.

## Owner controls

Visitors can read evidence. All audit, approval, event-selection, verification and
PR mutations require the owner key. Click **Unlock owner controls** and enter the
key in `~/.ship-check/vercel-owner-key.txt` on this Mac. It is saved with owner-only
filesystem permissions, never bundled into the site or committed. The browser
retains it only in that tab's session storage. Click **Lock owner controls** to
remove it. Keep the owner key private; public viewers need no key.

Vercel holds the gateway's relay secret as an encrypted environment variable.
Direct public access to the local runner is denied, including its local CSRF API.
The gateway only forwards known API routes. It never exposes the local CSRF secret.
The deployment includes static UI and gateway code only, not local credentials,
repository checkouts, SQLite files or the Discord bot token.

## Restart after this recording session

From the main Ship Check checkout, run:

```sh
python3 -m control.cloud_local --bridge f2fcebe1-afc2-40a0-8ade-070436f2a519 --channel 1568294022110388326 --owner 1417535988829392978 --repo '/Users/medhanshadhlakha/Documents/ChatGPT/Ship Check Demo'
```

In another terminal:

```sh
cloudflared tunnel --url http://127.0.0.1:8787 --no-autoupdate
```

A restarted Quick Tunnel gets a new HTTPS hostname. Update the encrypted backend
URL and redeploy; do not change any GitHub App callback for this dashboard tunnel:

```sh
python3 scripts/configure_vercel.py https://YOUR-NEW-TUNNEL.trycloudflare.com
npx vercel deploy --prod --yes --scope medhanshs-projects-1ac9d87f
```

The project was deployed through the authenticated Vercel CLI. Automatic GitHub
deployment is not connected; the private repository connection was unavailable.
CLI deployment works independently. A stable backend would remove the Mac/tunnel
dependency and is a separate hosting step.

## Verified

- Production homepage returned HTTP 200.
- Hosted state returned the correct demo project and 2/16 scored checks.
- Unauthenticated writes were rejected; authenticated owner audit succeeded.
- Direct unauthenticated tunnel access returned HTTP 403.
- Four cloud gateway tests and the 23 existing Python tests passed.
