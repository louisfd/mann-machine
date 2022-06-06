from algorithm_input.algorithms.a_b_equality import ABEquality
from algorithm_input.domains.ab_domain import ABDomain
from algorithm_input.invalid_algorithm_input_exception import InvalidAlgorithmInputException
from unit_tests.assert_utils import assert_except, assert_list

ab_equality = ABEquality(ABDomain())


def test_run_wrong_domain():
    assert_except(lambda: ab_equality.run('vwd'), InvalidAlgorithmInputException)


def test_positive():
    assert_list(lambda word: ab_equality.run(word),
                ['bababa', '', 'aaaaaaaaaaabbbbbbbbbbb', 'abba'],
                True)


def test_negative():
    assert_list(lambda word: ab_equality.run(word),
                ['a', 'b', 'ababbbba', 'aaaaaaaaaaa'],
                False)
