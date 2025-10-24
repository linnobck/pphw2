from functional import exclude # type: ignore


def test_exclude_empty():
    assert exclude.exclude([], lambda x: x > 10) == []


def test_exclude_basic1():
    assert exclude.exclude([2], lambda x: x > 10) == [2]


def test_exclude_basic_few():
    assert exclude.exclude([1, 20, 100], lambda x: x < 10) == [20, 100]


def test_exclude_indivisible():
    assert exclude.exclude(range(10), lambda x: x % 2 == 1) == [0, 2, 4, 6, 8]
