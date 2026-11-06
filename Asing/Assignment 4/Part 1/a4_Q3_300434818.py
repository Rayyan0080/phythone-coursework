def longest_run(numbers):
    '''(list of numbers) -> int
    Returns the length of the longest run (sequence of consecutive repeated values).
    '''
    max_length = 1
    current_length = 1
    
    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1]:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
            current_length = 1
    
    return max(max_length, current_length)

# Main block to test the function
if __name__ == "__main__":
    print("Please input a list of numbers separated by space: ", end="")
    raw_input = input().strip().split()
    numbers = [float(i) if '.' in i else int(i) for i in raw_input]
    result = longest_run(numbers)
    print(result)
    
    print("Please input a list of numbers separated by space: ", end="")
    raw_input = input().strip().split()
    numbers = [float(i) if '.' in i else int(i) for i in raw_input]
    result = longest_run(numbers)
    print(result)
    
    print("Please input a list of numbers separated by space: ", end="")
    raw_input = input().strip().split()
    numbers = [float(i) if '.' in i else int(i) for i in raw_input]
    result = longest_run(numbers)
    print(result)
