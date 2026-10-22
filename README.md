# omnipha/market

Used-market price estimates for Omnipha-supported devices. Filled from the
device database in [omnipha/ports](https://github.com/omnipha/ports).

## Data

- `estimates.json` — one entry per device (optionally per ram/storage variant
  from ports `variants`), with observed price range in EUR and date.
- `schema/estimates.schema.json` — JSON Schema; CI validates against it.

## Rules

- Estimates only: ranges change constantly and any contributor may update
  them with fresher observations via PR.
- Base currency EUR. USD values are derived at display time using a dated
  exchange rate, never stored.
- `device` must match a folder id in omnipha/ports `devices/`.
- No seller names, no listing links, no user data.

## Update

Maintainers derive each range from their latest confirmed observations.
The published range spans those markets; it is not an average and does not
name a market. Listing notes, sellers and per-market prices stay unpublished.
CI checks schema and device-id references.

## License

MIT.
