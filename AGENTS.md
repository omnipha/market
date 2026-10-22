# AGENTS.md — omnipha/market

Purpose: public used-price estimates per device, joined with omnipha/ports.

## Layout
- `estimates.json` — the data. Keyed by ports device id, optional variant.
- `schema/estimates.schema.json` — validates estimates.json.

## Conventions
- Values are estimates in EUR with `observed` date. Anyone may refresh them via PR.
- `estimate_eur` is the latest dated eBay range from maintainer observations. Listing notes, seller details and other markets stay out of this repo.
- `device` must exist in omnipha/ports `devices/<id>/`. CI fails otherwise.
- No listing URLs, no seller identifiers, no eBay user data.
- Never store USD or other converted currencies.

## Commands
```bash
python3 tools/check.py   # schema + device-id reference validation
```
