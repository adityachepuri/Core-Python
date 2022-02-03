l=[0,5,10,15,20,25]
l1=filter(lambda n:n%2==0,l)
l2=list(filter(lambda n:n%2==0,l))
l3=list(filter(lambda n:n%2!=0,l))
print(l1)
print(type(l1))
print(l2)
print(type(l2))
print(l3)
