"""CQ04 - Dict Function Writing."""

__author__ = "730476613"

def zip(list1: list[str], list2: list[int]) -> dict[str, int]:
    new: dict[str, int] = {}
    idx: int = 0
    if len(list1) != len(list2) or len(list1) == 0 or len(list2) == 0:
        return new
    while idx < len(list1):
        new[list1[idx]] = list2[idx]
    return new
