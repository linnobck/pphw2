from functional import count_all


def test_count_all_empty():
    assert count_all.count_all() == 0


def test_count_all_empty_inner():
    assert count_all.count_all(["a"], []) == 1


def test_count_all_basic():
    assert count_all.count_all(["a", "b", "c"], [1], [1, 2, 3]) == 7


def test_count_all_many():
    assert (
        count_all.count_all(
            [1, 2, 3, 4, 5],
            ["a", "b", "c", "d"],
            [(), (), (), ()],
            [None],
        )
        == 14
    )
