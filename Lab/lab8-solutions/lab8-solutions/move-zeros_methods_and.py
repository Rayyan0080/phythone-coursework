

# yet another solution ... no need to teach it really, but just in case

def move_zeros_with_methods(lst):
     '''lst -> lst
        Returns a new list where the zeros of the given list lst
        are placed to the end (without change the relative order of other numbers)

        Precondtion: lst is a list of numbers
     '''
     num_zeros=0
     for i in range(len(lst)):
          num_zeros=num_zeros+1
     for i in range(num_zeros):
          lst.remove(0)
          lst.append(0)


# the following solution is not meant to be thought to the students since I did not teach them list comprehension.
# But it is here, just in case, somebody asks -- seems unlikly though ... and because i thought it was nice

def move_zeros_list_comprehension(lst):
     tmp = [x for x in lst if x != 0]+ [x for x in lst if x == 0]
     return tmp


x = [1, 0, 3, 0, 0, 5, 7] 
move_zeros_with_methods(x)
print(x)

x = [1, 0, 3, 0, 0, 5, 7] 
x= move_zeros_list_comprehension(x)
print(x)
