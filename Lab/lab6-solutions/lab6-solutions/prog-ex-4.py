def sum_5_consecutive_for(a):
     '''(list)->bool
     Returns True if there are 5 consecutive elements that sum to zero and False otherwise'''

     if(len(a)<5):
          return False

     for i in range(len(a)-4):
         if a[i]+a[i+1]+a[i+2]+a[i+3]+a[i+4] == 0 :
              return True
     return False

def sum_5_consecutive_while(a):
     '''(list)->bool
     Returns True if there are 5 consecutive elements that sum to zero and False otherwise'''

     if(len(a)<5):
          return False
     i=0
     while i < len(a)-4:
          if a[i]+a[i+1]+a[i+2]+a[i+3]+a[i+4] == 0 :
               return True
          i=i+1
     return False        
