"""Research-grade statistical and plotting helpers.
All functions operate on explicit arrays/dataframes and are deterministic.
"""
from pathlib import Path
import numpy as np

def lorenz(values):
    x=np.sort(np.clip(np.asarray(values,dtype=float),0,None))
    if x.size==0 or x.sum()<=0:return np.array([0.0,1.0]),np.array([0.0,1.0])
    return np.r_[0.0,np.cumsum(x)/x.sum()],np.linspace(0,1,len(x)+1)

def concentration(values,ks=(1,5,10)):
    x=np.asarray(values,float); s=x.sum()
    return {f"top{k}_share":float(np.sort(x)[-min(k,len(x)):].sum()/s) if s>0 else 0.0 for k in ks}

def bootstrap_mean(values,iterations=2000,seed=0):
    x=np.asarray(values,float); rng=np.random.default_rng(seed)
    if x.size==0:return {"mean":0.0,"lower":0.0,"upper":0.0}
    means=np.mean(rng.choice(x,(iterations,len(x)),replace=True),axis=1)
    return {"mean":float(x.mean()),"lower":float(np.quantile(means,.025)),"upper":float(np.quantile(means,.975))}

def summarize_csv(path,outdir):
    import csv
    from collections import defaultdict
    rows=list(csv.DictReader(Path(path).open()))
    groups=defaultdict(list)
    for r in rows: groups[(r["scenario"],r["mechanism"])].append(r)
    out=Path(outdir); out.mkdir(parents=True,exist_ok=True)
    summary=[]
    for (scenario,mechanism),rs in sorted(groups.items()):
        g=np.array([float(r["gini"]) for r in rs]); w=np.array([float(r["welfare"]) for r in rs])
        ci=bootstrap_mean(g)
        summary.append({"scenario":scenario,"mechanism":mechanism,"runs":len(rs),"gini_mean":float(g.mean()),"gini_ci_low":ci["lower"],"gini_ci_high":ci["upper"],"welfare_mean":float(w.mean()),"welfare_std":float(w.std(ddof=1)) if len(w)>1 else 0.0})
    with (out/"statistical_summary.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=summary[0].keys());w.writeheader();w.writerows(summary)
    return summary

def make_figures(results_csv,outdir):
    """Generate Lorenz and mechanism/scenario figures when matplotlib is installed."""
    import csv
    import matplotlib.pyplot as plt
    rows=list(csv.DictReader(Path(results_csv).open())); out=Path(outdir);out.mkdir(parents=True,exist_ok=True)
    for mechanism in sorted(set(r["mechanism"] for r in rows)):
        vals=[float(r["gini"]) for r in rows if r["mechanism"]==mechanism]
        plt.figure();plt.hist(vals,bins=12);plt.xlabel("Funding Gini");plt.ylabel("Runs");plt.title(mechanism);plt.tight_layout();plt.savefig(out/f"{mechanism}_gini.png",dpi=180);plt.close()
    return sorted(str(p) for p in out.glob("*.png"))
