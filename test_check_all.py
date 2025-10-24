from functional import exclude


def test_check_all_basic():
    funcs = [lambda x: x > 10, lambda y: y < 100]
    assert exclude.check_all([1, 20, 200], funcs) == [
        (1, [False, True]),
        (20, [True, True]),
        (200, [True, False]),
    ]


def test_check_all_empty_vals():
    funcs = [lambda x: x > 10, lambda y: y < 100]
    assert exclude.check_all([], funcs) == []


def test_check_all_empty_funcs():
    funcs = []
    assert exclude.check_all([1, 2, 3], funcs) == [
        (1, []),
        (2, []),
        (3, []),
    ]


def test_check_all_many_funcs():
    funcs = [lambda x: True, lambda x: False, lambda x: x == 1, lambda x: x != 2]
    assert exclude.check_all([1, 2, 3], funcs) == [
        (1, [True, False, True, True]),
        (2, [True, False, False, False]),
        (3, [True, False, False, True]),
    ]
