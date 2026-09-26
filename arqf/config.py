from dataclasses import dataclass
@dataclass(frozen=True)
class ExperimentConfig:
    participants:int=500; projects:int=20; matching_pool:float=100000.0; seeds:int=20
    sybil_count:int=10; colluding_group:int=10; base_contribution:float=100.0
    fairness_gini_max:float=0.35; min_project_share:float=0.005; adaptive_strength:float=0.75
    random_temperature:float=0.20
    scenarios:tuple=('normal','concentration','sybil','splitting','collusion','mixed')
