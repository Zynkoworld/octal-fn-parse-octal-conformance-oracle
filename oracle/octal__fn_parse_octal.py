"""octal-fn-parse-octal-conformance-oracle -- deterministic CONFORMANCE oracle for `octal` (python).

WHAT THIS DECIDES: given a candidate callable and one canonical input, it decides whether the candidate
agrees with the proven reference. It is a *conformance* decider over a fixed, published corpus -- it does
not decide correctness in general, and it says nothing about inputs outside the corpus.

SCOPE (declared, so the boundary is visible rather than discovered): the corpus is the canonical Exercism
test data for this task, 6 input/output pairs, listed in `probes/probes.jsonl`. Inputs outside that
set are simply not covered; `decide` answers only about the input it is given.

PARTIAL: the reference raises on 2 of the canonical inputs (input validation); those cases are recorded in `probes/known_limitations.jsonl` and are NOT part of the gate.

PROVENANCE: the reference body comes from the Exercism reference solution for `octal` (MIT, Exercism);
the type annotations were added by harvest, the body is unchanged (checked at AST level). The capability
was PROVEN by the exercism testsuite (pin=8078fa769fdd60f1) and re-executed by harvest in a sealed sandbox
(unshare -rn) -- verify-not-relay, not a copied ledger label.
"""

TASK = "octal"
CWE = "octal"          # a publish-motor egyseges mezonevet var; itt a feladat azonositoja


def decide(fn, value, expect):
    """PASS iff fn(value) == expect. Determinista, nincs halozat, nincs allapot."""
    try:
        return "PASS" if fn(value) == expect else "FAIL"
    except Exception:                                      # noqa: BLE001
        return "FAIL"


def _validate_octal(digits):
    for digit in digits:
        if not '0' <= digit < '8':
            raise ValueError('Invalid octal digit: ' + digit)
    return digits

def parse_octal(digits: str) -> int:
    digits = _validate_octal(digits)
    return sum((int(digit) * 8 ** idx for idx, digit in enumerate(reversed(digits))))

REFERENCE = parse_octal
