def inner_product(a, b):
     '''(list,list)->number
     returns the inner product of two lists
     Precondition: a and b have the same lenght'''

     inner_prod=0
     for i in range(len(a)):
          inner_prod=inner_prod+a[i]*b[i]
     return inner_prod
          
          
