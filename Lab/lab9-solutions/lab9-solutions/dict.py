def letter2number(lgrade):
    '''(str)->int
    Returns the number grade corresponding to the letter grade lgrade'''

    if lgrade=="+A":
        return 10
    elif lgrade=="A":
        return 9
    elif lgrade=="-A":
        return 8
    elif lgrade=="B+":
        return 7
    elif lgrade=="B":
        return 6
    elif lgrade=="C+":
        return 5
    elif lgrade=="C":
        return 4
    elif lgrade=="D+":
        return 3
    elif lgrade=="D":
        return 2
    elif lgrade=="E":
        return 1
    elif lgrade=="F":
        return 0

def letter2number_v2(lgrade):
    '''(str)->int
    Returns the number grade corresponding to the letter grade lgrade'''
    grades = {'A+':10,'A':9, 'A-':8, 'B+':7, 'B':6, 'C+':5, 'C':4, 'D+':3, 'D':2, 'E':1, 'F':0}
    return grades[lgrade]

# Exercise 6.15
def lookup(phonebook):
    '''(dict)-> None
    implements interactive phone book service using the input phonebook dictionary'''
    while True:
        first = input('Enter the first name: ')
        last = input('Enter the last name: ')

        person = (first, last)    # construct the key

        if person in phonebook:   # if key is in dictionary
            for number in phonebook[person]: # print all numbers
                print(number)
        else:                     # if key not in dictionary
            print('The name you entered is not known.')

# Problem 6.20
def reverse(phonebook):
    ''' (dict)->dict
       phonebook is a dictionary mapping names (keys) to
       phone numbers (values); function returns another dictionary
       representing the reverse phone book mapping phone numbers
       (keys) to the names (values)'''
    reversebook = {}
    for key in phonebook:
        reversebook[phonebook[key]] = key
    return reversebook
