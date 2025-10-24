from functional import pipeline


def test_check_predicate_none():
    assert pipeline.check_predicates({"name": "a"}, []) is True


def test_check_predicate_one():
    assert (
        pipeline.check_predicates({"name": "a"}, [lambda d: d["name"] == "a"]) is True
    )
    assert (
        pipeline.check_predicates({"name": "a"}, [lambda d: d["name"] == "b"]) is False
    )


def test_check_predicate_many():
    predicates = [lambda d: d["name"] == "a", lambda d: d["age"] < 30]
    assert pipeline.check_predicates({"name": "a", "age": 99}, predicates) is False
    assert (
        pipeline.check_predicates(
            {"name": "b", "age": 9},
            [lambda d: d["name"] == "a", lambda d: d["age"] < 30],
        )
        is False
    )
    assert (
        pipeline.check_predicates(
            {"name": "a", "age": 9},
            [lambda d: d["name"] == "a", lambda d: d["age"] < 30],
        )
        is True
    )


def test_field_transform():
    assert pipeline.field_transform(
        {"name": "andy", "age": 55}, "name", lambda s: s.title()
    ) == {"name": "Andy", "age": 55}
    assert pipeline.field_transform(
        {"name": "andy", "age": 55}, "age", lambda s: s + 1
    ) == {"name": "andy", "age": 56}


def test_process_record():
    assert pipeline.process_record(
        {"name": "andy", "age": 55},
        [("name", lambda s: s.title()), ("age", lambda n: n + 1)],
    ) == {"name": "Andy", "age": 56}
