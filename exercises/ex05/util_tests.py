"""Unit tests for utility functions."""

__author__ = "730476613"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat


def test_use1_only_evens() -> None:
    """First use test of only evens."""
    test_list: list[int] = [1, 2, 4]
    assert only_evens(test_list) == [2, 4]


def test_use2_only_evens() -> None:
    """Second use test of only evens."""
    test_list: list[int] = [6, 9, 12]
    assert only_evens(test_list) == [6, 12]


def test_edge_only_evens() -> None:
    """Edge test of only evens."""
    test_list: list[int] = []
    assert only_evens(test_list) == []


def test_use1_sub() -> None:
    """First use test of sub."""
    test_list: list[int] = [1, 2, 3]
    test_int1: int = 1
    test_int2: int = 3
    assert sub(test_list[test_int1], test_list[test_int2]) == [1, 3]


def test_use2_sub() -> None:
    """Second use test of sub."""
    test_list: list[int] = [4, 7, 9]
    test_int1: int = 7
    test_int2: int = 9
    assert sub(test_list[test_int1], test_list[test_int2]) == [7, 9]


def test_edge_sub() -> None:
    """Edge test of sub."""
    test_list: list[int] = []
    test_int1: int = ()
    test_int2: int = ()
    assert sub(test_list[test_int1], test_list[test_int2]) == []


def test_use1_concat() -> None:
    """First use test of concat."""
    test_list1: list[int] = [1, 2, 3]
    test_list2: list[int] = [4, 5, 6]
    assert concat(test_list1, test_list2) == [1, 2, 3, 4, 5, 6]


def test_use2_concat() -> None:
    """Second use test of concat."""
    test_list1: list[int] = [7, 8, 9]
    test_list2: list[int] = [10, 11, 12]
    assert concat(test_list1, test_list2) == [7, 8, 9, 10, 11, 12]


def test_edge_concat() -> None:
    """Edge test of concat."""
    test_list1: list[int] = []
    test_list2: list[int] = []
    assert concat(test_list1, test_list2) == []