def is_sorted(l):
     '''(list)->bool
       Returns True if list l is sorted from smallest to largest number,
       False otherwise
       Precondition: Elements of l are numbers'''

     # A list of lengt 1 or zero is considered sorted:
     if(len(l)<2): 
         return True
     
     # The next loop tests if there is a pair of consecutive elements
     # that are out of order. If such pair is found, it returns False
     for i in range(0, len(l)-1):
        if l[i] > l[i+1]:
            return False

     # If the program ever reaches this line, it means that no out of order pair
     # was found. Thus True can be returned
     return True
