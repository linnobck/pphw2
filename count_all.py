import functools
# from functools import reduce
# something is wrong with my IDE, and the import isn't working properly, which is why I use functools.reduce


def newlen(s) -> int:
    '''
    Input: takes an iterable 

    This function taken an interable and returns its length, an integer.

    Output: returns integer matching len
    '''
    
    # use _ as a py convention because we don't care about the value in that place 
    return functools.reduce(lambda length, _: length + 1, s, 0)


def count_all(*lists):
    '''
    Input: any number of lists
    
    This function takes in any number of lists and returns the total count of objects inside the lists.

    Ouput: total count of objects as integer
    '''
    return functools.reduce(lambda count, i: count + newlen(i), lists, 0)
