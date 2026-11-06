def number_divisible(numbers, n):
    '''(list of int, int) -> int
    Returns the number of elements in the list that are divisible by n.
    '''
    count = 0
    for num in numbers:
        if num % n == 0:
            count += 1
    return count

# Main block to test the function
if __name__ == "__main__":
    print("Please input a list of integers separated by spaces: ", end="")
    raw_input = input().strip().split()
    # Convert each value to a float or int if necessary
    numbers = [float(i) if '.' in i else int(i) for i in raw_input]
    n = int(input("Please input an integer: "))
    result = number_divisible(numbers, n)
    print(f"The number of elements divisible by {n} is {result}")
