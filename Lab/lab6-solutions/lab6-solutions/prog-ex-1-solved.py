def sum_odd_while_v2(n):
     '''(int)->int
        Returns the sum of all odd integers between 5 and n 
     '''
     i=5
     sum_boring=0
     while i<=n:
          sum_boring=sum_boring+i
          i=i+2
     return sum_boring
