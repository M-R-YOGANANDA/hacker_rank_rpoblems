def print_formatted(number):
    width = len(bin(number)[2:])  # Get the width of the binary representation of number
    
    for i in range(1, number + 1):
        decimal = str(i).rjust(width)
        octal = oct(i)[2:].rjust(width)
        hexadecimal = hex(i)[2:].upper().rjust(width)  # Convert to uppercase
        binary = bin(i)[2:].rjust(width)

        print(f"{decimal} {octal} {hexadecimal} {binary}")



if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
