[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/NercpauI)
# Programming Assignment 2

The purpose of this assignment is to practice functional programming.

As a result, there are special restrictions in place for this assignment.

You may not (unless otherwise stated) use:

- `while` or `match` statements
- `for` or `if` *statements* (comprehensions are allowed)
- the `len` function
- the `in` operator (`x in y`)
- sequence methods like `list.append`, etc.
- repetition via `sequence * int`
- global variables
- the ternary operator syntax `X if Y else Z`
- the `match` statement
- `max(), min(), sum(), all(), any()`
- any `import` statements other than `functools` and `operator` (no `pandas`, `itertools`, etc.)

You may (unless otherwise stated) use:

- comprehensions of any type
- helper functions, but they too must obey these restrictions
- `functools.reduce`
    - https://docs.python.org/3/library/functools.html#functools.reduce
    - https://realpython.com/python-reduce-function/
- `functools.partial`
    - https://docs.python.org/3/library/functools.html#functools.partial
    - https://www.learnpython.org/en/Partial_functions
- All other builtin functions like `map`, `filter`, `range`, `tuple`, `bool`, `list` are allowed. (`list(...)` can be useful to convert the result of a map/filter into a `list`.)
- Unpacking syntax like `a, b = (1, 2)`.

If in doubt about a function or language feature, you should ask on Ed and we will gladly clarify for everyone.

Please take special care to follow these instructions, use of a disallowed function or construct will result in significant deductions.

**You will also notice that we have not provided doc strings for these functions, you should add your own.**


## Part 1 - `exclude` & `check_all`

In `functional/exclude.py` create a function named `exclude` that takes in an iterable `items` and a predicate function (`exclude_if`).

If the predicate function returns `True`, the value should be excluded, and vice-versa.

The function should return a list of items where the predicate function returned `False`.

Examples:

```python
>>> from functional.exclude import exclude

>>> exclude([1, 20, 200], lambda x: x > 10)
[1]

>>> exclude([0, 1, 2, 3], lambda x: x == 0)
[1, 2, 3]

>>> exclude([], lambda x: x > 0)
[]

>>> exclude([1, 2, 3], lambda x: True)
[]
```

Test with `uv run pytest functional/tests/test_exclude.py`.

The second function you'll write,
`check_all` takes an iterable (`values`) and a list of predicates (`funcs`).

The function should return a list of two-element tuples.
The first component being an integer from `values` and the second is a list of the return values from calling each predicate function with the integer.

```python
>>> from functional.exclude import check_all
>>> funcs = [lambda x: x > 10, lambda y: y < 100]

>>> check_all([1, 20, 200], funcs)
[(1, [False, True]), (20, [True, True]), (200, [True, False])]

>>> check_all([], funcs)
[]

>>> funcs = [lambda x: x > 10, lambda y: y < 100, lambda z: False]
>>> check_all([1, 20, 200], funcs)
[(1, [False, True, False]), (20, [True, True, False]), (200, [True, False, False])]
```

Test with `uv run pytest functional/tests/test_check_all.py`.

## Part 2 - `strmod`

In `functional/strmod.py`, complete a function `strmod` (string modify) which takes three parameters:

- `mod` - modification to make:
    - '+' - combines the two strings via concatenation
    - '-' - removes any occurrences of `str2` from `str1`
    - '@' - combines the two strings, and then sorts their letters alphabetically
- `str1` - first string parameter
- `str2` - second string parameter

Examples:
```python
>>> from functional.strmod import strmod
>>> strmod("+", "abc", "def")     # concatenation
"abcdef"
>>> strmod("-", "banana", "na")   # remove/replace all "na"
"ba"
>>> strmod("-", "banana", "x")    # nothing to remove
"banana"
>>> strmod("@", "cat", "dog")     # combined then sorted
"acdgot"

```

You must implement this part **without writing helper functions**; use `lambda` instead.

Test with `uv run pytest functional/tests/test_strmod.py`.

## Part 3 - `newlen` & `count_all`

For this part, you will complete these two functions in `functional/count_all.py`

Remember, you are not allowed to use `len` for this assignment.

If you were allowed to use for loops you could work around this by writing:

```python
def newlen(iterable):
    count = 0
    for _ in iterable:
        count += 1
    return count
```

But this is off-limits too, so for the first part of this problem instead write your own version using `functools.reduce`.

Write a function, `newlen`, which takes an iterable and returns its length, an integer.

Your `newlen` function's output should match `len`.

You can test with `uv run pytest functional/tests/test_newlen.py`.

Next, implement a `count_all` function that takes in any number of lists and returns the total count of objects inside the lists.

```python
>>> from functional.count_all import count_all

>>> count_all([1, 2, 3], ["a"], [3, 4, 5])
7
>>> count_all()
0
>>> count_all([], [])
0
>>> count_all([1], [], [3])
2
```
You can test with `uv run pytest functional/tests/test_count_all.py`.

## Part 4 - Pipeline

Functional programming can play a useful role in data pipelines.
By chaining functions together we can build complicated pipelines out of small, performant, and testable pieces of code.

For this assignment we will be implementing a rudimentary data pipeline system.


To do so, implement the following functions in `functional/pipeline.py`:

### `check_predicates(record, predicates)`

- `record` - dict - A dictionary with arbitrary data.
- `predicates` - list of functions - Each predicate function takes a single dictionary, and returns `True` or `False`.

`check_predicates` should return `True` if all predicate functions return `True` when called with the given record, and `False` otherwise.

```
>>> check_predicates({"name": "ash", "age": 13}, [lambda r: r["age"] > 18])
False
>>> check_predicates({"name": "sarah", "age": 32}, [lambda r: r["age"] > 18, lambda r: r["name"].startswith("s")])
True
```

### `field_transform(record, field, transform)`

- `record` - dict - A dictionary with arbitrary data.
- `field` - str - Name of a field in `item`.
- `transform` - function - A function that takes a single parameter and returns a modified value.

Return an updated dictionary, the result of applying `transform` to `record`'s `field`.

For example:

```python
>>> field_transform({"name": "andy", "age": 55}, "name", lambda s: s.title())
{"name": "Andy", "age": 55}
>>> field_transform({"name": "andy", "age": 55}, "age", lambda n: n + 1)
{"name": "andy", "age": 56}
```

Tip: It may be helpful to recall that you can merge two dictionaries with `|`.

Tests for these two functions can be run with `uv run pytest functional/tests/test_pipeline.py`.

### `process_record(record, transforms)`

- `record` - dict - A dictionary with arbitrary data.
- `transforms` - list of tuples, each tuple having 2 elements: `(field, transform)`:
  - `field` - str - Name of a field in `item`.
  - `transform` - function - A function that takes a single parameter, the `record[field]`, and returns a transformed result.

Example:

```python
bessie = {"animal": "cow", "name": "bessie"}
process_record(
    bessie,
    [
        ("name", lambda s: s.title()),
    ]
)
```

The result would be `{"animal": "cow", "name": "Bessie"}`


```python
bessie = {"animal": "cow", "name": "bessie"}
process_record(
    bessie,
    [
        ("name", lambda s: s.title()),
        ("animal", lambda s: s.upper())
    ]
)
```

The result would be `{"animal": "COW", "name": "Bessie"}`

### process_stream(records, filters, transforms)

This function brings all of the pieces together.

- `records` - list of dictionaries - each a `record` in above functions
- `filters` - list of predicate functions - records that are `False` for any predicate will be removed from the output
- `transforms` - list of two-string tuples (same format as in `process_record`)

It should return a list of all records that are not removed by `filters`. Each record should be transformed according to `transforms`.

### Using the Pipeline

Finally, look at `clean.py`, this program will call `process_stream` to clean a list of records loaded from a file.

More specifically, your code will receive a list of records resembling:


    {"name": "STEVEN", "age": "62", "title": "AUTHOR", "retired": False}
    {"name": "JODY", "age": "20", "title": "DRIVER", "retired": False}
    {"name": "JIM", "age": "51", "title": "PAINTER", "retired": True}
    {"name": "EDDIE", "age": "53", "title": "SCIENTIST", "retired": False}
    {"name": "JANE", "age": "77", "title": "CEO", "retired": True}
    {"name": None, "age": "34", "title": "PROGRAMMER", "retired": False}

Note that some data is missing & will be represented as `None`.

Each record should:

- have the name and title converted to lower case
- have age converted to an integer
- anyone that is retired should be removed
- anyone that is missing data (name/age/title) should be removed

For this portion, your job is only to modify `filters` and `transforms` to make the data pipeline that will clean the data appropriately.  You may also define helper functions for them to use if you choose.  Do not modify the data or the rest of the file.

You can run your data pipeline with `uv run python -m functional.clean`

You can also run a test of this pipeline with `uv run pytest functional/tests/test_clean.py`.

### Conclusion

While this simple pipeline could be done trivially with procedural code, writing in a functional style enables a higher level of code-reuse and testability that would be harder to come by in a procedural approach.

Composing pipelines can be done by modifying simple lists.
One benefit of this approach would be allowing team members that are not comfortable writing Python code to still define clear pipelines by listing the transforms that they want in the order they want them.

Of course as the complexity of the data transformations (filters & predicates) grows, these benefits become more apparent.
