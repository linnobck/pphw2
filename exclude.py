def exclude(values, exclude_if):
    '''
    Input: takes in an iterable items and a predicate function (exclude_if).

    If the predicate function returns True, the value should be excluded, and vice-versa.

    Output: returns a list of items where the predicate function returned False.
    '''
    return [x for x in values if not exclude_if(x)]

def check_all(values, funcs):
    '''
    Input: takes an iterable (values) and a list of predicates (funcs).

    Calls each predicate function with the integer.

    Output: returns a list of two-element tuples. The first component being an integer from values and the second is a list of the return values.
    '''
    return [(v, [f(v) for f in funcs]) for v in values]
