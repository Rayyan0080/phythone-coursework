def get_year():
    '''None->int'''
    print("Please enter a four digit integer for the year.")
    ans=None
    while ans==None:
        try:
            ans=int(input())
            if ans <1000 or ans >9999:
                print("Please enter a four digit integer for the year.")
                ans=None
        except ValueError:
            print("You enter something that is not an integer.",
                   "\nPlease enter a four digit integer for the year.")
    return ans
