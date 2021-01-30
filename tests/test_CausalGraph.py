import pytest
from optimal_adjustment.CausalGraph import CausalGraph
from tests.examples import EXAMPLES, OPTIMALS, OPTIMALS_MINIMAL, OPTIMALS_MINIMUM


@pytest.mark.parametrize("example, optimal_stored", zip(EXAMPLES, OPTIMALS))
def test_optimal(example, optimal_stored):
    optimal = example.G.optimal_adj_set(treatment=example.treatment,
                                        outcome=example.outcome,
                                        L=example.L,
                                        N=example.N)
    assert optimal == optimal_stored


@pytest.mark.parametrize("example, optimal_minimal_stored", zip(EXAMPLES, OPTIMALS_MINIMAL))
def test_optimal_minimal(example, optimal_minimal_stored):
    optimal = example.G.optimal_minimal_adj_set(treatment=example.treatment,
                                                outcome=example.outcome,
                                                L=example.L,
                                                N=example.N)
    assert optimal == optimal_minimal_stored


@pytest.mark.parametrize("example, optimal_minimum_stored", zip(EXAMPLES, OPTIMALS_MINIMUM))
def test_optimal_minimal(example, optimal_minimum_stored):
    optimal = example.G.optimal_minimum_adj_set(treatment=example.treatment,
                                                outcome=example.outcome,
                                                L=example.L,
                                                N=example.N)
    assert optimal == optimal_minimum_stored
