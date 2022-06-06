"""
Should be independant from the domain and language
If it does not fit well with language then we should simply use another one.
"""
from global_utils.global_exceptions import AbstractClassException


class GenerationStrategy:
    def generate_from(self, language):
        raise AbstractClassException
