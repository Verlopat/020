import math
import numpy as np
def gini(values):
    x=np.asarray(values,dtype=float)
    if x.size==0 or np.allclose(x.sum(),0): return 0.0
    x=np.sort(np.clip(x,0,None)); n=x.size
    return float((2*np.arange(1,n+1)@x)/(n*x.sum())-(n+1)/n)
def entropy(values):
    x=np.asarray(values,dtype=float); s=x.sum()
    if s<=0:return 0.0
    p=x[x>0]/s
    return float(-(p*np.log(p)).sum()/math.log(len(x))) if len(x)>1 else 0.0
def hhi(values):
    x=np.asarray(values,dtype=float); s=x.sum()
    return float(((x/s)**2).sum()) if s>0 else 0.0
def welfare(funding,utility):
    return float(np.minimum(np.asarray(funding,float),np.asarray(utility,float)).sum())
def top_share(values,k):
    x=np.asarray(values,float); s=x.sum()
    return float(np.sort(x)[-k:].sum()/s) if s>0 else 0.0
