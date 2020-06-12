# you can write to stdout for debugging purposes, e.g.

MIN_LEN_A = 4
MAX_LEN_A = 200

def is_aesthetically_correct(A, len_A):
    """This method checks if the height of the consecutive trees
       are aesthtetically correct. What is aestathically correct:
         1. Two adjacent trees cannot have equal heights
         2. The trees alternately increase and decrease:
            a. ...shorter, taller, shorter..
            a. ...taller, shorter, taller..

    Args:
        A (list): list of the height of the trees.
        len_A (int): Length of list A.  4 <= len_A <= 200.

    Returns:
        bool: True is is aesthetically pleasing, False otherwise.

    """

    if len_A < MIN_LEN_A or len_A > MAX_LEN_A:
        return False

    start_taller = True if A[0] > A[1] else False
    for i in range(1, len_A - 1):
        if start_taller:
            if A[i - 1] > A[i] and A[i] < A[i + 1]:
                start_taller = False
                continue
            else:
                return False
        else:
            if A[i - 1] < A[i] and A[i] > A[i+1]:
                start_taller = True
                continue
            else:
                return False
    return True

def number_of_ways_of_cutting_one_tree_aesthetically(A):
    """This method returns the number of ways of cutting out one tree,
       to that the remaining trees are already aesthetically pleasing.

    Args:
        A (list): list of the height of the trees.

    Returns:
        int: -1 if there is no way to cut one tree to that remainging trees
             are aesthetically pleasing. >= 1 if there ways to cut one tree to
             that remainging trees are aesthetically pleasing.

    """

    _A = list(A)
    _count = 0
    for i, tree in enumerate(A):
        height = _A.pop(i)
        if is_aesthetically_correct(_A, len_A=len(_A)):
            _count = _count + 1
        _A.insert(i, height)
    if _count == 0:
        return -1
    return _count

def solution(A):
    """CHANGELOG:

       ## Changed - 12-06-2020

        - In number_of_ways_of_cutting_one_tree_aesthetically method
          changed _ A = list(A) to _A.insert(i, height). There is no need to copy all the list.

        - In number_of_ways_of_cutting_one_tree_aesthetically method
          moved _A.insert(i, height) out of "if is_aesthetically_correct" condition,
          because if it is not a aesthetically correct we lose a height for the next iteration.

        - In number_of_ways_of_cutting_one_tree_aesthetically method changed _A(A copy) for A
          in the main for loop to iterate on full set of A instead of _A, that is a subset of A.

        - Minor changes:
            - Use constants for A max min lenth.
            - Pass len(A) as a paremeter for is_aesthetically_correct method.

        - Added more tests:
          [3, 4, 5, 3, 7]
          [1, 1, 2, 1, 2, 1]
          [5, 5, 2, 1, 2, 1]
          [5, 5, 2, 6, 5, 7]
          [5, 7, 2, 6, 5, 5]
          [5, 6, 2, 2, 6, 5, 7]
          [5, 6, 2, 2, 6, 5, 7, 2, 2]
          [1, 2, 1, 2, 1, 2]
          [2, 1, 2, 1, 2, 1, 2]
          [3, 4, 3]
          [1, 1, 3, 1, 2]
          [1, 1, 1, 3, 1, 2]
          [1, 3, 1, 2, 2]
          [1, 3, 1, 2, 2, 2]
          [1, 3, 3, 3, 1, 2]
          [1, 2, 3, 1, 2]
          [5, 4, 3, 2, 1]

    """

    len_A = len(A)
    if len_A < MIN_LEN_A or len_A > MAX_LEN_A:
        return -1
    if is_aesthetically_correct(A, len_A):
        return 0
    possible_trees_to_cut = number_of_ways_of_cutting_one_tree_aesthetically(A)
    return possible_trees_to_cut
