def first_one(L):
     ''' (list) -> int
     Return the index of the first occurrence of 1 in L, or return
     -1 if 1 is not in L.
     Precondition: L only has 0s and 1s and all 0s appear before all 1s

     >>> first_one( [0,0,0,0,0,0,1,1] )
     5
     >>> first_one( [1,1] )
     0
     >>> first_one( [0,0,0] )
     -1
     '''

     # Mark the beginning and the end indices of the unexplored sublist.
     b=0
     e = len(L) - 1

     while b != e + 1:
          mid = (b + e) // 2
          if L[mid] == 0:
               b=mid+1
          else:
               e=mid-1
          
     if 0 <= b < len(L) and L[b] == 1:
          return b
     else:
          return -1

def last_zero(L):
     ''' (list) -> int
     Return the index of the last occurrence of 0 in L, or return
     -1 if 0 is not in L.
     Precondition: L only has 0s and 1s and all 0s appear before all 1s'''

     # Mark the beginning and the end indices of the unexplored sublist.
     index_of_first_one=first_one(L)
     if len(L)==0:
          return -1
     elif index_of_first_one==-1:
          return len(L)-1
     else:
          return index_of_first_one-1
          return 
          
 
