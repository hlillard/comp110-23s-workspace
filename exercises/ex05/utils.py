"""EX05 - `list` Utility Functions."""

__author__ = "730476613"


def only_evens(int_list: list[int]) -> list():
    """Given a list of ints, only_evens should return a new list containing only the elements of the input list that were even."""
    evens: list[int] = list()
    for num in int_list:
        if num % 2 == 0:
            evens.append(num)
    return evens


def concat(list1: list[int], list2: list[int]) -> list:
    """Given two Lists of ints, concat should generate a new List which contains all of the elements of the first list followed by all of the elements of the second list."""
    lists: list[int] = list()
    for num in list1:
        lists.append(num)
    for num in list2:
        lists.append(num)
    return lists


def sub(sublist: list[int], start: int, end: int) -> list:
    """Given a list of ints, a start index, and an end index (not inclusive), sub should generate a List which is a subset of the given list, between the specified start index and the end index - 1."""
    subsets: list[int] = list()
    if start < 0:
        start = 0
    if end > len(subsets):
        end = len(subsets)
    for num in range(start, end):
        subsets.append(subsets[num])
    return subsets
 