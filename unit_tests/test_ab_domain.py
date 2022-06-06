from algorithm_input.domains.ab_domain import ABDomain
from global_utils.assert_utils import assert_list

ab_domain = ABDomain()


def test_in_positive():
    assert_list(lambda word: word in ab_domain,
                ['a', 'b', 'ababbbba', 'bababa', '', 'aaaaaaaaaaa'],
                True)


def test_in_negative():
    assert_list(lambda word: word in ab_domain,
                ['w', 'ccc', 'abacabba', 'bab aba', 'ABABA'],
                False)


def test_generate_randomly():
    for i in range(20):
        random_word = ab_domain.generate_randomly(i)
        assert len(random_word) == i and random_word in ab_domain
