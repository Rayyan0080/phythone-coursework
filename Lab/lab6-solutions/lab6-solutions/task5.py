def is_apple(x):
     if x%4 == 0:
          appleFlag = True
     else:
          appleFlag = False
     appleFlag = appleFlag and is_pear(-200)
     return appleFlag

def is_pear(x):
     if (x < -101):
          pearFlag = True
     else:
          pearFlag = False
     return pearFlag

flag1 = is_apple(44)
flag2 = is_pear(-101)
print(str(flag1)+" "+str(flag2))
if (flag1 and flag2):
     print("ding!")
if (flag1 or flag2):
     print("dong!") 
