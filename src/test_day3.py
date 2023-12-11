import pytest

from .day3_p01 import day3


@pytest.mark.parametrize(['lines', 'expected'], [
    (['25$'], 25),
    (['12.%'], 0),
    (['1234%'], 1234),
])
def test_left(lines, expected):
    assert day3(lines) == expected


@pytest.mark.parametrize(['lines', 'expected'], [
    (['$25'], 25),
    (['%.12'], 0),
    (['%1234'], 1234),
])
def test_right(lines, expected):
    assert day3(lines) == expected


@pytest.mark.parametrize(['lines', 'expected'], [
    (['25$25'], 50),
    (['.23', '5$5'], 33),
    (['..3', '5$5'], 13),
    (['3.3', '5$5'], 16),
    (['3.3', '5$5', '100'], 116)
])
def test_both(lines, expected):
    assert day3(lines) == expected
