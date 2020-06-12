import pytest

from aesthetically_pleasant.solution import number_of_ways_of_cutting_one_tree_aesthetically


@pytest.mark.parametrize("trees_height, number_of_ways_cut", [
    ([3, 4, 5, 3, 7], 3),
    ([1, 1, 2, 1, 2, 1], 2),
    ([5, 5, 2, 1, 2, 1], -1),
    ([5, 5, 2, 6, 5, 7], 2),
    ([5, 7, 2, 6, 5, 5], 2),
    ([5, 6, 2, 2, 6, 5, 7], 2),
    ([5, 6, 2, 2, 6, 5, 7, 2, 2], -1),
])
def test_is_number_of_ways_of_cutting_one_tree_aesthetically(trees_height, number_of_ways_cut):
    assert number_of_ways_of_cutting_one_tree_aesthetically(trees_height) == number_of_ways_cut
