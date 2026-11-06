def move_zeros_in_place(lst):
     '''lst -> None
        moves zeros of the given list lst to the end (but it may change the relative order of other numbers)
        Precondtion: lst is a list of numbers
     '''
     front=0;
     back=len(lst)-1
     while(front<back):
          if(lst[front]==0 and lst[back]!=0):
               lst[front]=lst[back]
               lst[back]=0
               front=front+1 
               back=back-1
          elif (lst[front]==0 and lst[back]==0):
               back=back-1
          else:
               front=front+1

x = [1, 0, 3, 0, 0, 5, 7] 
print(x)
move_zeros_in_place(x)
print(x)

