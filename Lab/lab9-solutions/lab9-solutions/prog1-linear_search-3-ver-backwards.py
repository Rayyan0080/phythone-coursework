# LINEAR SERACH FROM THE BACK OF THE LIST


# implementation with while loop
def linear_search_v1(lst, value):
     """ (list, object) -> int

     Return the index of the last occurrence of value in lst, or return
     -1 if value is not in lst.

     >>> linear_search_v1([2, 5, 1, -3], 5)
     1
     >>> linear_search_v1([2, 4, 2], 2)
     2
     >>> linear_search_v1([2, 5, 1, -3], 4)
     -1
     >>> linear_search_v1([], 5)
     -1
     """

     i = len(lst) - 1 # The index of the next item in lst to examine.

     # Keep going until we reach the end of lst or until we find value.
     while i != -1 and lst[i] != value:
          i = i - 1

     # If we fell off the end of the list, we didn't find value.
     if i == -1:
          return -1
     else:
          return i

# implementation with for loop
def linear_search_v2(lst, value):
     """ (list, object) -> int

     Return the index of the last occurrence of value in lst, or return
     -1 if value is not in lst.

     >>> linear_search_v2([2, 5, 1, -3], 5)
     1
     >>> linear_search_v2([2, 4, 2], 2)
     2
     >>> linear_search_v2([2, 5, 1, -3], 4)
     -1
     >>> linear_search_v2([], 5)
     -1
     """

     # The first index is included, the second is not, and the third is the
     # increment.
     for i in range(len(lst) - 1, -1, -1):
          if lst[i] == value:
               return i
     return -1


#implementation with sentinal version:

def linear_search_v3(lst, value):
     """ (list, object) -> int

     Return the index of the last occurrence of value in lst, or return
     -1 if value is not in lst.

     >>> linear_search_v3([2, 5, 1, -3], 5)
     1
     >>> linear_search_v3([2, 4, 2], 2)
     2
     >>> linear_search_v3([2, 5, 1, -3], 4)
     -1
     >>> linear_search_v3([], 5)
     -1
     """

     # Add the sentinel at the beginning.
     lst.insert(0, value)
     i = len(lst) - 1

     # Keep going until we find value.
     while lst[i] != value:
          i = i - 1

     # Remove the sentinel.
     lst.pop(0)

     # If we reached the beginning of the list we didn't find value.
     if i == 0:
          return -1
     else:
     # When we inserted, we shifted everything one to the right. Subtract 1
     # to account for that.
          return i - 1


