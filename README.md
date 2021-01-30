# Optimal adjustment sets

This package implements the algorithms introduced in [Smucler, Sapienza and Rotnitzky (2020)] (https://arxiv.org/abs/2004.10521) to compute optimal adjustment sets in causal graphical models.
The package provides a class (CasualGraph) that inherits from networkx's DiGraph and has methods
to compute: the optimal, optimal minimal and optimal minimum adjustment sets for individualized
treatment rules (point exposure dynamic treatment regimes) in causal graphical models with latent variables.