# Published evidence and reproduction boundaries

## Original reports, unchanged

| File | Original file SHA-256 |
|---|---|
| [Stage 2D confirmation report](stage2d_confirmation_report.json) | `8a52292d5fc9139f977fa7cdd4174840cc046b0c95401df7cc3bc91002120e72` |
| [Stage 2E oracle summary](stage2e_oracle_summary.json) | `2f4341fdefd5e39aa658ce1c72ec298f2e35dc97b8a202cb5f35965a4628c9ca` |

The Stage 2E basename changed from `summary.json`; its bytes did not change.
Each report's `payload_sha256` seals its other fields using sorted compact JSON.
The verifier checks both original file hashes and payload seals.

## Aggregate exports

- [Stage 2D strongest-setting CSV](stage2d_strongest_strategy_summary.csv) contains
  all 1,440 strategy rows from the forty strongest cases, including counts,
  existing gate summaries, existing HAC interval bounds, baseline comparisons
  and case-file hash references. Baseline improvement is the arithmetic
  difference of two retained means. It introduces no new inference.
- [Strongest-case source hashes](stage2d_strongest_source_hashes.json) bind those
  forty original case files and their payload seals.
- [Stage 2E setting CSV](stage2e_setting_summary.csv) exports all ten pooled
  shape/effect rows from the original report. The original JSON also includes
  every one of the 200 seed-level aggregate summaries.

Before export, every strongest-setting file matched the full campaign report's
hash and its own payload seal. The retained forty-case archive hash is
`67cf5d972cdb5c6c7500efd224896d59148686d5880a8e33ab72ad9bfa8bd44f`.
The archive itself is not bundled. Public readers can check the CSV's integrity
and aggregate relationships, but cannot independently repeat its extraction
without those original case files.

## Frozen identity

- Scientific implementation: `20eeba9df80e81cbbf99e03debb823848cf7faed`
- Configuration: `5af8b9cef4c0849af02406551c6bf5a97bbbf35bf65c16701a9df768628d968f`
- Dataset identity: `f4a5e88feebc5a3cbbd014335df9675e8f0ca86d6402b074814d0e3ed0263200`
- Eligible index: `a03d5eaa94877f9992631c1f736a933f56dbbdea2d4ac60feaa5a3ff0468bf69`
- Stage 2D execution contract: `7cbcc840cfcf25c1c7ded85efc5c94fda9c57a1c9eee8772e1acc3503dfc2d1b`
- Stage 2E execution contract: `332a4a8be50433e4d65fe88027af7358217036e110d2a788fa1780108ad8e28d`

Hashes identify retained evidence. They do not make unpublished inputs available
or independently authenticate the private registry. The implementation commit is
an identifier from the frozen checkout, not a promise of a public source link.

## Retained privately

Original source data and synthetic bases, model/fold/selection audits, full case
files, registry records, approvals, preflights, original packages, incident
archives and execution logs remain unchanged. Raw scores, return streams and
daily statistical input vectors were not persisted by the registered output
schemas. Vendor bars, credentials and personal machine paths are not released.

The Stage 2D continuation log hash is
`63d48c7a8b36ee9ee19a029f75d126bb366718e2643564df69654b6ce8d30691`;
the final inspection reported all 261 jobs completed. Stage 2E's execution log
hash is `091e98808b8b80c962a6417b24ce1507683541288446d8496161acee18bfea74`.
The final Stage 2E inspection reported 21 completed jobs and zero pending.

## What public verification does

`python3 tools/verify_results.py` checks this release's checksums, original report
bindings, retained scope flags, reported setting/count completeness, aggregate
CSV relationships, weighted oracle means, gross/net/cost reconciliation and
normal-approximation capacity arithmetic. It does not access a database, run
scientific jobs, recreate fits or recalculate inference from unretained raw
streams. End-to-end scientific reproducibility is therefore outside this release.
