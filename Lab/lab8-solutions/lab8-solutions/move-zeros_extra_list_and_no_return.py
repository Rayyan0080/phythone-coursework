def move_zeros_extra_list_no_return(lst):
     '''lst -> None
        moves zeros of the given list lst to the end (without change the relative order of other numbers)
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
    
     # we now just need to copy the elements of tmp to to the given list
     for i in range (len(lst)):
          lst[i]=tmp[i]

     # note that if we have not return and really need to change lst
     # that we cannot use lst=tmp[:] !!!
     # Why?
     # that changes what variable lst refers to
     # and NOT what x, the variable outside of this funciton, referrs to 

x = [1, 0, 3, 0, 0, 5, 7] 
print(x)
move_zeros_extra_list_no_return(x)
print(x)

