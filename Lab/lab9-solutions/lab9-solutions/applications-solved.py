'''We study algorithms

O(1) - basic operations addition/multiplication function call, accessing a set

O(log n) - bigger than O(1), but less than O(n)

O(n) - iterating over a list (of length n)

O(n^2)

'''

def element_uniqueness(L):
     '''(list)->bool
     Returns True if all the elements in the list are distinct,
     in other words, if there is no element in the list that appears more than once.
     Precondition: L is not empty

     >>> element_uniqueness([2, 2,2, 2, 8])
     False
     >>> element_uniqueness([1,-20,-1])
     True
     >>> element_uniqueness([3,2,4,0,3])
     False
     >>> element_uniqueness([10])
     True
     >>> element_uniqueness([10,10])
     False
     >>> element_uniqueness([10,-1])
     True
     '''
     X=sorted(L) # X is is a sorted versin of L

     # answer in short lists, those of length 1
     if len(X)==1:
          return True

     for i in range(len(X)-1):
          if X[i]==X[i+1]: 
               return False
     return True


def one_unique_at_least(L):
     '''(list)->bool
     Returns True if there exist at least one element in L that is unique,
     in other words, that appears exactlly once in the list
     Precondition: L is not empty
     >>> one_unique_at_least([2,2,2,2,8])
     True
     >>> one_unique_at_least([2,1,2])
     True
     >>> one_unique_at_least([1,-20,-1])
     True
     >>> one_unique_at_least([3,2,2,3,3])
     False
     >>> one_unique_at_least([10])
     True
     >>> one_unique_at_least([10,10])
     False
     >>> one_unique_at_least([10,-1])
     True
     '''
     X=sorted(L) # X is a sorted versin of L

     # answer in short lists, those of length 1
     if len(X)==1:
          return True

     # 1st element is unique if the one after is different
     # last element is unique if the one before is different
     # Every other element is unique if both the one before
     # and the one after are different for it
     
     for i in range(len(X)):
          if i==0 and X[i]!=X[i+1]: # first element
               return True
          elif i==len(L)-1 and X[i]!=X[i-1]: # last element
               return True
          elif i!=0 and i!=len(L)-1: #neither first nor last element
               print(X[i-1],X[i+1])
               if X[i]!=X[i-1] and X[i]!=X[i+1]:
                    return True
     return False
     
def all_unique(L):
     ''' (list,int)->list
     Return a list of elements of L that appear exactlly once in L. 
     Precondition: L is not empty
    
     >>> all_unique([2, 2,2, 2, 8])
     [8]
     >>> all_unique([1,-20,-1])
     [-20,-1,,1]
     >>> all_unique([3,2,2,3,3])
     []
     >>> all_unique([10])
     [10]
     >>> all_unique([10,10])
     []
     >>> all_unique([10,-1])
     [-1,10]
     '''
     X=sorted(L) # X is a sorted versin of L

     # answer in short lists, those of length 1
     if len(X)==1:
          return [X[0]]
     
     result=[]

     for i in range(len(X)):
          if i==0 and X[i]!=X[i+1]: # first element
               result.append(X[i])
          elif i==len(L)-1 and X[i]!=X[i-1]: # last element
               result.append(X[i])
          elif i!=0 and i!=len(L)-1: #neither first nor last element
               if X[i]!=X[i-1] and X[i]!=X[i+1]:
                    result.append(X[i])
     return result

def element_uniqueness_v2(L):
     return len(all_unique(L)) == len(L)

def one_unique_at_least_v2(L):
     return len(all_unique(L)) > 0

def count_unique(L):
     '''(list,int)->int
     Return the number of unique elements of L,
     i.e. the number of elements that appear exactlly once in L
     Precondition: L is not empty
    
     >>> count_unique([2, 2,2, 2, 8])
     1
     >>> count_unique([1,-20,-1])
     3
     >>> count_unique([3,2,2,3,3])
     0
     >>> count_unique([10])
     1
     >>> count_unique([10,10])
     0
     >>> count_unique([10,-1])
     2
     '''

     return len(all_unique(L))
          
                               

def duplicates(L):
     ''' (list)->int
     Returns True if the given list L has duplicates, in other,
     if it has at least one element that appears two or more times.
     Precondition: L is not empty

     >>> duplicates([2, 2,2, 2, 8])
     True
     >>> duplicates([1,-20,-1])
     False
     >>> duplicates([3,2,2,3,3])
     True
     >>> duplicates([10])
     False
     >>> duplicates([10,10])
     True
     >>> duplicates([10,-1])
     False
     '''
     if len(L) != len(all_unique(L)):
          return True
     else:
          return False

def majority(L):
     '''(list)->
     An element of a list is called "majority" if MORE THAN half of the elements of the list are equal to it.
     This function returns the majority element of L if such an element exsits, otherwise it returns None
     >>> majority([2,1,2])
     2
     >>> majority([10,5,1,5,5])
     5
     >>> majority([5,5,1,1])
     
     >>> majority([3])
     3
     >>> majority([8,8,2,8])
     8
     '''
     X=sorted(L) # X is a sorted versin of L
     mid=(len(X)-1) // 2
     candidate=X[mid] # if there exists a majority element than
                      # the only candidate for it is in the middle of the sorted list
                      # Why?
     #we now need to see if that element appears more than half the times
     count=0
     for item in X:
          if item==candidate:
               count=count+1
     if count > len(L)/2:
          return candidate
     else:
          return None

