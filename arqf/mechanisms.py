import numpy as np
from .metrics import gini,entropy
def quadratic_funding(contrib,matching_pool):
    scores=np.asarray([float(np.square(np.sqrt(np.clip(r,0,None)).sum())) for r in contrib])
    total=scores.sum(); match=np.zeros_like(scores) if total<=0 else matching_pool*scores/total
    return contrib.sum(axis=1)+match
def adaptive_alpha(contrib,strength=0.75):
    t=contrib.sum(axis=0); return float(np.clip(1+strength*(gini(t)-(entropy(t)-0.5)),0.70,1.60))
def ar_qf(contrib,matching_pool,rng,strength=0.75,temperature=0.20):
    alpha=adaptive_alpha(contrib,strength)
    raw=np.asarray([float(np.power(np.sqrt(np.clip(r,0,None)).sum(),2*alpha)) for r in contrib])
    scores=raw*rng.lognormal(0,temperature,len(raw)); total=scores.sum()
    match=np.zeros_like(scores) if total<=0 else matching_pool*scores/total
    return contrib.sum(axis=1)+match,alpha
def fairness_regulator(funding,matching_pool,gini_max=0.35,min_share=0.005):
    f=np.asarray(funding,float).copy()
    if f.sum()<=0:return f,False
    changed=False; floor=matching_pool*min_share
    for _ in range(50):
        if gini(f)<=gini_max and np.all(f>=floor):break
        low=np.where(f<floor)[0]; high=np.where(f>f.mean())[0]
        if len(low)==0 or len(high)==0:break
        need=float(np.sum(floor-f[low])); donor=high[np.argmax(f[high])]
        take=min(need,max(0.0,f[donor]-f.mean()))
        if take<=1e-12:break
        f[donor]-=take; f[low]+=take/len(low); changed=True
    return f,changed
