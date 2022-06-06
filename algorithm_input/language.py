from algorithm_input.invalid_algorithm_input_exception import InvalidLanguageInputException
from global_utils.global_exceptions import AbstractClassException


class Language:
    def __init__(self, domain):
        self.domain = domain

    def __contains__(self, x):
        self.validate_domain(x)
        return self._contains(x)

    def validate_domain(self, x):
        if x not in self.domain:
            raise InvalidLanguageInputException

    def _contains(self, x):
        raise AbstractClassException
