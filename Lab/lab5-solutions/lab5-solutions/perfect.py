def is_perfect(n):
     ''' (number)->bool
     Returns True if the given positive integer n is perfect
     Precondition: n>=1
     '''
     current_sum = 0
     for divisor in range(1, n):
          if n % divisor == 0:
               current_sum = current_sum + divisor

     if n == current_sum:
          return True
     else:
          return False

print("Printing perfect numbers smaller than 10,000:")
for number in range(6,10001):
     if is_perfect(number):
          print(number)         
