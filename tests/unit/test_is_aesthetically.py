import pytest

from aesthetically_pleasant.solution import is_aesthetically_correct

@pytest.mark.parametrize("trees_height, len_A", [
    ([1, 3, 1, 2], 4),
    ([1, 3, 1, 2, 1, 3, 1, 2], 8),
    ([1, 2, 1, 2, 1, 2], 6),
    ([2, 1, 2, 1, 2, 1, 2], 7),
    ([2, 1, 2, 1, 2, 1], 6),
])
def test_is_asthetically_correct(trees_height, len_A):
    assert is_aesthetically_correct(trees_height, len_A) == True


@pytest.mark.parametrize("trees_height, len_A", [
    ([1, 1, 3, 1, 2], 5),
    ([1, 1, 1, 3, 1, 2], 6),
    ([1, 3, 1, 2, 2], 5),
    ([1, 3, 1, 2, 2, 2], 6),
    ([1, 3, 3, 3, 1, 2], 7),
    ([1, 2, 3, 1, 2], 5),
    ([5, 4, 3, 2, 1], 5),
    ([3, 4, 3], -1),
])
def test_is_asthetically_incorrect(trees_height, len_A):
    assert is_aesthetically_correct(trees_height, len_A) == False
