from optimaladj.CausalGraph import CausalGraph


class CausalGraphExample:
    def __init__(self, G, treatment, outcome, L, N, costs=None):
        self.G = G
        self.treatment = treatment
        self.outcome = outcome
        self.L = L
        self.N = N
        self.costs = costs


EXAMPLES = []
OPTIMALS = []
OPTIMALS_MINIMAL = []
OPTIMALS_MINIMUM = []
OPTIMALS_MINCOST = []

# Example with no observable adjustment set
G_0 = CausalGraph()
G_0.add_edges_from([("A", "Y"), ("U", "Y"), ("U", "A")])
L_0 = []
N_0 = ["A", "Y"]
treatment_0 = "A"
outcome_0 = "Y"

EXAMPLES.append(CausalGraphExample(G_0, treatment_0, outcome_0, L_0, N_0))

OPTIMALS.append("An adjustment set formed by observable variables does not exist")
OPTIMALS_MINIMAL.append(
    "An adjustment set formed by observable variables does not exist"
)
OPTIMALS_MINIMUM.append(
    "An adjustment set formed by observable variables does not exist"
)

# Figure 1 of the Biometrika paper

G_epi = CausalGraph()
G_epi.add_edges_from(
    [
        ("coach", "team motivation"),
        ("coach", "fitness"),
        ("fitness", "pre-game prop"),
        ("fitness", "neuromusc fatigue"),
        ("team motivation", "warm-up"),
        ("team motivation", "previous injury"),
        ("pre-game prop", "warm-up"),
        ("warm-up", "intra-game prop"),
        ("contact sport", "previous injury"),
        ("contact sport", "intra-game prop"),
        ("intra-game prop", "injury"),
        ("genetics", "fitness"),
        ("genetics", "neuromusc fatigue"),
        ("genetics", "tissue disorder"),
        ("tissue disorder", "neuromusc fatigue"),
        ("tissue disorder", "tissue weakness"),
        ("neuromusc fatigue", "intra-game prop"),
        ("neuromusc fatigue", "injury"),
        ("tissue weakness", "injury"),
    ]
)

L_epi = ["team motivation", "previous injury"]
N_epi = [
    "team motivation",
    "previous injury",
    "warm-up",
    "coach",
    "fitness",
    "contact sport",
    "neuromusc fatigue",
    "tissue disorder",
    "injury",
]
treatment_epi = "warm-up"
outcome_epi = "injury"

EXAMPLES.append(CausalGraphExample(G_epi, treatment_epi, outcome_epi, L_epi, N_epi))

OPTIMALS.append(
    set(
        [
            "team motivation",
            "previous injury",
            "contact sport",
            "tissue disorder",
            "neuromusc fatigue",
        ]
    )
)
OPTIMALS_MINIMAL.append(
    set(["team motivation", "previous injury", "tissue disorder", "neuromusc fatigue"])
)
OPTIMALS_MINIMUM.append(set(["team motivation", "previous injury", "fitness"]))


# Figure 3 of the Biometrika paper

G_2 = CausalGraph()
G_2.add_edges_from(
    [("A", "M"), ("T", "A"), ("T", "F"), ("F", "A"), ("U", "F"), ("U", "Y"), ("M", "Y")]
)
L_2 = ["T"]
N_2 = ["A", "Y", "M", "T", "F"]
treatment_2 = "A"
outcome_2 = "Y"

EXAMPLES.append(CausalGraphExample(G_2, treatment_2, outcome_2, L_2, N_2))

OPTIMALS.append(set(["T", "F"]))
OPTIMALS_MINIMAL.append(set(["T", "F"]))
OPTIMALS_MINIMUM.append(set(["T", "F"]))

# Figure 4 of the Biometrika paper

G_3 = CausalGraph()
G_3.add_edges_from(
    [
        ("A", "Y"),
        ("T", "W1"),
        ("T", "Y"),
        ("W1", "A"),
        ("W2", "W1"),
        ("W2", "Y"),
        ("W3", "W1"),
        ("W3", "Y"),
        ("W4", "Y"),
    ]
)
L_3 = ["T"]
N_3 = ["A", "Y", "T", "W1", "W2", "W3", "W4"]
treatment_3 = "A"
outcome_3 = "Y"

EXAMPLES.append(CausalGraphExample(G_3, treatment_3, outcome_3, L_3, N_3))

OPTIMALS.append(set(["T", "W2", "W3", "W4"]))
OPTIMALS_MINIMAL.append(set(["T", "W2", "W3"]))
OPTIMALS_MINIMUM.append(set(["T", "W1"]))

# Figure 5 of the Biometrika paper

G_4 = CausalGraph()
G_4.add_edges_from([("A", "Y"), ("Z1", "A"), ("Z1", "Z2"), ("U", "Z2"), ("U", "Y")])
L_4 = []
N_4 = ["A", "Y", "Z1", "Z2"]
treatment_4 = "A"
outcome_4 = "Y"

EXAMPLES.append(CausalGraphExample(G_4, treatment_4, outcome_4, L_4, N_4))

OPTIMALS.append(
    "Conditions to guarantee the existence of an optimal adjustment set are not satisfied"
)
OPTIMALS_MINIMAL.append(set())
OPTIMALS_MINIMUM.append(set())

# Figure 6 of the Biometrika paper

G_5 = CausalGraph()
G_5.add_edges_from([("T", "A"), ("A", "Y"), ("U", "Y"), ("U", "F")])
L_5 = ["T"]
N_5 = ["A", "Y", "T", "F"]
treatment_5 = "A"
outcome_5 = "Y"

EXAMPLES.append(CausalGraphExample(G_5, treatment_5, outcome_5, L_5, N_5))

OPTIMALS.append(
    "Conditions to guarantee the existence of an optimal adjustment set are not satisfied"
)
OPTIMALS_MINIMAL.append(set("T"))
OPTIMALS_MINIMUM.append(set("T"))

# Figures 2 and 3 of optimal minimum cost paper

G_6 = CausalGraph()
costs_6 = [
    ("X", {"cost": 1}),
    ("B", {"cost": 2}),
    ("K", {"cost": 4}),
    ("Q", {"cost": 1}),
    ("R", {"cost": 1}),
    ("T", {"cost": 1}),
]
L_6 = ["X"]
N_6 = ["A", "Y", "X", "B", "K", "Q", "R", "M", "T", "F"]
treatment_6 = "A"
outcome_6 = "Y"
G_6.add_nodes_from(costs_6)
G_6.add_edges_from(
    [
        ("X", "A"),
        ("A", "M"),
        ("K", "A"),
        ("B", "K"),
        ("Q", "K"),
        ("B", "R"),
        ("Q", "T"),
        ("R", "Y"),
        ("M", "Y"),
        ("T", "Y"),
        ("U", "Y"),
        ("U", "F"),
    ]
)

EXAMPLES.append(CausalGraphExample(G_6, treatment_6, outcome_6, L_6, N_6))

OPTIMALS.append(
    "Conditions to guarantee the existence of an optimal adjustment set are not satisfied"
)
OPTIMALS_MINIMAL.append(set(["X", "T", "R"]))
OPTIMALS_MINIMUM.append(set(["X", "K"]))
OPTIMALS_MINCOST.append(set(["X", "T", "R"]))
