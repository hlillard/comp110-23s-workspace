"""Dictionary Function Practice."""

__author__ = "730476613"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Given a dictionary of strings, invert should return a dict[str, str] that inverts the keys and the values. The keys of the input list becomes the values of the output list and vice versa."""
    swap: dict[str, str] = {}
    for i in input:
        if input[i] in swap:
            raise KeyError("no duplicate names pls")
        swap[input[i]] = i
    return swap


def favorite_color(input: dict[str, str]) -> str:
    """Returns most popular color."""
    mostcolor: dict[str, int] = {}
    fave: str = ""
    most: int = 0
    for i in input:
        if input[i] not in mostcolor:
            mostcolor[input[i]] = 1
        else:
            mostcolor[input[i]] += 1
    for i in mostcolor:
        if mostcolor[i] > most:
            fave = i
            most = mostcolor[i]
    return fave


def count(input: list[str]) -> dict[str, int]:
    """Given a list, count how many times a thing is in that list."""
    count: dict[str, int] = {}
    for i in input:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count