# Adaptive Randomized Quadratic Funding (AR-QF)

A Python-based research implementation for studying adaptive randomized quadratic funding (AR-QF), a public-goods funding mechanism that combines:

- conventional quadratic funding (QF)
- explicit fairness regulation
- adaptive participation weighting
- randomized allocation under adversarial participation scenarios

The repository models and compares three mechanisms across simulated participant/project conditions, with outputs designed for reproducible experimentation and analysis.

## Why this project?

The goal is to evaluate how funding allocation changes when a mechanism adapts to participation concentration, Sybil behavior, collusion, splitting, and mixed adversarial conditions. The project includes a configurable experimental framework and a Solidity smart-contract boundary for a blockchain-integrated version of the same funding logic.

## Key features

- Experiment runner for multiple seeds and scenarios
- Comparison of:
  - baseline QF
  - QF with fairness regulation
  - AR-QF with fairness regulation
- Scenario coverage for normal, concentrated, Sybil, splitting, collusion, and mixed adversarial participation
- Metrics for distributional fairness, welfare, concentration, entropy, and adversarial gain
- Reproducible output folders with raw and aggregate results
- Solidity contract interfaces for EVM deployment boundaries

## Repository layout

```text
.
├── Main.py                     # entry point for the experiment runner
├── README.md
├── requirements.txt
├── pyproject.toml
├── foundry.toml
├── .env.example
├── arqf/
│   ├── cli.py
│   ├── config.py
│   ├── experiment.py
│   ├── mechanisms.py
│   ├── metrics.py
│   └── simulation.py
├── config/
│   └── default.json
├── contracts/
│   ├── ARQF.sol
│   └── ARQFVRFConsumer.sol
├── deploy/
│   └── README.md
├── docs/
│   └── METHODOLOGY.md
├── notebooks/
├── script/
├── scripts/
├── test/
├── tests/
└── output/                     # generated at runtime
```

## Installation

This project targets Python 3.10+.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If you want to use the package metadata from the project config as well, the repository also exposes a `pyproject.toml` configuration.

## Quick start

Run the default experiment:

```bash
python3 Main.py
```

Run with custom experiment parameters:

```bash
python3 Main.py --participants 1000 --projects 30 --seeds 50 --matching-pool 250000
```

Each run creates a new numbered output directory such as:

```text
output/test1/
├── results.csv
├── summary.csv
├── metadata.json
```

## Default configuration

The default experiment settings live in `config/default.json`:

```json
{
  "participants": 500,
  "projects": 20,
  "matching_pool": 100000,
  "seeds": 20,
  "fairness_gini_max": 0.35,
  "min_project_share": 0.005,
  "adaptive_strength": 0.75,
  "random_temperature": 0.2
}
```

You can adjust these values directly or override them from the CLI.

## Methodology

The implementation follows the project methodology described in `docs/METHODOLOGY.md` and compares three funding regimes:

1. conventional quadratic funding (QF)
2. QF with explicit fairness regulation
3. adaptive randomized QF (AR-QF) with the same fairness regulator

The experimental design evaluates distributional fairness, concentration, entropy, welfare, and adversarial participation effects across multiple scenarios.

## Smart contracts

The repository includes Solidity contract interfaces intended for EVM-based experimentation:

- `contracts/ARQF.sol`: round/contribution state and randomness request boundary
- `contracts/ARQFVRFConsumer.sol`: Chainlink VRF v2.5-compatible consumer interface

These contracts are designed for reproducible experimentation and deployment boundaries. The project does not assume a specific deployed Chainlink coordinator, key hash, or testnet address; those values must be supplied by the operator when deploying to a live network.

## Testing

Run the test suite with:

```bash
pytest -q
```

## Reproducibility

The project is built around independent seeds and deterministic output generation. Each execution creates a fresh numbered `output/testN/` directory so that results from different runs do not overwrite each other.

This allows repeated experimentation, comparison across mechanisms, and auditing of raw outputs and aggregate summaries.

## Research notes

This repository is a research implementation rather than a production-grade fairness guarantee. The fairness threshold is explicit and configurable, but it should be viewed as an operational constraint used in simulation rather than a universal or mathematically complete fairness theorem.

For more detail on the experimental framing and metrics, see:

- `docs/METHODOLOGY.md`
- `deploy/README.md`

## License

This repository currently does not appear to declare a license in the root directory. If you plan to reuse or distribute the code publicly, consider adding an explicit license file such as MIT, Apache-2.0, or GPL-3.0.

## Contributing

Contributions are welcome. If you are extending the model, adjusting the fairness regulator, or adding new scenarios or metrics, keep the workflow reproducible and document any new configuration knobs in the relevant config and docs files.
