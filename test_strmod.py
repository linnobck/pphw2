from functional import strmod


def test_strmod_concat():
    assert strmod.strmod("+", "abc", "def") == "abcdef"


def test_strmod_replace_one():
    assert strmod.strmod("-", "apple", "pp") == "ale"


def test_strmod_replace_multiple():
    assert strmod.strmod("-", "bananana", "na") == "ba"


def test_strmod_scramble():
    assert strmod.strmod("@", "cat", "dog") == "acdgot"


def test_strmod_scramble_repeat():
    assert strmod.strmod("@", "aba", "bab") == "aaabbb"
