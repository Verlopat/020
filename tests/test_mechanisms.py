import numpy as np
from arqf.mechanisms import quadratic_funding,ar_qf,fairness_regulator
def test_qf_preserves_positive_matching():
    c=np.array([[100,100,0],[0,0,100]],float); assert quadratic_funding(c,1000).sum()>c.sum()
def test_arqf_seed_reproducible():
    c=np.array([[1,2,3],[4,5,6]],float); a,_=ar_qf(c,100,np.random.default_rng(1)); b,_=ar_qf(c,100,np.random.default_rng(1)); assert np.allclose(a,b)
def test_regulator_preserves_total():
    x=np.array([1000.,1.,1.,1.]); y,_=fairness_regulator(x,100,0.9,0.01); assert abs(y.sum()-x.sum())<1e-9
