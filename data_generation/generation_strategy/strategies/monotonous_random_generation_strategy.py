from data_generation.generation_strategy.generation_strategy import GenerationStrategy


class MonotonousRandomGenerationStrategy(GenerationStrategy):
    def __init__(self, gen_range=range(10)):
        super().__init__()
        self.gen_range = gen_range

    def generate_from(self, language):
        words = [language.domain.generate_randomly(i) for i in self.gen_range]
        return [(word, word in language) for word in words]
