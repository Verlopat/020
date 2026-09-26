# Dataset dictionary

| Field | Meaning |
|---|---|
| seed | independent experiment seed |
| scenario | experimental condition |
| mechanism | QF, QF+fairness, or AR-QF |
| participants/projects | population dimensions |
| contribution_total/matching_total | money entering the round |
| project_funding | final allocation total |
| gini/contribution_gini | funding and contributor concentration |
| entropy | normalized contributor participation entropy |
| hhi | project funding HHI |
| top1/top5/top10_share | largest project funding shares |
| contributor_top1/top5/top10_share | largest contributor contribution shares |
| sybil_gain/collusion_gain | adversarial gain relative to same-seed normal condition |
| adaptive_alpha | AR-QF adaptive parameter |
| gas_used/transaction_count/latency_seconds | live-chain measurement fields |
