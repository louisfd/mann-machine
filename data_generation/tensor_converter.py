import torch

from global_utils.global_exceptions import TODOException


class TensorConverter:

    def word_membership_to_tensors(self, word_memberships):
        words, memberships = tuple(map(list, list(zip(*word_memberships))))
        return self.words_to_tensor(words), self.memberships_to_tensor(memberships)

    def words_to_tensor(self, words):
        raise TODOException

    def memberships_to_tensor(self, memberships):
        return 2 * torch.tensor(memberships, dtype=torch.float64) - 1


if __name__ == '__main__':
    tc = TensorConverter()
    print(tc.memberships_to_tensor([True, False]))
