# Methods and scope of the completed synthetic studies

## Source and chronology

The originating vendor was TradeStation; the versioned research source was
PostgreSQL. The project used regular-session SPY bars with interval-start
timestamps and session-aware validation. Synthetic constructions were limited
to approved development-partition inputs. No result in this release comes from
real walk-forward or final-holdout model evaluation.

Stage 2D generated twenty new synthetic bases using seeds 32000001–32000020.
They were unused relative to the earlier synthetic development seeds
31000001–31000010. "Confirmation" here means confirmation of the registered
synthetic procedure; it does not mean independent real-market validation.
Stage 2E reused those same twenty bases after seeing Stage 2D's result.

## Models, folds and rule

Twelve frozen model configurations comprised four logistic configurations
(C = 0.01, 0.1, 1, 10) and eight XGBoost configurations (depth 2 or 3, learning
rate 0.03 or 0.05, minimum child weight 20 or 100). Three time filters gave
36 actual strategies within each case. The four all-times logistic strategies
alone determined primary detection; exploratory success could not rescue them.

The registered mapping used 585 initial training sessions followed by eight
expanding evaluation folds of 146 sessions. Preprocessing and threshold
estimation used training data. The higher 70th-percentile cutoff was applied
as a fixed number to later scores with >= and retained ties. Evaluation signal
counts were not forced to 30%. Five-minute purge/embargo and one-position
chronological scheduling were frozen.

The primary trading definition was long only, next-open entry, fifth-close exit
and $50,000 notional. Plant amplitudes were 1.0, 0.5, 0.25, 0.1 and 0.05 bp.
The linear amplitude was per training-standardized driver standard deviation;
the conditional amplitude was per active eligible event. Neither was a net
selected-trade return target.

## Exact base-cost accounting

For entry anchor O and exit anchor X, the frozen accounting was:

```text
entry_fill = O * 1.000055 + 0.010
exit_fill = X * 0.999945 - 0.010
shares = 50000 / entry_fill
fees = 2 * max(0.50, shares * 0.005)
gross_bps = 10000 * (X / O - 1)
net_bps = 10000 * (shares * (exit_fill - entry_fill) - fees) / 50000
modeled_drag_bps = gross_bps - net_bps
```

Proportional allowances total approximately 1.10 bp, while fixed cents and fees
depend on price levels and share sizing. These are modeled fill assumptions,
not calibration to historical quoted spreads or realized fills. Published costs
come from this accounting, not a blanket round-trip constant.

## Stage 2D gates

The count floor was 16,600 completed trades. The economic hurdle was mean
base-net return at least +0.25 bp; fold stability required positive means in
at least six of eight folds. Registered baseline comparisons, five-lag Bartlett
HAC with small-sample correction, fold concentration and statistical gates
were also required. Full gate outputs are retained in the source evidence.

The Reality Check used all 36 actual strategies, 5,000 replications and shared
20-day circular blocks. The prospectively amended DSR ledger counted 360
historical variants and used dispersion across the 36 current strategies.
These trial counts serve different roles; they are not interchangeable.

All twenty null cases were completed and screened before positive cases.
Any null strategy passing the candidate gates would have stopped positive
execution/reduction. For each positive shape/amplitude, the operational
reference required at least sixteen primary detections out of twenty.
Observed seed proportions are not certified population power/error rates.

## Stage 2E diagnostic

The linear known-plant score was the monotonic mapping (z + 3) / 6 of the
training-standardized driver clipped to [-3, 3]. The conditional score was binary
for the registered positive-momentum/low-volatility condition. The same frozen
quantile, comparison, scheduling and costs were used. Selection preceded reading
outcomes and was reused for every positive amplitude and paired zero accounting.

Only the existing aggregate economic/count diagnostic was evaluated. No new
model, inference, bootstrap, population-power calculation or full candidate gate
evaluation occurred. The oracle is a causal known-plant rule under one policy,
not a mathematical upper bound over all possible strategies.

## Assistance and review

Engineering, evidence review and drafting used Codex. LLM-Works supplied external
design feedback and reviews communicated by the project owner. External feedback
is distinct from reproducing the experiments; the conditional fixture review
explicitly did not rerun the tests. The verifier in this release checks published
aggregates, not the private scientific execution environment.
