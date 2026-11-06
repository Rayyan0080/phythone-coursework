def two_length_run(numbers):
    '''(list of numbers) -> bool
    Returns True if the list has at least one run (sequence of consecutive repeated values of length 2).
    '''
    for i in range(len(numbers) - 1):
        if numbers[i] == numbers[i + 1]:
            return True
    return False

# Main block to test the function
if __name__ == "__main__":
    print("Please input a list of numbers separated by space: ", end="")
    raw_input = input().strip().split()
    numbers = [float(i) if '.' in i else int(i) for i in raw_input]
    result = two_length_run(numbers)
    print(result)
    
    print("Please input a list of numbers separated by space: ", end="")
    raw_input = input().strip().split()
    numbers = [float(i) if '.' in i else int(i) for i in raw_input]
    result = two_length_run(numbers)
    print(result)
    
    print("Please input a list of numbers separated by space: ", end="")
    raw_input = input().strip().split()
    numbers = [float(i) if '.' in i else int(i) for i in raw_input]
    result = two_length_run(numbers)
    print(result)
