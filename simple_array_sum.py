def simple_array_sum(list1):
    sum=0
    for i in list1:
        sum+=int(i)
    return sum
n=int(input())
string=input()
list1=string.split()
print(simple_array_sum(list1))
