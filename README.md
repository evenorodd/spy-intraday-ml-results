# SPY intraday ML research: closeout and results

**Status: closed research line, October 9, 2026.** The project stopped during
synthetic pipeline validation. It did not establish a profitable real-data
strategy, and it did not proceed to real walk-forward, final-holdout evaluation
or paper trading.

The registered five-minute synthetic confirmation completed but did not meet its
acceptance criteria. A later causal known-plant diagnostic showed why the tested
benchmark was economically inadequate: at its strongest linear setting, selected
trades averaged **0.702 bp gross against 2.235 bp modeled costs**, yielding
**−1.533 bp net**. The conditional diagnostic averaged **−1.981 bp net**.

The original control amplitude was not a promise of net profit per selected
trade. The project should have checked this economic feasibility before its
large confirmation fitting campaign.

## Read the findings

- [Final closeout](CLOSEOUT.md): outcomes, original phase status and lessons.
- [Methods and scope](METHODS.md): the tested rule, costs and statistical gates.
- [Thirty-minute capacity review](reports/PUBLIC_CAPACITY_REVIEW.md): why the
  proposed follow-on stopped at planning, with its uncertainty preserved.
- [Incident record](reports/INCIDENTS.md): retained failures and approved repairs.
- [Evidence index](evidence/README.md): original aggregate reports, derived
  summaries, checksums and reproduction limits.

## Principal results

| Item | Outcome |
|---|---|
| Stage 2D scientific jobs | 261 completed: 20 builds, 20 validations, 220 cases, 1 reducer |
| Stage 2D fitting | 21,120 outer prediction fits; 35,200 estimator fit calls |
| Null cases with any candidate passing | 0 / 20; not a population false-promotion guarantee |
| Positive-control primary detections | 0 / 20 in each of the 10 shape/effect settings |
| Five-minute capacity | All 396 Stage 2D count cells passed the 16,600-trade gate |
| Stage 2E diagnostic | 20 existing-base analyses + 1 reducer; zero new fits or datasets |
| Thirty-minute proposal | Closed at planning; no measured real-data result |

One basis point (bp) is 0.01%. All trading-performance numbers here are synthetic
results under assumption-based costs. They are not realized account returns.

## Verify the published evidence

From the repository root, using Python 3.10 or newer and no third-party packages:

```bash
python3 tools/verify_results.py
```

The verifier checks file checksums, the original reports' payload seals, complete
reported settings, counts, exported strategy summaries, trade-weighted oracle
accounting and public planning arithmetic. It reads local published files only.
It makes no network requests, fits no models and starts no scientific run.

This repository contains a results release and its verification code. Full
training, raw vendor data, individual trades, daily input vectors and the private
registry are outside this release. See the evidence index for the exact limits.

The frozen scientific implementation was identified by commit
`20eeba9df80e81cbbf99e03debb823848cf7faed`; publication commits are separate.
No new study or automatic continuation is proposed by this closeout.
