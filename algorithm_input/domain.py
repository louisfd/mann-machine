from global_utils.global_exceptions import AbstractClassException


class Domain:
    def __contains__(self):
        raise AbstractClassException

    def generate_randomly(self, length):
        raise AbstractClassException
