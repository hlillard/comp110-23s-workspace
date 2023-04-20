"""EX04 - `List` Utility Functions."""

__author__ = "730476613"


def all(list_num: list[int], num: int) -> bool:
    """Determine whether each element in list of ints is equal to given int."""
    idx: int = 0
    if len(list_num) == 0:
        return False
    while idx < len(list_num):
        if list_num[idx] != num:
            return False
        idx += 1
    else:
        return True


def max(input: list[int]) -> int:
    """Find max integer in given list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty sequence.")
    idx: int = 0
    current_max = input[0]
    while idx < len(input):
        if input[idx] > current_max:
            current_max = input[idx]
        idx += 1
    return current_max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """See if two lists have the same length."""
    if len(list1) != len(list2):
        return False
    if list1 == list2:
        return True
    else:
        return False