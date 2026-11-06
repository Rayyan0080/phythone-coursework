# Solution 1. See below for better solution.

x=int(input("Give me an integer: "))
y=int(input("Give me anoter integer: "))
print("The sum is", x+y)
choice=input("Type yes if you wish to compute another sum, otherwise type anything other than yes: ")
     
while(choice=='yes'):
     x=int(input("Give me an integer: "))
     y=int(input("Give me anoter integer: "))
     print("The sum is", x+y)
     choice=input("Type yes if you wish to compute another sum, otherwise type anything other than yes: ")




# Solution 2. Much shorter code and handles the cases when the user
# enters for example (wihtout quotes): "    YES "

choice='yes' # set choice to yes since we want the while loop to execute at least once in this

while(choice.lower().strip()=='yes'):
     x=int(input("Give me an integer: "))
     y=int(input("Give me anoter integer: "))
     print("The sum is", x+y)
     choice=input("Type yes if you wish to compute another sum, otherwise type anything other than yes: ")
