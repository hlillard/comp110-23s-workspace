"""Dictionary Function Practice Test File."""

__author__ = "730476613"


from exercises.ex07.dictionary import invert
from exercises.ex07.dictionary import favorite_color
from exercises.ex07.dictionary import count


def test_use1_invert() -> None:
    """First use test of invert."""
    assert invert({'a': 'z', 'b': 'y'}) == {'z': 'a', 'y': 'b'}


def test_use2_invert() -> None:
    """Second use test of invert."""
    assert invert({'c': 'm', 'r': 't'}) == {'m': 'c', 't': 'r'}


def test_edge_invert() -> None:
    """Edge test of invert."""
    assert invert({}) == {}


def test_use1_favorite_color() -> None:
    """First use test of favorite_color."""
    assert favorite_color({'Katniss': 'green', 'Peeta': 'orange', 'Haymitch': 'green'}) == {'green'}


def test_use2_favorite_color() -> None:
    """Second use test of favorite_color."""
    assert favorite_color({'Finnick': 'blue', 'Mags': 'blue', 'Johannah': 'brown'}) == {'blue'}


def test_edge_favorite_color() -> None:
    """Edge test of favorite_color."""
    assert favorite_color({}) == {}


def test_use1_count() -> None:
    """First use test of count."""
    assert count({'bow', 'bow', 'trident'}) == {'bow': 2, 'trident': 1}


def test_use2_count() -> None:
    """Second use test of count."""
    assert count({'soup', 'ax', 'teeth'}) == {'soup': 1, 'ax': 1, 'teeth': 1}


def test_edge_count() -> None:
    """Edge test of count."""
    assert count({}) == {}