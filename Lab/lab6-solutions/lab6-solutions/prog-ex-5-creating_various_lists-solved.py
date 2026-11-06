n=int(input("Enter a positive even integer for the size of the list?" ))

############### Bullet 1: list of length n filled with zeros

# version 1
a=[0]*n
# see for yourself
print(a)

# version 2, accumulator pattern
a=[] 
for i in range(n):
     a=a+[0]
# see for yourself
print(a)

# version 3
# this resambles the most the way you will do this in Java (or C)

a=[None]*n  #instead of None it could be anything, as long as you know you will overwrite it
for i in range(n):
     a[i]=0
# see for yourself
print(a)

#version 4, using list method append
a=[] 
for i in range(n):
     a.append(0)
# see for yourself
print(a)

# version 5, list comprehension
a=[0 for i in range(n)]
print(a)

############# Bullet 2: list filled with random integers between 1 and 1000
import random

# version 1, accumulator pattern
b=[None]
for i in range(n):
     b=b+ [random.randint(1,1000)]
# see for yourself
print(b)

# version 2
# this resambles the most the way you will do this in Java (or C)
b=[None]*n
for i in range(n):
     b[i]=random.randint(1,1000)
# see for yourself
print(b)

############# Bullet 3: make c alias of b
c=b

############# Bullet 4:

# version 1
for i in range( len(c)//2  ):
     c[i]=0
print(c)
print(b)
print("b and c are aliases?", b is c)

# version 2. # food for thought: this also solves bullet 4. But do b and c stay aliases?

c=[0]*( len(c)//2 ) + c[n//2 : 0]

# they do not
print("b and c are aliases?", b is c)

############ Bullet 5: copy b into d

#version 1
d=b[:]
print(d)

#version 2. This resemables the most the way you do it in other languages
d=[None]*len(b)
for i in range( len(b) ):
     d[i]=b[i]
# see for yourself
print(d)

#version 3. accumulator pattern, loop over indices
d=[]
for i in range( len(b) ):
     d=d+[ b[i] ] 
# see for yourself
print(d)

# version 4, accumulator pattern, loop over items
d=[]
for item in b:
     d=d+[item] 
# see for yourself
print(d)

# version 5, using list method append
d=[]
for item in b:
     d.append(item)
# see for yourself
print(d)

# version 6, list comprehension
d=[x for x in b]
print(b)

############ Bullet 6:

#version 1:
e=[None]* ( len(b)//2 )
for i in range( len (e) ):
     print(i)
     e[i]= b[2*i] 
# see for yourself
print(e)

#version 2, possibly easier to understand why correct
# via accumulator patern 
e=[]
for i in range(0, len (b),2 ):
     e=e+[ b[i]  ]
# see for yourself
print(e)

#version 3, via append method
e=[]
for i in range(0, len (b),2 ):
     e.append(b[i])
# see for yourself
print(e)

#version 4, via list comprehension
e=[b[i] for i in range(0, len (b),2 )]
print(e)
