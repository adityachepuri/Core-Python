def calc(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum,sub,mul,div
t=calc(100,50)
for x in t:
    print(x)
t=calc(10,5)
for x in t:
    print(x)
