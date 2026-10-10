# SPY intraday ML research — final closeout

**Closeout date:** October 9, 2026, America/Chicago.  
**Disposition:** close the current intraday SPY research line at the project
owner's request. Retain completed results, original artifacts and all failures.
This is a project-management closure; it does not rewrite scientific registry
records, change any completed study's result or authorize another experiment.

## Outcome

The original goal of a validated, usable SPY trading strategy was not achieved.
Research stopped during synthetic pipeline validation, before real model
evaluation. The completed evidence supports an economic non-pass for the tested
five-minute synthetic procedure. It does not establish a real-data SPY null or
prove that every intraday strategy is impossible.

Stage 2D completed its entire registered campaign. All twenty null cases passed
the registered null screen, and trade counts were sufficient. No positive-control
setting produced a qualifying primary detection. Stage 2E then directly used the
known causal plant with the frozen selection rule and found insufficient gross
edge to pay modeled costs at every tested setting.

The proposed thirty-minute extension was closed on dataset/budget planning
grounds. Its selected-trade variance was never measured on private development
outcomes, so it must not be described as a failed real-data experiment.

## What was tested

The completed studies used development-partition synthetic data, chronological
training, a fixed training-derived higher 70th-percentile cutoff, score >= cutoff
with ties retained, next-open entry, fifth-close exit, long-only positions and one
position at a time. The cutoff was fixed for later evaluation rows within each
fold. It did not force exactly 30% of evaluation bars to become trades.

The quantile studies were separately registered developments from the original
absolute-probability-threshold proposal. They ask whether a training-derived
ranking rule selects economically useful later opportunities. No completed
quantile result silently amends or completes the original threshold-based
real-data hypothesis.

The final synthetic geometry used 585 initial training sessions and eight
expanding evaluation folds of 146 sessions, with the frozen five-minute
purge/embargo. Within a case there were 36 actual strategies: twelve models
times three time filters. Only the four all-times logistic strategies determined
primary detection. Statistical details appear in [METHODS.md](METHODS.md).

## Completed confirmation: Stage 2D

Study: `stage2d_development_quantile_confirmation_20261005_v2`.

Twenty previously unused seeds, 32000001–32000020, produced twenty synthetic
physical bases and 220 cases: twenty null cases, plus twenty seeds for each of
five positive amplitudes and two shapes. Null cases completed before positive
cases. All 261 scientific jobs completed, including the campaign reducer.
The recorded fitting totals were 21,120 outer prediction fits and 35,200
estimator fit calls.

| Registered amplitude (bp) | Linear primary detections | Conditional primary detections |
|---:|---:|---:|
| 1.00 | 0 / 20 | 0 / 20 |
| 0.50 | 0 / 20 | 0 / 20 |
| 0.25 | 0 / 20 | 0 / 20 |
| 0.10 | 0 / 20 | 0 / 20 |
| 0.05 | 0 / 20 | 0 / 20 |

The operational reference required at least sixteen detections out of twenty.
Neither shape established a sensitivity boundary. The registered result remains
`registered_confirmation_nonpass`.

All 396 scenario/model/filter count cells passed; every reported seed count met
the 16,600-trade requirement. Across these cells counts ranged from 20,214 to
37,831. The five-minute confirmation failed on acceptance criteria despite count
sufficiency.

None of the 36 strategies would pass the candidate gates in any null case.
Zero of twenty observations does not establish a population false-promotion rate
of at most 5%. The registered one-sided 95% upper bound is about 13.9%.
Nor would an observed sixteen-of-twenty detection rate establish population
power of at least 80%.

### Learning evidence and the economic failure

The retained forty strongest-setting cases contain 1,440 strategy summaries.
Every strategy's mean base-net return and every evaluation-fold mean were
negative. Primary means ranged from −1.654 to −1.531 bp for linear cases and
−1.696 to −1.453 bp for conditional cases, against a +0.25-bp hurdle.

All 1,440 strategies beat all 100 count-matched random draws in their respective
cases. All 720 linear results and 700 of 720 conditional results exceeded the
best deterministic baseline by at least 0.10 bp. That is evidence of useful
selection in these synthetic cases, while the chosen trades remained
uneconomic under base costs. It does not establish real-market predictability.

Small two-sided HAC p-values in the strongest cases reflected distinguishable
negative means, not profitable signals. All reported HAC upper bounds there
were below zero. No statistical gate was relaxed after seeing the result.

## Economic diagnostic: Stage 2E

Study: `stage2e_synthetic_oracle_feasibility_20261008_v1`.

Twenty existing-base analyses and one reducer reused the completed Stage 2D
bases. They produced 200 positive-setting seed summaries and 1,760 fold outcome
materializations, with zero new datasets, seeds or model fits. The oracle used
the causal mathematical plant driver; selection was fixed before reading
outcomes and reused across amplitudes and paired zero-effect accounting.

| Strongest 1.0-bp setting | Gross bp/trade | Modeled cost bp/trade | Net bp/trade | Seeds meeting diagnostic screen |
|---|---:|---:|---:|---:|
| Linear known-plant rule | +0.7017 | 2.2347 | −1.5330 | 0 / 20 |
| Conditional known-plant rule | +0.2526 | 2.2341 | −1.9815 | 0 / 20 |

These are trade-weighted pooled means. Every one of the ten shape/effect cells
had zero qualifying seeds. All 200 seed summaries cleared the trade-count floor,
but every reported mean net return was negative.

The exact accounting produced approximately 2.23 bp modeled round-trip drag,
correcting an earlier rough 1.6-bp estimate based on different price levels.
At that drag, clearing a +0.25-bp net hurdle needs about 2.48 bp gross per trade.
The strongest linear oracle supplied about 0.70 bp gross. A plant amplitude
defined per standardized driver deviation or active event is not the selected
trade's gross or net advantage.

This diagnostic explains the inadequacy of the tested known-driver/rule
combination. It is not a mathematical optimum over policies, fresh confirmation
evidence or a population-power estimate. No new HAC, DSR, Reality Check,
bootstrap or power inference was run in Stage 2E.

### Conditional-score limitation

With a binary conditional score, a higher 70th-percentile cutoff can be zero,
admitting inactive bars through the frozen >= rule. Artificial tests reproduced
this behavior; a prospective binary-oracle stop guard was tested but never
installed into the completed studies. Existing results retain their original
tie policy. The Stage 2E reducer alone does not identify every source fold's
cutoff, so the precise inactive-bar dilution is not claimed from this release.

## Thirty-minute proposal: planning stop

The proposed full opening-hour warm-up and thirty-minute nonoverlapping holds
allow at most eleven holdings per full session. Eight 146-session evaluation
folds give an optimistic ceiling of 12,848 trades, before gaps, early closes,
selection and exclusions.

At effect 0.25 bp, two-sided alpha 0.05 and nominal power 0.80, the proposal's
normal approximation requires about 125.582 times planning variance in bp²,
rounded upward to hundreds. At 12-bp standard deviation this requires 18,100
trades; at 20 bp, 50,300. The ceiling supports at most about 10.096-bp standard
deviation after rounding.

Public evidence and stated scenarios were sufficient for a budget stop. They
are not measurements or lower bounds for the exact model-selected distribution
on the project's real data. The proposed real descriptive pass, zero-fit
benchmark and 48-fit learning diagnostic were not executed. See the
[capacity review](reports/PUBLIC_CAPACITY_REVIEW.md).

## Original phases 0–6 at closure

| Original phase | Closure status |
|---|---|
| 0 — Contracts and pre-registration | Technical contracts, data validation and registry foundation completed and used for the approved synthetic work |
| 1 — Pipeline controls | Substantial implementation and synthetic campaigns completed; the required positive-control sensitivity gate did not pass |
| 2 — Data and feature validation | Foundation checks existed; the full independent feature/label closure report for progression was not completed |
| 3 — Real walk-forward research | Not started |
| 4 — Freeze and open holdout once | Not started; holdout remained sealed under the retained access restrictions |
| 5 — Follow-on horizons | Thirty-minute proposal stopped at planning; sixty-minute execution not started |
| 6 — Paper trading | Not started |

This project is closed as a stopped research effort, without marking all phases
complete. No real model was promoted and no real trading was authorized.

## Lessons and accountability

The most consequential sequencing mistake was proceeding with the large
positive-control fitting campaign before a cheap check of whether the plant and
selection rule could pay the registered costs. The cost warning was explicit in
external review while the campaign was still running. Stage 2E supplied the
missing direct calculation only after completion. Economic feasibility should
have been checked first.

Count/variance sufficiency is not signal usefulness or joint gate power. A
training-derived percentile changes the research question and needs explicit
registration. Costs must use exact price-dependent accounting and retain their
status as fill assumptions. Calendar trade capacity should be checked before
preparing a new horizon. Retained failures and separate repair approvals remain
part of the record; successful completion does not erase those incidents.

The reusable outputs are the contracts, chronological audit structure,
experiment registry, provenance checks, retained aggregate evidence and explicit
stopping procedure. A later project needs its own rationale and budget; this
closeout does not launch one.

## Verification and publication limits

The original Stage 2D/2E aggregate report bytes and their payload checksums are
included unchanged. The 1,440-row strongest-setting CSV was extracted from forty
original case files after checking every file against the campaign report and
every payload seal. The original forty-case archive is retained privately; its
hash and the individual case hashes accompany the export.

Published verification reproduces aggregate arithmetic and checks the release's
integrity. It does not reproduce model fitting, synthetic generation,
chronological trade scheduling, HAC estimates, DSR or bootstrap results from raw
inputs. The private live registry was not independently reopened for this
publication. Runner-reported lineage checks and reviewer-checked retained
evidence are distinguished in the [evidence index](evidence/README.md).

The scientific implementation remains identified by
`20eeba9df80e81cbbf99e03debb823848cf7faed`. Original artifacts, approvals,
preflights and failure records remain unchanged. Publication is documentation
and aggregate evidence release, with no new scientific work or data access.
