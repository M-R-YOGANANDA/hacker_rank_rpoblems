def divmod(a,b):
    div=a//b
    mod=a%b
    return div,mod
a=int(input())
b=int(input())
div,mod=divmod(a,b)
print(div)
print(mod)
lis=["(",div,", ",mod,")"]
for i in lis:
    print(i,end="")
