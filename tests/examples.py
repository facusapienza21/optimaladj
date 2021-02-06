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

# Figure 1 of the paper

G_epi = CausalGraph()
G_epi.add_edges_from([('coach', 'team motivation'),
                  ('coach', 'fitness'),
                  ('fitness', 'pre-game prop'),
                  ('fitness', 'neuromusc fatigue'),
                  ('team motivation', 'warm-up'),
                  ('team motivation', 'previous injury'),
                  ('pre-game prop', 'warm-up'),
                  ('warm-up', 'intra-game prop'),
                  ('contact sport', 'previous injury'),
                  ('contact sport', 'intra-game prop'),
                  ('intra-game prop', 'injury'),
                  ('genetics', 'fitness'),
                  ('genetics', 'neuromusc fatigue'),
                  ('genetics', 'tissue disorder'),
                  ('tissue disorder', 'neuromusc fatigue'),
                  ('tissue disorder', 'tissue weakness'),
                  ('neuromusc fatigue', 'intra-game prop'),
                  ('neuromusc fatigue', 'injury'),
                  ('tissue weakness', 'injury')])

L_epi = ['team motivation', 'previous injury']
N_epi = ['team motivation', 'previous injury', 'warm-up', 'coach', 'fitness',
     'contact sport', 'neuromusc fatigue', 'tissue disorder', 'injury']
treatment_epi = 'warm-up'
outcome_epi = 'injury'

EXAMPLES.append(CausalGraphExample(G_epi, treatment_epi, outcome_epi, L_epi, N_epi))

OPTIMALS.append(set(['team motivation', 'previous injury', 'contact sport',
                     'tissue disorder', 'neuromusc fatigue']))
OPTIMALS_MINIMAL.append(set(['team motivation', 'previous injury', 'tissue disorder', 'neuromusc fatigue']))
OPTIMALS_MINIMUM.append(set(['team motivation', 'previous injury', 'fitness']))


# Figure 3 of the paper

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

# Figure 4 of the paper

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

# Figure 5 of the paper

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

# Figure 6 of the paper

G_4 = CausalGraph()
G_4.add_edges_from([('T', 'A'),
                    ('A', 'Y'),
                    ('U', 'Y'),
                    ('U', 'F')])
L_4 = ['T']
N_4 = ['A', 'Y', 'T', 'F']
treatment_4 = 'A'
outcome_4 = 'Y'

EXAMPLES.append(CausalGraphExample(G_4, treatment_4, outcome_4, L_4, N_4))

OPTIMALS.append("Conditions to guarantee the existence of an optimal adjustment set are not satisfied")
OPTIMALS_MINIMAL.append(set('T'))
OPTIMALS_MINIMUM.append(set('T'))

# Example with no observable adjustment set
G_5 = CausalGraph()
G_5.add_edges_from([('A', 'Y'),
                    ('U', 'Y'),
                    ('U', 'A')])
L_5 = []
N_5 = ['A', 'Y']
treatment_5 = 'A'
outcome_5 = 'Y'

EXAMPLES.append(CausalGraphExample(G_5, treatment_5, outcome_5, L_5, N_5))

OPTIMALS.append("An adjustment set formed by observable variables does not exist")
OPTIMALS_MINIMAL.append("An adjustment set formed by observable variables does not exist")
OPTIMALS_MINIMUM.append("An adjustment set formed by observable variables does not exist")
