# Reading the input
n, m = map(int, input().split())

# Half the size of the top and bottom rows
half_n = n // 2

# Top part (before "WELCOME")
for i in range(half_n):
    # Create the pattern for the current row
    pattern = ".|." * (2 * i + 1)
    # Print the row with proper padding to center it
    print(pattern.center(m, "-"))

# Center row with "WELCOME"
print("WELCOME".center(m, "-"))

# Bottom part (after "WELCOME")
for i in range(half_n - 1, -1, -1):
    # Create the pattern for the current row (mirror image)
    pattern = ".|." * (2 * i + 1)
    # Print the row with proper padding to center it
    print(pattern.center(m, "-"))
