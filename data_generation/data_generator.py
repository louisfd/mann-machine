class DataGenerator:
    def __init__(self, language, generation_strategy, tensor_converter):
        self.language = language
        self.generation_strategy = generation_strategy
        self.tensor_converter = tensor_converter

    def generate(self):
        word_membership = self.generation_strategy.generate_from(self.language)
        return self.tensor_converter.word_membership_to_tensors(word_membership)
