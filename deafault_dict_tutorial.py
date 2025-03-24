from collections import defaultdict

# Read input values
n, m = map(int, input().split())

# Create defaultdict to store indices of words in Group A
group_a = defaultdict(list)

# Read Group A words and store their positions (1-based index)
for i in range(1, n + 1):
    word = input().strip()
    group_a[word].append(str(i))  # Store as string for easy joining

# Read Group B words and print their positions in Group A
for _ in range(m):
    word = input().strip()
    print(" ".join(group_a[word]) if word in group_a else "-1")
