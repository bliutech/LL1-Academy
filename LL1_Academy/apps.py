from django.apps import AppConfig

class Ll1AcademyConfig(AppConfig):
    name = 'LL1_Academy'

    def ready(self) -> None:
        try:
            from LL1_Academy.tools import SingleGrammarGenerator, MassGrammarGenerator
            from LL1_Academy.tools.SingleGrammarGenerator import SingleGrammarGenerator
            from LL1_Academy.tools.MassGrammarGenerator import MassGrammarGenerator
            import string, random

            def generate_grammar(nonTerminals, terminals):
                g = SingleGrammarGenerator()
                return g.generate(nonTerminals, terminals)

            def mass_generate_grammar(num, nonTerminals, terminals):
                mg = MassGrammarGenerator(num)
                mg.run(num, nonTerminals, terminals)

            # I found that the SVM is not entirely robust so I simplified the grammar generation
            potentialNonTerminals = list("AB")
            potentialTerminals = list("wxyz")

            num_grammars = 10
            for _ in range(num_grammars):
                nonTerminals = random.sample(potentialNonTerminals, 2)
                terminals = random.sample(potentialTerminals, random.randint(2, 4))
                mass_generate_grammar(2, nonTerminals, terminals)
            
            potentialNonTerminals = list("ABC")
            
            for _ in range(num_grammars):
                nonTerminals = random.sample(potentialNonTerminals, 3)
                terminals = random.sample(potentialTerminals, random.randint(2, 4))
                mass_generate_grammar(3, nonTerminals, terminals)

            return super().ready()
        except:
            return self.ready()
