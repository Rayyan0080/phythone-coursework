def arithmetic(l):
     '''(list)->bool
       Returns True if list l contains an arithmetic sequence,
       False otherwise
       Precondition: Elements of l are numbers'''

     if(len(l)<2):
         return True
     
     # check that the difference between consecutive numbers is
     # equal to the difference between the first two numbers 
     diff = l[1] - l[0]
     for i in range(1, len(l)-1):
        if l[i+1] - l[i] != diff:
            return False
     return True
