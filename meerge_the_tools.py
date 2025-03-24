def merge_the_tools(s, k):
    for i in range(0, len(s), k):
        chunk = s[i:i+k]
        seen = set()
        print("".join([c for c in chunk if not (c in seen or seen.add(c))]))



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
