import torch

from data_generation.tensor_converter import TensorConverter

tensor_converter = TensorConverter()


def test_memberships_to_tensor():
    memberships = [True, False, False, False]
    tensor = tensor_converter.memberships_to_tensor(memberships)
    assert torch.equal(tensor, torch.tensor([1., -1., -1., -1.], dtype=torch.float64))
