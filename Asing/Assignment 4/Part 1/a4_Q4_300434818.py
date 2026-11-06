def read_raw(file):
    '''str -> list of str
    Reads the contents of a file and returns a list of strings.
    '''
    with open(file, 'r') as f:
        return [line.strip() for line in f]

def clean_up(l):
    '''list of str -> list of str
    Removes characters with an odd count and '*' characters from the list.
    '''
    clean_board = []
    for char in set(l):
        if char != '*' and l.count(char) % 2 == 0:
            clean_board.extend([char] * l.count(char))
    return clean_board

def is_rigorous(l):
    '''list of str -> bool
    Returns True if every character appears exactly twice or the list is empty.
    '''
    return all(l.count(char) == 2 for char in set(l))

# Main block to test the functions
if __name__ == "__main__":
    file = input("Enter the name of the file: ").strip()
    b = read_raw(file)
    print("\nBefore clean-up:\n", b)
    b = clean_up(b)
    print("\nAfter clean-up:\n", b)
    if is_rigorous(b):
        print(f"\nThis list is now rigorous; it has no * and it has {len(b)} characters.")
    else:
        print(f"\nThis list has no * but is not rigorous and it has {len(b)} characters.")
