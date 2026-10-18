#!/usr/bin/env python3
"""Validate estimates.json against schema and omnipha/ports device ids."""
import json
import os
import sys
import urllib.request
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parent.parent
# API instead of raw.githubusercontent.com: the raw CDN caches for minutes.
PORTS_IDS_URL = "https://api.github.com/repos/omnipha/ports/contents/devices.json?ref=main"


def fetch_ports_index():
    headers = {"Accept": "application/vnd.github.raw", "User-Agent": "omnipha-market-check"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(PORTS_IDS_URL, headers=headers)
    return json.loads(urllib.request.urlopen(req, timeout=30).read())


def main():
    data = json.loads((ROOT / "estimates.json").read_text())
    schema = json.loads((ROOT / "schema" / "estimates.schema.json").read_text())
    errors = 0
    for err in jsonschema.Draft202012Validator(schema).iter_errors(data):
        print(f"schema: {'/'.join(map(str, err.path))}: {err.message}", file=sys.stderr)
        errors += 1
    try:
        ports = fetch_ports_index()
        known = {d["id"] for d in ports}
    except Exception as exc:
        print(f"warning: could not fetch ports index ({exc}); skipping device-id check", file=sys.stderr)
        known = None
    if known is not None:
        for entry in data["devices"]:
            if entry["device"] not in known:
                print(f"unknown device id: {entry['device']}", file=sys.stderr)
                errors += 1
    print("check:", "ok" if not errors else f"{errors} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
