# Thirty-minute follow-on: public planning check and stop

October 9, 2026. This follow-on was never executed. Closure is a dataset/budget
decision based on published aggregates and stated planning scenarios, not a
measured failure of a model-selected real-data distribution.

## Capacity

The proposed inputs were twelve complete same-session five-minute bars, giving
a full 60-minute warm-up. A thirty-minute hold with one position at a time allows
at most floor((390 − 60) / 30) = 11 holdings in a full session. Eight evaluation
folds of 146 sessions give a ceiling of **12,848 trades** before all capacity
losses. This is an optimistic bound, not a predicted realized count.

## Planning arithmetic

For a true mean effect of 0.25 bp against zero, two-sided alpha 0.05 and nominal
power 0.80, the normal approximation gives:

```text
k = (1.959963984540054 + 0.8416212335729143)^2 / 0.25^2
  = 125.58207574958541
required_trades = 100 * ceil(k * sigma_bps^2 / 100)
```

No dependence inflation is added in this table. The draft's inflation floor of
one would prevent negative dependence from reducing the requirement.

| Assumed planning standard deviation (bp) | Required trades | Within ceiling? |
|---:|---:|:---:|
| 8 | 8,100 | Yes, before losses |
| 10 | 12,600 | Barely, before losses |
| 12 | 18,100 | No |
| 15 | 28,300 | No |
| 20 | 50,300 | No |
| 23 | 66,500 | No |

After rounding to hundreds, the ceiling supports sigma at most approximately
**10.0958 bp**. This power approximation describes a single mean-versus-zero
contrast, not passage of the joint economic/statistical gates or the probability
that the estimated mean exceeds +0.25 bp.

## Public context and its limitations

Gao, Han, Li and Zhou report annualized standard deviation 6.21% for a daily
final-half-hour SPY holding in their February 1993–December 2013 sample
(Table 6, Panel B). Their 252-session annualization implies about 39.12 bp per
observation and 192,200 trades under the planning formula. This is a different
period and a particular closing interval. It is not a lower bound for our
post-warm-up universe or model-selected returns.

Source: [Market Intraday Momentum, June 2017 author manuscript](https://assets.super.so/e46b77e7-ee08-445e-b43f-4ffd88ae0a0e/files/ee7dac49-530b-4950-b5d0-e0b5eee08f2e.pdf).

Reviewer estimates of 10–16% annual volatility and 12–23-bp half-hour volatility
were planning estimates, not certified measurements of the project's dates.
Converting annual volatility requires assumptions about intraday variance share,
time-of-day seasonality and dependence. The selected-trade distribution could
differ. No private real-price outcome pass was undertaken to narrow that gap.

The cited momentum study enters in the final half-hour. A full opening-hour
warm-up excludes early entries, not closing entries. The substantive mismatch
is its early-to-late predictor versus the proposed rolling recent-hour features.
The paper does not establish the draft's exact hypothesis.

The proposed descriptive variance pass would have computed an internal centering
mean and discarded it; it would not literally have avoided calculating any mean.
That pass, the zero-fit benchmark and the 48-fit learning study were all stopped
before execution. No sixty-minute rescue or alternative warm-up was launched.
