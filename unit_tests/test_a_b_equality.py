from algorithm_input.languages.a_b_equality import ABEquality
from algorithm_input.domains.ab_domain import ABDomain
from algorithm_input.invalid_algorithm_input_exception import InvalidLanguageInputException
from global_utils.assert_utils import assert_except, assert_list

ab_equality = ABEquality(ABDomain())


def test_run_wrong_domain():
    assert_except(lambda: 'vwd' in ab_equality, InvalidLanguageInputException)


def test_positive():
    assert_list(lambda word: word in ab_equality,
                ['bababa', '', 'aaaaaaaaaaabbbbbbbbbbb', 'abba'],
                True)


def test_negative():
    assert_list(lambda word: word in ab_equality,
                ['a', 'b', 'ababbbba', 'aaaaaaaaaaa'],
                False)
