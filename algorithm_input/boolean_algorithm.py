from algorithm_input.invalid_algorithm_input_exception import InvalidAlgorithmInputException


class BooleanAlgorithm:
    def __init__(self, domain):
        self.domain = domain

    def run(self, x):
        self.validate_domain(x)
        return self._run(x)

    def validate_domain(self, x):
        if x not in self.domain:
            raise InvalidAlgorithmInputException

    def _run(self, x):
        raise NotImplementedError("Sub-classes must implement this method")
