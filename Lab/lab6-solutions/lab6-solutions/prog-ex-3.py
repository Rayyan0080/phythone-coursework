def first_neg(a):
     '''(list)->int or None
      Returns the position/index of the first negative number in the given list a
      Returns None if there is no negative number or the list is empty

      Precondition: a contains numbers
      '''
     if len(a)==0:
          return None
     i=0
     while(i<len(a) and a[i]>=0):
          i=i+1

     if(i==len(a)):
          return None
     else:
          return i
     
def first_neg_v2(a):
     '''(list)->int or None
      Returns the position/index of the first negative number in the given list a
      Returns None if there is no negative number or the list is empty

      Precondition: a contains numbers'''
     
     i=0
     
     # this solution (while loop) works too
     # since a[i]>=0 will never get executed (and thus case a crash) if len(a) is zero
     # The reason is that Python knows that False and anyting is False
     # so it does not evaluate the second expressin
     # if the first is already False in case of the "and" operator

     while(i<len(a) and a[i]>=0): 
          i=i+1

     if(i==len(a) or len(a)==0):
          return None
     else:
          return i
