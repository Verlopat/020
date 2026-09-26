from arqf.metrics import gini,entropy
def test_gini_equal(): assert abs(gini([1,1,1,1]))<1e-12
def test_gini_extreme(): assert gini([0,0,1])>0.6
def test_entropy_equal(): assert abs(entropy([1,1,1])-1)<1e-12
