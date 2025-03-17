def print_rangoli(size):
    import string
    alphabet = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
    
    # Create the rangoli pattern row by row
    rows = []
    for i in range(size):
        # Create the pattern of letters for the row
        letters = '-'.join(alphabet[size-1:i:-1] + alphabet[i:size])
        # Center align and pad with '-' for proper formatting
        rows.append(letters.center(4*size-3, '-'))
    
    # Print the final rangoli
    # First part (from top to the middle)
    print('\n'.join(rows))
    # Second part (from the middle to bottom)
    print('\n'.join(rows[-2::-1]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
