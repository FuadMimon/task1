import pytest

from aesthetically_pleasant.solution import solution

@pytest.mark.parametrize("trees_height, expected_cuts", [
    ([1, 2, 1, 2, 1, 2], 0),
    ([2, 1, 2, 1, 2, 1, 2], 0),
    ([5, 5, 2, 1, 2, 1], -1),
    ([3, 4, 5, 3, 7], 3),
    ([1, 1, 2, 1, 2, 1], 2),
    ([3, 4, 3], -1),
    ([5, 5, 2, 6, 5, 7], 2),
    ([5, 7, 2, 6, 5, 5], 2),
    ([5, 6, 2, 2, 6, 5, 7], 2),
    ([5, 6, 2, 2, 6, 5, 7, 2, 2], -1),
    ([1, 1, 3, 1, 2], 2),
    ([1, 1, 1, 3, 1, 2], -1),
    ([1, 3, 1, 2, 2], 2),
    ([1, 3, 1, 2, 2, 2], -1),#quitar
    ([1, 3, 3, 3, 1, 2], -1),
    ([1, 2, 3, 1, 2], 3),
    ([5, 4, 3, 2, 1], -1),
    ([7, 5, 5, 1, 2, 1], -1)
])
def test_solution(trees_height, expected_cuts):
    assert solution(trees_height) == expected_cuts
