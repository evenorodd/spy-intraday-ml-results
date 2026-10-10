# Public results release

The public results repository is
[evenorodd/spy-intraday-ml-results](https://github.com/evenorodd/spy-intraday-ml-results).
The scientific closeout is dated October 9, 2026; this publication is dated
October 10, 2026. Publication commits are separate from the frozen scientific
implementation commit.

This release contains reviewed reports, aggregate evidence and a verifier. The
original Stage 2D and Stage 2E aggregate report bytes remain unchanged. Raw vendor
prices, individual trades and private registry contents remain outside the
public release.

## Review and verify

Open `README.md` and `CLOSEOUT.md`. From a downloaded or cloned copy of this
repository, run:

```bash
python3 tools/verify_results.py
```

Verification requires only Python 3.10+ and the standard library. It checks the
published files and aggregate accounting without accessing a database or
starting a scientific run.

The earlier preparation ZIP contains a single `spy-intraday-ml-results/` folder.
Its publication helper described the then-pending upload; this repository updates
that administrative file and its checksum. Keep any downloaded results copy
separate from the frozen scientific checkout. Publication does not require
changing that checkout or its retained study records.
