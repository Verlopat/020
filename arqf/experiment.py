import csv,json,time
from pathlib import Path
import numpy as np
from .mechanisms import quadratic_funding,ar_qf,fairness_regulator
from .metrics import gini,entropy,hhi,welfare,top_share
from .simulation import make_scenarios,generate
def run(cfg,outdir):
    outdir=Path(outdir); outdir.mkdir(parents=True,exist_ok=True); rows=[]; started=time.time()
    for scenario in make_scenarios():
        for seed in range(cfg.seeds):
            c,u,_=generate(seed,cfg.participants,cfg.projects,scenario,cfg.base_contribution)
            q=quadratic_funding(c,cfg.matching_pool); qf,_=fairness_regulator(q,cfg.matching_pool,cfg.fairness_gini_max,cfg.min_project_share)
            ar,alpha=ar_qf(c,cfg.matching_pool,np.random.default_rng(seed+10000),cfg.adaptive_strength,cfg.random_temperature)
            arf,_=fairness_regulator(ar,cfg.matching_pool,cfg.fairness_gini_max,cfg.min_project_share)
            for mech,f in {'qf':q,'qf_fair':qf,'arqf':arf}.items():
                rows.append({'scenario':scenario.name,'seed':seed,'mechanism':mech,'participants':cfg.participants,'projects':cfg.projects,'contribution_total':float(c.sum()),'matching_total':cfg.matching_pool,'project_funding':float(f.sum()),'gini':gini(f),'entropy':entropy(c.sum(axis=0)),'welfare':welfare(f,u),'sybil_gain':0.0,'collusion_gain':0.0,'hhi':hhi(f),'top1_share':top_share(f,1),'top5_share':top_share(f,min(5,cfg.projects)),'adaptive_alpha':alpha if mech=='arqf' else 1.0})
    idx={(r['scenario'],r['seed'],r['mechanism']):r for r in rows}
    for r in rows:
        if r['scenario']!='normal':
            n=idx[('normal',r['seed'],r['mechanism'])]; gain=(r['project_funding']-n['project_funding'])/max(n['project_funding'],1e-12)
            if r['scenario'] in ('sybil','splitting','mixed'):r['sybil_gain']=gain
            if r['scenario'] in ('collusion','mixed'):r['collusion_gain']=gain
    with (outdir/'results.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    summary=[]
    for s,m in sorted(set((r['scenario'],r['mechanism']) for r in rows)):
        g=[r for r in rows if r['scenario']==s and r['mechanism']==m]
        summary.append({'scenario':s,'mechanism':m,'runs':len(g),'mean_gini':float(np.mean([x['gini'] for x in g])),'std_gini':float(np.std([x['gini'] for x in g],ddof=1)) if len(g)>1 else 0.0,'mean_welfare':float(np.mean([x['welfare'] for x in g])),'mean_sybil_gain':float(np.mean([x['sybil_gain'] for x in g])),'mean_collusion_gain':float(np.mean([x['collusion_gain'] for x in g]))})
    with (outdir/'summary.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(summary[0])); w.writeheader(); w.writerows(summary)
    (outdir/'metadata.json').write_text(json.dumps({'elapsed_seconds':time.time()-started,'config':cfg.__dict__,'rows':len(rows)},indent=2))
    return rows
