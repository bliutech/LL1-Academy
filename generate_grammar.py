"""
Checking out the LL1_Academy grammar generation libraries
"""

from LL1_Academy.tools.SingleGrammarGenerator import SingleGrammarGenerator
from LL1_Academy.tools.MassGrammarGenerator import MassGrammarGenerator
import string, random

def generate_grammar(nonTerminals, terminals):
    g = SingleGrammarGenerator()
    return g.generate(nonTerminals, terminals)

def mass_generate_grammar(num, nonTerminals, terminals):
    mg = MassGrammarGenerator(num)
    mg.run(num, nonTerminals, terminals)


potentialNonTerminals = list(string.ascii_uppercase)
potentialTerminals = list(string.ascii_lowercase) + ['(', ')', '+', '*']

num_grammars = 100
for i in range(num_grammars):
    nonTerminals = random.sample(potentialNonTerminals, 2)
    print(nonTerminals)
    terminals = random.sample(potentialTerminals, random.randint(2, 4))
    print(terminals)
    mass_generate_grammar(2, nonTerminals, terminals)
