from optimaladj.CausalGraph import CausalGraph


class CausalGraphExample:
    def __init__(self, G, treatment, outcome, L, N):
        self.G = G
        self.treatment = treatment
        self.outcome = outcome
        self.L = L
        self.N = N


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
OPTIMALS_MINCOST.append(
    "An adjustment set formed by observable variables does not exist"
)

# Figure 1 of the Biometrika paper

G_epi = CausalGraph()
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
costs_epi = [(node, {"cost": 1}) for node in N_epi]
G_epi.add_nodes_from(costs_epi)
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
OPTIMALS_MINCOST.append(set(["team motivation", "previous injury", "fitness"]))


# Figure 3 of the Biometrika paper

G_2 = CausalGraph()
costs_2 = [
    ("T", {"cost": 1}),
    ("F", {"cost": 1}),
    ("M", {"cost": 1}),
]
G_2.add_nodes_from(costs_2)
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
OPTIMALS_MINCOST.append(set(["T", "F"]))
# Figure 4 of the Biometrika paper
G_3 = CausalGraph()
costs_3 = [
    ("T", {"cost": 1}),
    ("W1", {"cost": 1}),
    ("W2", {"cost": 1}),
    ("W3", {"cost": 1}),
    ("W4", {"cost": 1}),
]
G_3.add_nodes_from(costs_3)
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
OPTIMALS_MINCOST.append(set(["T", "W1"]))

# Figure 5 of the Biometrika paper

G_4 = CausalGraph()
costs_4 = [("Z1", {"cost": 1}), ("Z2", {"cost": 1})]
G_4.add_nodes_from(costs_4)
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
OPTIMALS_MINCOST.append(set())

# Figure 6 of the Biometrika paper

G_5 = CausalGraph()
costs_5 = [("T", {"cost": 1}), ("F", {"cost": 1})]
G_5.add_nodes_from(costs_5)
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
OPTIMALS_MINCOST.append(set(["T"]))

# Figures 1 and 2 of optimal minimum cost paper

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

# Figures 1 and 2 of optimal minimum cost paper modified

G_7 = CausalGraph()
costs_7 = [
    ("X", {"cost": 1}),
    ("B", {"cost": 1}),
    ("K", {"cost": 4}),
    ("Q", {"cost": 1}),
    ("R", {"cost": 2}),
    ("T", {"cost": 1}),
]
L_7 = ["X"]
N_7 = ["A", "Y", "X", "B", "K", "Q", "R", "M", "T", "F"]
treatment_7 = "A"
outcome_7 = "Y"
G_7.add_nodes_from(costs_7)
G_7.add_edges_from(
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

EXAMPLES.append(CausalGraphExample(G_7, treatment_7, outcome_7, L_7, N_7))

OPTIMALS.append(
    "Conditions to guarantee the existence of an optimal adjustment set are not satisfied"
)
OPTIMALS_MINIMAL.append(set(["X", "T", "R"]))
OPTIMALS_MINIMUM.append(set(["X", "K"]))
OPTIMALS_MINCOST.append(set(["X", "B", "T"]))

# Figure 3 of optimal minimum cost paper

G_8 = CausalGraph()
costs_8 = [
    ("B", {"cost": 1}),
    ("Q", {"cost": 1}),
    ("R", {"cost": 2}),
    ("T", {"cost": 2}),
]
L_8 = []
N_8 = ["A", "Y", "B", "Q", "R", "T"]
treatment_8 = "A"
outcome_8 = "Y"
G_8.add_nodes_from(costs_8)
G_8.add_edges_from(
    [
        ("B", "A"),
        ("B", "T"),
        ("Q", "A"),
        ("Q", "R"),
        ("A", "Y"),
        ("T", "Y"),
        ("R", "Y"),
    ]
)

EXAMPLES.append(CausalGraphExample(G_8, treatment_8, outcome_8, L_8, N_8))

OPTIMALS.append(set(["T", "R"]))
OPTIMALS_MINIMAL.append(set(["T", "R"]))
OPTIMALS_MINIMUM.append(set(["T", "R"]))
OPTIMALS_MINCOST.append(set(["B", "Q"]))

# All different example

G_9 = CausalGraph()
costs_9 = [
    ("W1", {"cost": 2}),
    ("W2", {"cost": 1}),
    ("W3", {"cost": 1}),
    ("W4", {"cost": 1}),
    ("W5", {"cost": 2}),
    ("W6", {"cost": 1}),
    ("W7", {"cost": 1}),
    ("W8", {"cost": 1}),
    ("W9", {"cost": 2}),
    ("K", {"cost": 11}),
    ("O", {"cost": 1}),
]
L_9 = []
N_9 = ["A", "Y", "K", "O", "W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8", "W9"]
treatment_9 = "A"
outcome_9 = "Y"
G_9.add_nodes_from(costs_9)
G_9.add_edges_from(
    [
        ("A", "Y"),
        ("K", "A"),
        ("W1", "K"),
        ("W2", "K"),
        ("W3", "K"),
        ("W1", "W4"),
        ("W2", "W5"),
        ("W3", "W6"),
        ("W4", "W7"),
        ("W5", "W8"),
        ("W6", "W9"),
        ("W7", "Y"),
        ("W8", "Y"),
        ("W9", "Y"),
        ("O", "Y"),
    ]
)

EXAMPLES.append(CausalGraphExample(G_9, treatment_9, outcome_9, L_9, N_9))

OPTIMALS.append(set(["O", "W7", "W8", "W9"]))
OPTIMALS_MINIMAL.append(set(["W7", "W8", "W9"]))
OPTIMALS_MINIMUM.append(set(["K"]))
OPTIMALS_MINCOST.append(set(["W7", "W8", "W6"]))

# Regression test for bug on name handling, spotted by Sara Taheri

G_10 = CausalGraph()
L_10 = []
N_10 = ["T", "Y", "M1", "M2", "Z1", "Z2", "Z3"]
costs_10 = [(node, {"cost": 1}) for node in N_10]
treatment_10 = "T"
outcome_10 = "Y"
G_10.add_nodes_from(costs_10)
G_10.add_edges_from(
    [
        ("Z1", "Z2"),
        ("Z1", "T"),
        ("Z2", "Z3"),
        ("Z3", "Y"),
        ("T", "M1"),
        ("M1", "M2"),
        ("M2", "Y"),
    ]
)

EXAMPLES.append(CausalGraphExample(G_10, treatment_10, outcome_10, L_10, N_10))

OPTIMALS.append(set(["Z3"]))
OPTIMALS_MINIMAL.append(set(["Z3"]))
OPTIMALS_MINIMUM.append(set(["Z3"]))
OPTIMALS_MINCOST.append(set(["Z3"]))

# Another regression test for bug on name handling, spotted by Sara Taheri

G_11 = CausalGraph()
L_11 = []
N_11 = ["T", "Y", "M1", "M2", "M3", "Z1", "Z2", "Z3", "Z4", "Z5"]
costs_11 = [(node, {"cost": 1}) for node in N_11]
treatment_11 = "T"
outcome_11 = "Y"
G_11.add_nodes_from(costs_11)
G_11.add_edges_from(
    [
        ("Z1", "Z2"),
        ("Z1", "T"),
        ("Z2", "Z3"),
        ("Z3", "Z4"),
        ("Z4", "Z5"),
        ("Z5", "Y"),
        ("T", "M1"),
        ("M1", "M2"),
        ("M2", "M3"),
        ("M3", "Y"),
        ("U1", "Z1"),
        ("U1", "T"),
        ("U2", "Z2"),
        ("U2", "M1"),
    ]
)

EXAMPLES.append(CausalGraphExample(G_11, treatment_11, outcome_11, L_11, N_11))

OPTIMALS.append(set(["Z1", "Z2", "Z5"]))
OPTIMALS_MINIMAL.append(set(["Z1"]))
OPTIMALS_MINIMUM.append(set(["Z1"]))
OPTIMALS_MINCOST.append(set(["Z1"]))
