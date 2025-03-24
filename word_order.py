from collections import OrderedDict

# Read input
n = int(input().strip())
word_count = OrderedDict()

# Count occurrences while maintaining order
for _ in range(n):
    word = input().strip()
    word_count[word] = word_count.get(word, 0) + 1

# Print the number of distinct words
print(len(word_count))

# Print the occurrences in order of first appearance
print(" ".join(map(str, word_count.values())))
