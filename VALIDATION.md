# Publication validation

Prepared and checked October 9, 2026. These checks verify a results publication,
not a new scientific run.

- Both original aggregate reports matched their retained original SHA-256
  values and their internal payload seals.
- All forty strongest-setting case files matched Stage 2D's report hashes and
  their own seals before the 1,440-row export was created.
- All 396 reported count cells and ten detection settings were checked.
- All 200 Stage 2E seed aggregates reconciled to the ten trade-weighted pooled
  summaries; gross, net, cost components and paired increments reconciled.
- The thirty-minute capacity and stated planning scenarios reproduced.
- Relative document links resolved within the release.
- The release content scan found no private machine paths, database connection
  strings, private IP addresses, email addresses or credential assignments.
- Verification passed from a copied release in a fresh temporary directory.
- Altering the original Stage 2E report by one byte caused verification to fail.

Run `python3 tools/verify_results.py` from the release root to repeat the public
aggregate checks. `CHECKSUMS.sha256` covers the release files other than itself.
File integrity does not independently authenticate a private registry or
reproduce a scientific model from unavailable inputs.

No model was fitted, dataset generated, registry accessed or real outcome
analysis started in preparing this publication.
