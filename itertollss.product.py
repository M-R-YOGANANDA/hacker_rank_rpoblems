from itertools import product

# Read input
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Compute the cartesian product
result = product(A, B)

# Print the result as space-separated tuples
print(" ".join(str(tup) for tup in result))
