def move_zeros_with_return(lst):
     '''lst -> lst
        Returns a new list where the zeros of the given list lst
        are placed to the end (without change the relative order of other numbers)

        Precondtion: lst is a list of numbers
     '''
     tmp=[0]*len(lst) #tmp is filled with zeros
     index_tmp=0
     for i in range(len(lst)):
          if(lst[i]!=0):
               tmp[index_tmp]=lst[i]
               index_tmp=index_tmp+1
          
     # why are we done?
     # because tmp is filled initially with zeros
     return tmp

x = [1, 0, 3, 0, 0, 5, 7] 
print(x)
y=move_zeros_with_return(x)
print(x,y)

#note that if we made a call like this
# x would change, or rather refer to a list with zeros moved
x=move_zeros_with_return(x) 
print(x)          
