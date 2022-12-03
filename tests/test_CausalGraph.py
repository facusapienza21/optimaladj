import pytest

from optimaladj.CausalGraph import ConditionException, NoAdjException
from tests.examples import (
    EXAMPLES,
    OPTIMALS,
    OPTIMALS_MINCOST,
    OPTIMALS_MINIMAL,
    OPTIMALS_MINIMUM,
)


def test_no_adj_optimal(example=EXAMPLES[0]):
    with pytest.raises(NoAdjException):
        example.G.optimal_adj_set(
            treatment=example.treatment,
            outcome=example.outcome,
            L=example.L,
            N=example.N,
        )


def test_no_adj_minimal_optimal(example=EXAMPLES[0]):
    with pytest.raises(NoAdjException):
        example.G.optimal_minimal_adj_set(
            treatment=example.treatment,
            outcome=example.outcome,
            L=example.L,
            N=example.N,
        )


def test_no_adj_minimum_optimal(example=EXAMPLES[0]):
    with pytest.raises(NoAdjException):
        example.G.optimal_minimum_adj_set(
            treatment=example.treatment,
            outcome=example.outcome,
            L=example.L,
            N=example.N,
        )


@pytest.mark.parametrize(
    "example, optimal_stored",
    zip(EXAMPLES[1:4] + EXAMPLES[8:12], OPTIMALS[1:4] + OPTIMALS[8:12]),
)
def test_optimal(example, optimal_stored):
    optimal = example.G.optimal_adj_set(
        treatment=example.treatment, outcome=example.outcome, L=example.L, N=example.N
    )
    assert optimal == optimal_stored


@pytest.mark.parametrize("example", EXAMPLES[4:6])
def test_optimal_failure(example):
    with pytest.raises(ConditionException):
        example.G.optimal_adj_set(
            treatment=example.treatment,
            outcome=example.outcome,
            L=example.L,
            N=example.N,
        )


@pytest.mark.parametrize(
    "example, optimal_minimal_stored", zip(EXAMPLES[1:12], OPTIMALS_MINIMAL[1:12])
)
def test_optimal_minimal(example, optimal_minimal_stored):
    optimal = example.G.optimal_minimal_adj_set(
        treatment=example.treatment, outcome=example.outcome, L=example.L, N=example.N
    )
    assert optimal == optimal_minimal_stored


@pytest.mark.parametrize(
    "example, optimal_minimum_stored", zip(EXAMPLES[1:12], OPTIMALS_MINIMUM[1:12])
)
def test_optimal_minimum(example, optimal_minimum_stored):
    optimal = example.G.optimal_minimum_adj_set(
        treatment=example.treatment, outcome=example.outcome, L=example.L, N=example.N
    )
    assert optimal == optimal_minimum_stored


@pytest.mark.parametrize(
    "example, optimal_mincost_stored", zip(EXAMPLES[1:12], OPTIMALS_MINCOST[1:12])
)
def test_optimal_mincost(example, optimal_mincost_stored):
    optimal = example.G.optimal_mincost_adj_set(
        treatment=example.treatment, outcome=example.outcome, L=example.L, N=example.N
    )
    assert optimal == optimal_mincost_stored
