# Build and verification

Python:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python Main.py --help
pytest
python scripts/run_experiment.py
python scripts/analyze.py outputs/results.csv outputs/figures
```

Foundry:
```bash
forge install OpenZeppelin/openzeppelin-contracts --no-commit
forge install smartcontractkit/chainlink-brownie-contracts --no-commit
forge test
forge test --gas-report
```

A real testnet run additionally requires a funded deployer, an RPC endpoint and network-specific Chainlink VRF configuration. Those values are deliberately not committed.
