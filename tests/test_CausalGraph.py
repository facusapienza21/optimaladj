import pytest
from optimaladj.CausalGraph import ConditionException, NoAdjException
from tests.examples import EXAMPLES, OPTIMALS, OPTIMALS_MINIMAL, OPTIMALS_MINIMUM


@pytest.mark.parametrize("example, optimal_stored", zip(EXAMPLES[0:3], OPTIMALS[0:3]))
def test_optimal(example, optimal_stored):
    optimal = example.G.optimal_adj_set(treatment=example.treatment,
                                        outcome=example.outcome,
                                        L=example.L,
                                        N=example.N)
    assert optimal == optimal_stored


@pytest.mark.parametrize("example", EXAMPLES[3:5])
def test_optimal_failure(example):
    with pytest.raises(ConditionException):
        example.G.optimal_adj_set(treatment=example.treatment,
                                  outcome=example.outcome,
                                  L=example.L,
                                  N=example.N)


@pytest.mark.parametrize("example, optimal_minimal_stored", zip(EXAMPLES[0:5], OPTIMALS_MINIMAL[0:5]))
def test_optimal_minimal(example, optimal_minimal_stored):
    optimal = example.G.optimal_minimal_adj_set(treatment=example.treatment,
                                                outcome=example.outcome,
                                                L=example.L,
                                                N=example.N)
    assert optimal == optimal_minimal_stored


@pytest.mark.parametrize("example, optimal_minimum_stored", zip(EXAMPLES[0:5], OPTIMALS_MINIMUM[0:5]))
def test_optimal_minimum(example, optimal_minimum_stored):
    optimal = example.G.optimal_minimum_adj_set(treatment=example.treatment,
                                                outcome=example.outcome,
                                                L=example.L,
                                                N=example.N)
    assert optimal == optimal_minimum_stored


def test_no_adj_optimal(example=EXAMPLES[5]):
    with pytest.raises(NoAdjException):
        example.G.optimal_adj_set(treatment=example.treatment,
                                  outcome=example.outcome,
                                  L=example.L,
                                  N=example.N)


def test_no_adj_minimal_optimal(example=EXAMPLES[5]):
    with pytest.raises(NoAdjException):
        example.G.optimal_minimal_adj_set(treatment=example.treatment,
                                          outcome=example.outcome,
                                          L=example.L,
                                          N=example.N)


def test_no_adj_minimum_optimal(example=EXAMPLES[5]):
    with pytest.raises(NoAdjException):
        example.G.optimal_minimum_adj_set(treatment=example.treatment,
                                          outcome=example.outcome,
                                          L=example.L,
                                          N=example.N)
