# optimaladj: A library for computing optimal adjustment sets in causal graphical models

This package implements the algorithms introduced in [Smucler, Sapienza and Rotnitzky (2021)](https://doi.org/10.1093/biomet/asab018) and
[Smucler and Rotnitzky (2022)](https://arxiv.org/abs/2201.02037) to compute optimal adjustment sets in causal graphical models.
The package provides a class, called CasualGraph, that inherits from [networkx's](https://networkx.org/) DiGraph class and has methods
to compute: the optimal, optimal minimal, optimal minimum cardinality and optimal minimum cost adjustment sets for individualized
treatment rules (point exposure dynamic treatment regimes) in non-parametric causal graphical
models with latent variables. 

Suppose we are given a causal graph G specifying:

* a treatment variable A,
* an outcome variable Y,
* a set of observable (that is, non-latent) variables N,
* a set of observable variables that will be used to allocate treatment L, and possibly
* positive costs associated with each observable variable.

Suppose moreover that there exists at least one adjustment set with respect to A and Y in G that is comprised of observable variables.

An optimal adjustment set is an observable adjustment set that yields the non-parametric estimator of the interventional mean with the smallest asymptotic variance among those that are based on observable adjustment sets. 

An optimal minimal adjustment set is an observable adjustment set that yields the non-parametric estimator of the interventional mean with the smallest asymptotic variance among those that are based on observable minimal adjustment sets. An observable minimal adjustment set is a valid adjustment set such that all its variables are observable and the removal of any variable from it destroys validity.

An optimal minimum cardinality adjustment set is an observable adjustment set that has minimum possible cardinality and yields the non-parametric estimator of the interventional mean with the smallest asymptotic variance among those that are based on observable minimum cardinality adjustment sets.

An optimal minimum cost adjustment set is defined similarly, being optimal in the class of observable adjustment sets that have minimum possible cost.

Under these assumptions, [Smucler, Sapienza and Rotnitzky (2020)](https://arxiv.org/abs/2004.10521) and [Smucler and Rotnitzky (2022)](https://arxiv.org/abs/2201.02037) show that 
optimal minimal, optimal minimum cardinality and optimal minimum cost adjustment sets always exist, and can be computed in polynomial time. They also provide a sufficient criterion for the existance of an optimal adjustment set and a polynomial time algorithm to compute it when it exists.

Check out our notebook with [examples](https://github.com/facusapienza21/optimaladj/blob/main/examples/Examples.ipynb).

## Installation

You can install the stable version of the package from [PyPI](https://pypi.org/project/optimaladj/0.0.1/) by running

```sh
pip install optimaladj
```

You can install the development version of the package from Github by running

```sh
pip install git+https://github.com/facusapienza21/optimaladj.git#egg=optimaladj
```


