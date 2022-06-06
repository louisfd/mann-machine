from algorithm_input.domain import Domain


class ABDomain(Domain):
    def __contains__(self, x):
        return all(c in ('a', 'b') for c in x)
