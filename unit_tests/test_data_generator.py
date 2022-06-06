"""
    def input_outputs_to_tensor(self, input_output_pairs):
        X_, y_ = tuple(map(list, list(zip(*input_output_pairs))))
        print(X_)
        print(y_)
"""
from unittest.mock import Mock

import torch

from algorithm_input.domains.ab_domain import ABDomain
from algorithm_input.languages.a_b_equality import ABEquality
from data_generation.data_generator import DataGenerator
from data_generation.generation_strategy.strategies.monotonous_random_generation_strategy import \
    MonotonousRandomGenerationStrategy

# def generate(self):
#     word_membership = self.generation_strategy.generate_from(self.language)
#     return self.tensor_converter.word_membership_to_tensors(word_membership)
from global_utils.assert_utils import return_if

DATA_TENSOR = torch.tensor([1, 2, 3])
LABEL_TENSOR = torch.tensor([4, 5, 6])
WORD_MEMBERSHIP = [("a", True), ("b", False)]


def make_data_generator():
    language, generation_strategy, tensor_converter = Mock(), Mock(), Mock()
    generation_strategy.generate_from = Mock(side_effect=return_if(language, WORD_MEMBERSHIP))
    tensor_converter.word_membership_to_tensors = Mock(
        side_effect=return_if(WORD_MEMBERSHIP, (DATA_TENSOR, LABEL_TENSOR)))
    return DataGenerator(language, generation_strategy, tensor_converter)


def test_generate():
    dg = make_data_generator()
    X, y = dg.generate()
    assert torch.equal(X, DATA_TENSOR)
    assert torch.equal(y, LABEL_TENSOR)
