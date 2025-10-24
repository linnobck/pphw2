from functional import count_all
import pytest


@pytest.mark.parametrize(
    "obj,expected",
    [
        ("", 0),
        ([], 0),
        ("a", 1),
        (["abc"], 1),
        (["a", "b"], 2),
        (range(10), 10),
    ],
)
def test_newlen(obj, expected):
    assert count_all.newlen(obj) == expected
