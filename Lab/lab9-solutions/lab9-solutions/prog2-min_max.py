def min_or_max_index(L, flag):
    """ (list, bool) -> tuple of (object, int)

    Return the minimum or maximum item and its index from L, depending on
    whether flag is True or False.

    >>> min_or_max_index([4, 3, 2, 4, 3, 6, 1, 5], True)
    (1, 6)
    >>> min_or_max_index([4, 3, 2, 4, 3, 6, 1, 5], False)
    (6, 5)
    """ 

    index = 0
    current_value = L[0]

    if flag:
        for i in range(1, len(L)):
            if L[i] < current_value:
                index = i
                current_value = L[i]
    else:
        for i in range(1, len(L)):
            if L[i] > current_value:
                index = i
                current_value = L[i]        

    return (current_value, index)
