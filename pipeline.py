import functools


def check_predicates(record, predicates) -> bool:
    '''
    Input: record -> dict. A dictionary with arbitrary data.
           predicates -> list of functions. Each predicate function takes a single dictionary, and returns True or False.

    This function returns True if all predicate functions return True when called with the given record, and False otherwise.

    Output: Bool
    '''
    # Lambda checks both the accumulated result AND predicate(record) evaluate to True
    return functools.reduce(lambda result, predicate: result and predicate(record), predicates, True)


def field_transform(record, field, transform):
    '''
    Input: record - dict - A dictionary with arbitrary data.
           field - str - Name of a field in item.
           transform - function - A function that takes a single parameter and returns a modified value.

    This function applies transform to record's field, and returns an updated dictionary

    Output: An updated dictionary
    '''
    return {key: transform(record[key]) if key == field else record[key] for key in record}


def process_record(record, transforms):
    '''
    Input: record - dict - A dictionary with arbitrary data.
           transforms - list of tuples - Each tuple contains two elements:
                field - str - The name of a field in the dictionary.
                transform - function - A function that takes record[field] as input and returns a transformed result.

    This function applies each transform function to its corresponding field in the record, 
    updating the record sequentially and returning a fully transformed dictionary.

    Output: Dictionary with all specified fields transformed.
    '''
    # uses the previous function to update dictionary for each tuple
    return functools.reduce(lambda current, field_trans_tuple: field_transform(current, field_trans_tuple[0], field_trans_tuple[1]), transforms, record)


def process_stream(records, filters, transforms):
    '''
    Input:  records - list of dicts - Each dictionary represents a record.
            filters - list of predicate functions - Each predicate takes a record and returns True or False.
                    Records that return False for any predicate will be excluded.
            transforms - list of tuples - Each tuple has:
                    field - str - The name of the field to modify.
                    transform - function - The function to apply to that field’s value.

    This function filters out records that fail any predicate and applies all
    transforms to the remaining records using process_record.

    Output: List of transformed dictionaries that passed all filters.
    '''
    return [process_record(record, transforms) for record in records if all(f(record) for f in filters)]
