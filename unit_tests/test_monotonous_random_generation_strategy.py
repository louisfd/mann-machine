from unittest.mock import Mock

from data_generation.generation_strategy.strategies.monotonous_random_generation_strategy import \
    MonotonousRandomGenerationStrategy

A_WORD = "*"
A_MEMBERSHIP = True


def make_language():
    domain = Mock()
    domain.generate_randomly = Mock(return_value=A_WORD)
    language = Mock(domain=domain)
    language.__contains__ = Mock(return_value=A_MEMBERSHIP)
    return language


def test_generate_from():
    language = make_language()
    MRGS = MonotonousRandomGenerationStrategy(range(1))
    tuple = MRGS.generate_from(language)[0]
    assert tuple[0] == A_WORD and tuple[1] == A_MEMBERSHIP
