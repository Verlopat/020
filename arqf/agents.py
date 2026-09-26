from dataclasses import dataclass
import numpy as np
@dataclass
class Agent:
    agent_id:int
    identity_group:int
    kind:str
    budget:float
    participation_frequency:float
    preferred_projects:tuple
    def contribution(self,rng,base):
        if rng.random()>self.participation_frequency:return 0.0
        return float(max(0.0,rng.lognormal(np.log(base),.6)))
def create_agents(seed,n,projects,scenario,base=100.0):
    rng=np.random.default_rng(seed); agents=[]
    sybil_n=max(1,n//20) if scenario in ("sybil","mixed") else 0
    collude_n=max(2,n//20) if scenario in ("collusion","mixed") else 0
    for i in range(n):
        kind="honest"; group=i
        if i<sybil_n: kind="sybil";group=0
        elif i<sybil_n+collude_n: kind="colluder";group=1
        if scenario=="concentration" and i<n//20: kind="large"
        if scenario in ("normal","high_diversity"): freq=rng.uniform(.35,.95)
        elif scenario=="low_diversity": freq=rng.uniform(.05,.25)
        else: freq=rng.uniform(.2,.8)
        prefs=tuple(rng.choice(projects,size=max(1,min(3,projects)),replace=False))
        agents.append(Agent(i,group,kind,float(rng.lognormal(np.log(base),.6)),float(freq),prefs))
    return agents
