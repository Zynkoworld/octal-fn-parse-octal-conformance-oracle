# zynko-oracle · `octal-fn-parse-octal-conformance-oracle`

**A deterministic, re-checkable conformance oracle for `octal` (Python).**

An **oracle** *deterministically decides* the truth of a case — it doesn't guess, it decides. This one
decides, for a candidate implementation and a canonical input, whether the candidate **agrees with the
proven reference**.

## Proven
Measured on the **canonical Exercism corpus** for this task — **6 input/output pairs, 6 distinct
outputs** — verified by *running* the reference, not asserted:

```
agree = 6/6    mismatch = 0    non-degenerate = yes  ->  PASS
```

`verify.py` (stdlib only, no network) is the CI gate. The inputs and the expected outputs are **published
in full** in `probes/probes.jsonl`, so the corpus this claim rests on is visible and re-runnable — a probe
set is a floor on behaviour, not a coverage measure.

## Scope (declared)
The corpus is the canonical Exercism test data for `octal`. Inputs outside that set are **not covered**;
`decide` answers only about the input it is given, and makes no claim of correctness in general.

**Partial:** the reference *raises* on 2 canonical input(s) (input validation). Those are recorded in `probes/known_limitations.jsonl` and are deliberately **not** part of the gate — labelling them as agreement would hide the gap instead of recording it.

## Provenance
The reference body is the Exercism reference solution for `octal` (MIT, Exercism); harvest added the
type annotations and left the body unchanged (checked at AST level). The capability was **proven by the
exercism testsuite** (`pin=8078fa769fdd60f1`) and **re-executed by harvest in a sealed sandbox** (`unshare -rn`)
before this bundle was generated — the outputs below are that run's, not a copied ledger label.

## License
Apache-2.0 for the oracle scaffolding (see `LICENSE`); the reference body retains its upstream MIT
(Exercism) license, as recorded above.
