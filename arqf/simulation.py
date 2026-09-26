from dataclasses import dataclass
import numpy as np
@dataclass
class Scenario:
    name:str; sybil:bool=False; split:bool=False; collusion:bool=False; concentrated:bool=False
def make_scenarios():
    return [Scenario('normal'),Scenario('concentration',concentrated=True),Scenario('sybil',sybil=True),Scenario('splitting',split=True),Scenario('collusion',collusion=True),Scenario('mixed',True,True,True,True)]
def generate(seed,participants,projects,scenario,base=100.0):
    rng=np.random.default_rng(seed); utilities=rng.lognormal(0,0.7,projects)*base*8
    prefs=rng.integers(0,projects,participants); amounts=rng.lognormal(np.log(base),0.75,participants)
    if scenario.concentrated: amounts[:max(1,participants//20)]*=15
    if scenario.sybil:
        n=max(1,participants//10); prefs[:n]=prefs[0]; amounts[:n]=amounts[0]/n
    if scenario.split:
        n=max(1,participants//20); amounts[:n]/=10; prefs[:n]=prefs[0]
    if scenario.collusion:
        n=max(2,participants//20); prefs[:n]=prefs[0]; amounts[:n]*=3
    contrib=np.zeros((projects,participants))
    for i,(p,a) in enumerate(zip(prefs,amounts)): contrib[p,i]=a
    return contrib,utilities,amounts
