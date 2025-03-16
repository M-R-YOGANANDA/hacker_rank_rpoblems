def wrap(string, max_width):
    max_width-=1
    list1=[]
    count=0
    s=""
    for i in string:
        if count<max_width:
            s+=i
            count+=1
        elif count==max_width:
            s+=i
            count=0
            list1.append(s)
            s=""
    if len(s)>0:
        list1.append(s)
    return "\n".join(list1)
    

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
