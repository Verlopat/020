"""Off-chain reference model for contract invariants and gas experiment schemas."""
from dataclasses import dataclass
@dataclass
class GasRecord:
    operation:str
    gas_used:int
    latency_seconds:float
def expected_round_invariants(contributions,total):
    assert contributions>=0 and total>=0
    return contributions<=total
