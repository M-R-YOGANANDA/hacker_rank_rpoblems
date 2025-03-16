def check_c(s):
    x=False
    for i in s:
        if i.isalnum():
            x=True
            break
    print(x)
    x=False
    for i in s:
        if i.isalpha():
            x=True
            break
    print(x)
    x=False
    for i in s:
        if i.isdigit():
            x=True
            break
    print(x)
    x=False
    for i in s:
        if i.islower():
            x=True
            break
    print(x)
    x=False
    for i in s:
        if i.isupper():
            x=True
            break
    print(x)
    
if __name__ == '__main__':
    s = input()
    check_c(s)
