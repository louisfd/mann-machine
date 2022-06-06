from algorithm_input.domains.ab_domain import ABDomain
from unit_tests.assert_utils import assert_list

ab_domain = ABDomain()


def test_positive():
    assert_list(lambda word: word in ab_domain,
                ['a', 'b', 'ababbbba', 'bababa', '', 'aaaaaaaaaaa'],
                True)


def test_negative():
    assert_list(lambda word: word in ab_domain,
                ['w', 'ccc', 'abacabba', 'bab aba', 'ABABA'],
                False)
