from algorithm_input.language import Language


class ABEquality(Language):
    def _contains(self, x):
        return sum([1 if c == 'a' else -1 for c in x]) == 0
