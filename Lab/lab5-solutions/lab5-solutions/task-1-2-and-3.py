
s1="this is a string"
s2="this is a string"
s3=s1
print(s1==s3)
s1="aha"
print(s3==s1)
print(s3==s2)

s1="this is a string"
print("A variable s1, referes to an object of what type?")
print( type(s1) )

s4=["this is a string"]
print("A variable s4, referes to an object of what type?")
print( type(s4) )

print("A variable s4[0], referes to an object of what type?")
print( type(s4[0]) )

s5=[2, 4, "oaxaca", True]
s6=[2, 4, "oaxaca", True]
print(s5==s6)
print(s5 is s6)
s7=s6
print(s6 is s7)
s7[3]=False
print(s5)
print(s6)
print(s7)



