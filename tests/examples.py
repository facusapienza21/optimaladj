from optimal_adjustment.CausalGraph import CausalGraph


class CausalGraphExample():
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

# Example 1, Figure 3 of the paper

G_1 = CausalGraph()
G_1.add_edges_from([('A', 'M'),
                    ('T', 'A'),
                    ('T', 'F'),
                    ('F', 'A'),
                    ('U', 'F'),
                    ('U', 'Y'),
                    ('M', 'Y')])
L_1 = ['T']
N_1 = ['A', 'Y', 'M', 'T', 'F']
treatment_1 = 'A'
outcome_1 = 'Y'

EXAMPLES.append(CausalGraphExample(G_1, treatment_1, outcome_1, L_1, N_1))

OPTIMALS.append(set(['T', 'F']))
OPTIMALS_MINIMAL.append(set(['T', 'F']))
OPTIMALS_MINIMUM.append(set(['T', 'F']))

# Example 2, Figure 4 of the paper

G_2 = CausalGraph()
G_2.add_edges_from([('A', 'Y'),
                    ('T', 'W1'),
                    ('T', 'Y'),
                    ('W1', 'A'),
                    ('W2', 'W1'),
                    ('W2', 'Y'),
                    ('W3', 'W1'),
                    ('W3', 'Y'),
                    ('W4', 'Y')])
L_2 = ['T']
N_2 = ['A', 'Y', 'T', 'W1', 'W2', 'W3', 'W4']
treatment_2 = 'A'
outcome_2 = 'Y'

EXAMPLES.append(CausalGraphExample(G_2, treatment_2, outcome_2, L_2, N_2))

OPTIMALS.append(set(['T', 'W2', 'W3', 'W4']))
OPTIMALS_MINIMAL.append(set(['T', 'W2', 'W3']))
OPTIMALS_MINIMUM.append(set(['T', 'W1']))

# Example 4, Figure 5 of the paper

G_3 = CausalGraph()
G_3.add_edges_from([('A', 'Y'),
                    ('Z1', 'A'),
                    ('Z1', 'Z2'),
                    ('U', 'Z2'),
                    ('U', 'Y')])
L_3 = []
N_3 = ['A', 'Y', 'Z1', 'Z2']
treatment_3 = 'A'
outcome_3 = 'Y'

EXAMPLES.append(CausalGraphExample(G_3, treatment_3, outcome_3, L_3, N_3))

OPTIMALS.append("Conditions to guarantee the existence of an optimal adjustment set are not satisfied")
OPTIMALS_MINIMAL.append(set())
OPTIMALS_MINIMUM.append(set())
