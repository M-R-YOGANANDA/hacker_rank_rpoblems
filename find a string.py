def count_substring(string, sub_string):
    count=0
    x=len(sub_string)
    for i in range(len(string)-len(sub_string)+1):
        
        temp=string[i:x:1]
        x+=1
        if temp==sub_string:
            count+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
