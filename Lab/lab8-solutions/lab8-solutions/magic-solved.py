def is_square(m):
     '''(2d-list) => bool
     Return True if m is a square matrix, otherwise return False
     (Matrix is square if it has the same number of rows and columns'''
     for i in range(len(m)):
          if len(m[i]) != len(m):
               return False
     return True



# SLOWER SOLUTION. No need to explain the running time analysis to the students
# unless some are that advanced
def has_1_to_n_square_v1(m):
     '''(2D list)->bool
     Returns True if the given matrix has elements 1, 2, ..., n^2
     Precondition: m is n x n squre matrix of numbers, where n>=2
     '''
     n=len(m)
     tmp=[]
     for row in m:
          for item in row:
               tmp.append(item)

     # this part basically runs in O(n^4) time,
     # or equally O(M^2) where M is the number of elements in the matrix m
     for i in range(1,n*n+1):
          if i not in tmp:
               return False
     return True


#FASTER SOLUTION, No need to explain the running time analysis to the students
# unless some are that advanced
def has_1_to_n_square_v2(m):
     '''(2D list)->bool
     Returns True if the given matrix has elements 1, 2, ..., n^2
     Precondition: m is n x n squre matrix of numbers, where n>=2
     '''
     tmp=[]
     for row in m:
          for item in row:
               tmp.append(item)
               
     # This solution basically runs in O(n^2 log n), or equally O(M log M) time
     # where M is the number of elements in the matrix m         
     tmp.sort() # provided that this .sort funtion guarantees N log N time to sort the list of N elements.
                # it is unclear if it does
     for i in range(len(tmp)):
          if tmp[i]!=i+1:
               return False
     return True


def magic(m):
     '''2D list->bool
     Returns True if m forms a magic square
     Precondition: m is a matrix with at least 2 rows and 2 columns '''

     # this tests the condition that is implied by the definition
     # i.e. that m has to be a square matrix
     if(not(is_square(m))): # if matrix is not square
          return False      # return False

     # TEST CONDITION 1

     if(not(has_1_to_n_square_v1(m))):
          return False
     
##     if(not(has_1_to_n_square_v2(m))):
##          return False

     
     # TEST CONDITION 2
     n=len(m)

     # need to find out what should we compare sums of rows, colums and diagonals to
     value=0
     for j in range(n):
          value=value+m[0][j]

     #testing if the sum of each row is equal to computed value
     for i in range(n):
          row_sum=0
          for j in range(n):
               row_sum=row_sum+m[i][j]
          if row_sum!=value:
               return False
     #testing if the sum of each column is equal to computed value
     for j in range(n):
          col_sum=0
          for i in range(n):
               col_sum=col_sum+m[i][j]
          if col_sum!=value:
               return False

     # testing the two diagonals:
     diag1_sum=0
     diag2_sum=0
     for i in range(n):
          diag1_sum=diag1_sum+m[i][i]
          diag2_sum=diag2_sum+m[n-1-i][i]
     if diag1_sum!=value or diag2_sum!=value:
          print("testing and it is false")
          return False

     # if we ever come here, we know m passed all the tests
     # thus we can safely return True
     return True


# main
# TESTING OF magic functions
# this should print True

m0=[[2,7, 6],[9,5,1],[4,3,8]]
print(magic(m0))
    
# this should print True
m1 = [[16,3,2,13], [5,10,11,8],[9,6,7,12], [4,15,14,1]]
print(magic(m1))
    
# this should print False. Why? Which condition imposed on magic squares is not true for m3
m2 = [[1,2,3,4], [5,6,7,8],[9,10,11,12], [13,14,15,16]]
print(magic(m2))
    
#this should print False. Why? Which condition imposed on magic squares is not true for m3
m3 =  [[1,1],[1,1]]
print(magic(m3))

# #this should print False. Why? Which condition imposed on magic squares is not 
m3 =  [[1,1],[1,1],[1,2]]
print(magic(m3))
