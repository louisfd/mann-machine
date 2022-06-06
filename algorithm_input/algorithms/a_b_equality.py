from algorithm_input.boolean_algorithm import BooleanAlgorithm


class ABEquality(BooleanAlgorithm):
    def _run(self, x):
        return sum([1 if c == 'a' else -1 for c in x]) == 0


print(ABEquality(['ababab']).run('ababab'))
