import math
def ah(l,x,y):
     '''(list, int,int)->(int,number/+inf)
     Returns two numbers such that ...
     Precondition: x <= y
                   and list l contains numbers
     '''
     counter=0
     min_in_range = math.inf
     for num in l:
          if num>=x and num <=y:
               counter=counter+1
               if(num<=min_in_range): # test if there is better minimum 
                    min_in_range=num  # if yes, update

     return(counter,min_in_range)


# the version below even works for strings, i.e when x and y are strings
# and l is a list of strings

def ah_v2(l,x,y):
     '''
     Precondition: x <= y
                   and list l contains numbers only or strings only
     '''
     counter=0
     min_in_range = None
     for item in l:
          if item>=x and item <=y:
               counter=counter+1
               if(min_in_range==None or item<=min_in_range): 
                    min_in_range=item

     return(counter,min_in_range)
