from functional import pipeline

# DO NOT MODIFY
example_data = [
    {"name": "STEVEN", "age": "62", "title": "AUTHOR", "retired": False},
    {"name": "JODY", "age": "20", "title": "DRIVER", "retired": False},
    {"name": "JIM", "age": "51", "title": "PAINTER", "retired": True},
    {"name": "EDDIE", "age": "53", "title": "SCIENTIST", "retired": False},
    {"name": "JANE", "age": "77", "title": "CEO", "retired": True},
    {"name": None, "age": "34", "title": "PROGRAMMER", "retired": False},
    {"name": "HENRY", "age": None, "title": "UNKNOWN", "retired": False},
]

# MODIFY THESE LISTS (you may create helper functions too)
transforms = [("name", lambda s: s.lower()),
    ("title", lambda s: s.lower()),
    ("age", lambda s: int(s))]

filters = [lambda r: not r["retired"],
    lambda r: r["name"] is not None,
    lambda r: r["title"] is not None,
    lambda r: r["age"] is not None]


def main():
    # do not modify, this function runs your data pipeline and prints the results
    for record in pipeline.process_stream(example_data, filters, transforms):
        print(record)


if __name__ == "__main__":
    main()
