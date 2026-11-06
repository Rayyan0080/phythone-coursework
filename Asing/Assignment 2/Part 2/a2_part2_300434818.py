def min_enclosing_rectangle(radius, x, y):
    if radius < 0:
        return None
    bottom_left_x = x - radius
    bottom_left_y = y - radius
    return (bottom_left_x, bottom_left_y)

def vote_percentage(results):
    yes_count = results.count('yes')
    no_count = results.count('no')
    total_votes = yes_count + no_count
    return yes_count / total_votes

def vote():
    results = input("Enter the yes, no, abstained votes one by one and then press enter:\n").strip()
    percentage = vote_percentage(results)
    
    if percentage == 1.0:
        print("proposal passes unanimously")
    elif percentage >= 2/3:
        print("proposal passes with super majority")
    elif percentage >= 1/2:
        print("proposal passes with simple majority")
    else:
        print("proposal fails")

def l2lo(w):
    l = int(w)
    o = (w - l) * 16
    return (l, o)

# Test cases for min_enclosing_rectangle
print(min_enclosing_rectangle(1, 1, 1))  # Expected output: (0, 0)
print(min_enclosing_rectangle(4.5, 10, 2))  # Expected output: (5.5, -2.5)
print(min_enclosing_rectangle(-1, 10, 2))  # Expected output: None
print(min_enclosing_rectangle(500, 1000, 2000))  # Expected output: (500, 1500)

# Test cases for vote_percentage
print(vote_percentage('yes yes yes yes yes abstained abstained yes yes yes yes'))  # Expected output: 1.0
print(vote_percentage('yes,yes, no, yes, no, yes, abstained, yes, yes,no'))  # Expected output: 0.6666666666666666
print(vote_percentage('abstained no abstained yes no yes no yes yes yes no'))  # Expected output: 0.5555555555555556
print(vote_percentage('no yes no no no, yes yes yes no'))  # Expected output: 0.4444444444444444

# Manually run tests for vote function by calling vote()
# Example:
# vote() -> Will prompt user to input strings.

# Test cases for l2lo
print(l2lo(7.5))  # Expected output: (7, 8.0)
print(l2lo(9.25))  # Expected output: (9, 4.0)
vote()