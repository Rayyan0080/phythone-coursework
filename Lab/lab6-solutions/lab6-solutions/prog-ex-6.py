def fib(n):
     ''' (int)->None
         prints first n fibonacci numbers (in a list form)
         Precondition: n>=2
     '''
     a=[None]*n  
         
     a[0]=1
     a[1]=1
     i=2
     while i<n:
          a[i]=a[i-1]+a[i-2]  
          i=i+1
     print(a)

# the below solution is even shorter
# since first two fibonacci numbers are 1 we might as well fill everything with 1
# but 3rd, 4th ... number will be overwritten (correctly) in the while loop

def fib_v2(n):
     ''' (int)->None
         prints first n fibonacci numbers (in a list form)
         Precondition: n>=2
     '''
     a=[1]*n  
     i=2
     while i<n:
          a[i]=a[i-1]+a[i-2]  
          i=i+1
     print(a)
