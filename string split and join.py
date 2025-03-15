def split_and_join(line):
    list1=[]
    for i in line:
        if i==" ":
            list1.append("-")
        else:
            list1.append(i)
            
    string=""
    for j in list1:
        string+=str(j)
    return string
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
