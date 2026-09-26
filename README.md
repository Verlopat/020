# Adaptive Randomized Quadratic Funding (AR-QF)

Research implementation for a public-goods funding mechanism combining quadratic funding, adaptive participation parameters, randomized allocation, and explicit fairness regulation.

## Run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 Main.py
```

Every execution creates a new `output/testN/` directory containing `results.csv`, `summary.csv`, and `metadata.json`.

The default experiment uses 500 participants, 20 projects, 20 seeds, and six participation/adversarial scenarios. It compares conventional QF, QF with fairness regulation, and AR-QF.

## Method

The implementation follows the supplied research specification: contribution collection, participation analysis, adaptive parameter selection, randomized matching, fairness regulation, and statistical evaluation. It records funding inequality (Gini), participation entropy, welfare, HHI, top-contributor/project concentration, Sybil gain, collusion gain, and adaptive parameters.

The fairness threshold is explicit and configurable. It is an experimental constraint, not a claim of universal fairness; a formal guarantee requires proving the exact regulator and admissible input domain.

## Smart contracts

- `contracts/ARQF.sol`: EVM round/contribution state and randomness-request boundary.
- `contracts/ARQFVRFConsumer.sol`: Chainlink VRF v2.5-compatible consumer boundary.

Chainlink describes VRF as a verifiable randomness service. This repository deliberately does not fabricate a deployed coordinator, subscription, key hash, or testnet address; those are network/deployment parameters. See the official Chainlink documentation: https://docs.chain.link/

The Solidity layer requires the Chainlink contracts package when compiling with Foundry. The Python research pipeline does not require blockchain credentials.

## Tests

```bash
pytest -q
```

## CLI

```bash
python3 Main.py --participants 1000 --projects 30 --seeds 50 --matching-pool 250000
```

## Project layout

```
Main.py
arqf/
  cli.py
  config.py
  experiment.py
  mechanisms.py
  metrics.py
  simulation.py
contracts/
  ARQF.sol
  ARQFVRFConsumer.sol
tests/
config/default.json
docs/METHODOLOGY.md
```

## Reproducibility

Each seed is independent. Raw rows and aggregate summaries are written to the numbered output directory created for that run. This supports repeated experiments without overwriting prior results.

## Research scope

The supplied specification calls for formal definitions of baseline QF, adaptive amplification, diversity, entropy, fairness constraints, randomization, and correction before claiming formal fairness guarantees. This implementation makes those components executable and testable; the theorem/proof layer remains a separate mathematical research task rather than an unsupported claim.
