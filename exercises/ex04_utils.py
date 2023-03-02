"""List Utility Functions."""

__author__ = "730476613"


def all(list: list[int], int) -> bool:
    """Determine whether each element in list of ints is equal to given int."""
    if not list:
        return False
    while list:
        x = list.pop()
        if x != int:
            return False
    return True


def max(input: list[int]) -> int:
    """Find max integer in given list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty sequence")
    current_max = input[0]
    for int in range(1, len(input)):
        if input[int] > current_max:
            current_max = input[int]
    return current_max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Do 2 lists have the same length?""""
    if len(list1) != len(list2):
        return False
    for int in range(len(list1)):
        if list1[int] != list1[int]:
            return False
    return True