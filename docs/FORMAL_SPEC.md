# Formal AR-QF specification

Let projects be i=1..m and contributors j=1..n. Let c_ij>=0 be the contribution of j to i and M the matching pool.

Baseline quadratic score:
S_i = (sum_j sqrt(c_ij))^2.
Baseline allocation:
A_i = sum_j c_ij + M S_i/sum_k S_k, when the denominator is positive.

Participation weights p_j=c_j/sum_l c_l. Normalized participation entropy:
H = -sum_j p_j log(p_j)/log(n).

Let C be contributor-level Gini and H the normalized entropy. The current executable adaptive rule is:
alpha = clip(1 + lambda(C-(H-0.5)), alpha_min, alpha_max).

The randomized AR-QF provisional score is:
R_i = (sum_j sqrt(c_ij))^(2 alpha) * Z_i,
where log Z_i is Gaussian with mean 0 and configured standard deviation.

The regulator is a deterministic correction operator subject to explicit parameters: a minimum project floor derived from M and a maximum project-funding Gini target.

Important: these definitions support an executable experimental specification, but they do NOT by themselves prove an unconditional fairness theorem. A formal guarantee must state the admissible domain and prove that the correction operator terminates and satisfies the target constraints on that domain.
