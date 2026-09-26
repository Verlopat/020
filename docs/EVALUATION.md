# Evaluation protocol

Run each mechanism over the same seeds and scenario configuration. Report mean, standard deviation and bootstrap 95% confidence intervals.

Required scenario matrix:
normal, high contribution concentration, Sybil, contribution splitting, collusion, mixed adversarial, high participation diversity, low participation diversity.

Primary outcomes: funding Gini, contribution Gini, participation entropy, HHI, top-1/top-5/top-10 contributor shares, funded-project count, welfare per matching unit, Sybil gain, collusion gain.

Blockchain outcomes: contribution gas, round-finalization gas, allocation gas, transaction count, VRF overhead and measured RPC/receipt latency.

Do not infer causal claims from one seed. Preserve raw rows and configuration alongside processed summaries.
