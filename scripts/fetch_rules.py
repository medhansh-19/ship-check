#!/usr/bin/env python3
"""Save public rules as readable text plus a provenance sidecar. Stdlib only."""

import argparse
from datetime import datetime, timezone
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import urlsplit
from urllib.request import Request, urlopen


class RulesParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.hidden = 0

    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style", "noscript"}:
            self.hidden += 1
        if not self.hidden and tag in {"p", "div", "br", "li", "h1", "h2", "h3", "tr", "section", "pre"}:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in {"script", "style", "noscript"}:
            self.hidden = max(0, self.hidden - 1)
        elif not self.hidden and tag in {"p", "div", "li", "h1", "h2", "h3", "tr", "section", "pre"}:
            self.parts.append("\n")

    def handle_data(self, data):
        if not self.hidden:
            self.parts.append(data)


def html_to_text(html):
    parser = RulesParser()
    parser.feed(html)
    return "\n".join(line for raw in "".join(parser.parts).splitlines()
                     if (line := " ".join(raw.split()))) + "\n"


def fetch_rules(url, output_dir, slug):
    if urlsplit(url).scheme not in {"http", "https"}:
        raise ValueError("Rules URL must use http or https")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
        raise ValueError("Slug must contain lowercase words/digits separated by hyphens")
    request = Request(url, headers={"User-Agent": "ShipCheck/0.1 (rules snapshot)"})
    with urlopen(request, timeout=30) as response:
        raw = response.read(5_000_001)
        if len(raw) > 5_000_000:
            raise ValueError("Rules response exceeds 5 MB; save a smaller source manually")
        media_type = response.headers.get_content_type()
        if media_type not in {"text/html", "application/xhtml+xml", "text/plain", "text/markdown"}:
            raise ValueError(f"Unsupported content type: {media_type}; save rules as text manually")
        content = raw.decode(response.headers.get_content_charset() or "utf-8")
        final_url = response.geturl()
    text = html_to_text(content) if media_type in {"text/html", "application/xhtml+xml"} else content
    if not text.strip():
        raise ValueError("No text found; paste the rules into scout/inputs/ instead")
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / f"{slug}.txt"
    sidecar = output_dir / f"{slug}.source.json"
    if target.exists() or sidecar.exists():
        raise FileExistsError(f"Snapshot already exists for {slug}; choose a new slug")
    target.write_text(text, encoding="utf-8")
    sidecar.write_text(json.dumps({
        "requested_url": url, "final_url": final_url,
        "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
        "content_type": media_type,
        "note": "HTML whitespace is normalized; verify quotes against the original page.",
    }, indent=2) + "\n", encoding="utf-8")
    return target


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url")
    parser.add_argument("--slug", required=True)
    parser.add_argument("--output-dir", type=Path,
                        default=Path(__file__).resolve().parents[1] / "scout" / "inputs")
    args = parser.parse_args()
    try:
        print(fetch_rules(args.url, args.output_dir, args.slug))
    except (OSError, ValueError, UnicodeError) as error:
        parser.exit(1, f"fetch_rules: {error}\n")


if __name__ == "__main__":
    main()
