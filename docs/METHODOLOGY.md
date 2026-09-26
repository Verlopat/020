# Experimental methodology

## Compared mechanisms
1. Conventional quadratic funding (QF).
2. QF plus the explicit fairness regulator.
3. Adaptive randomized QF (AR-QF) plus the same regulator.

## Scenarios
normal, concentration, sybil, splitting, collusion, and mixed adversarial participation.

## Metrics
Project-funding Gini, normalized participation entropy, funding HHI, top-1/top-5 project shares, welfare, Sybil gain, collusion gain, and adaptive exponent.

## Fairness rule
The regulator uses a maximum project-funding Gini and a minimum matching-pool-derived project floor. This is an operational constraint, not a universal fairness theorem.

## Reproducibility
Each seed is independent. Results contain scenario, seed, mechanism, participant/project counts, financial totals, and metric values. Every invocation creates a new output/testN directory.
