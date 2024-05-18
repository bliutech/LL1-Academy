"""
Checking out the LL1_Academy grammar generation libraries
"""

from LL1_Academy.tools.SingleGrammarGenerator import SingleGrammarGenerator
from LL1_Academy.tools.GrammarChecker import GrammarChecker
import string, random


def generate_grammar(nonTerminals, terminals):
    g = SingleGrammarGenerator()
    return g.generate(nonTerminals, terminals)


potentialNonTerminals = list(string.ascii_uppercase)
potentialTerminals = list(string.ascii_lowercase)

potentialNonTerminals = list("AB")
potentialTerminals = list("wxyz")

num_grammars = 100
for i in range(num_grammars):
    nonTerminals = random.sample(potentialNonTerminals, 2)
    print(nonTerminals)
    terminals = random.sample(potentialTerminals, random.randint(2, 4))
    print(terminals)
    g = generate_grammar(nonTerminals, terminals)
    gc = GrammarChecker()
    firstSets, followSets, parsingTable, status, reachable, terminals = gc.solve(g, "A", False)
    print("Start symbol:", nonTerminals[0])
    print("First sets:", firstSets)
    filteredFirstSets = {}
    for key, value in firstSets.items():
        filteredFirstSets[key] = [x for x in value if x in terminals]
    print("First sets (filtered):", filteredFirstSets)
    print("Follow sets:", followSets)
    filteredFollowSet = {}
    for key, value in followSets.items():
        filteredFollowSet[key] = [x for x in value if x in terminals]
    print("Follow sets (filtered):", filteredFollowSet)
    print("Parsing table:", parsingTable)
    print("Is LL(1):", "yes" if status == 0 else "no" if status == 1 else "left recursion")
    print("Reachable:", reachable)
    print("Terminals:", terminals)
    print("Grammar:", g)
    breakpoint()
