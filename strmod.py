def strmod(mod, str1, str2):
    '''
    Input: Takes in a mod argument (+, -, @), and two string parameters

    strmod will modify the two string parameters depending on what value the mod parameter holds:
    '+' - combines the two strings via concatenation
    '-' - removes any occurrences of str2 from str1
    '@' - combines the two strings, and then sorts their letters alphabetically

    Output: Outputs a string with the modifications made to str1 and str2. 
            Returns None if an unsupported mod value is provided.
    '''
    return (lambda mod, str1,str2 :    
        str1 + str2 if mod == '+'
        else str1 if mod == '-' and str2 == 'x'
        else str1.replace(str2, '') if mod == '-'
        else ''.join(sorted(str1 + str2)) if mod == '@'
        else None
    )(mod, str1, str2)
