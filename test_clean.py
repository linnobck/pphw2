from functional import pipeline
from functional.clean import filters, transforms

example_data = [
    {"name": "STEVEN", "age": "62", "title": "AUTHOR", "retired": False},
    {"name": "JODY", "age": "20", "title": "DRIVER", "retired": False},
    {"name": "HENRY", "age": None, "title": "UNKNOWN", "retired": False},
    {"name": "JIM", "age": "51", "title": "PAINTER", "retired": True},
    {"name": None, "age": "34", "title": "PROGRAMMER", "retired": False},
    {"name": "EDDIE", "age": "53", "title": "SCIENTIST", "retired": False},
    {"name": "JANE", "age": "77", "title": "CEO", "retired": True},
]

cleaned_data = [
    {"name": "steven", "age": 62, "title": "author", "retired": False},
    {"name": "jody", "age": 20, "title": "driver", "retired": False},
    {"name": "eddie", "age": 53, "title": "scientist", "retired": False},
]


def test_clean():
    assert pipeline.process_stream(example_data, filters, transforms) == cleaned_data
