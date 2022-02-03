l=[10,20,30,40]
print(type(l))
z=[5,10,10,30,50,90]
print(l==z)
print("The id of l is:", id(l))
print("The id of z is:", id(z))
print(l[0]==z[0])

print(l[1]==z[1])

print(l>z)

l.clear()
print(l)
print(type(l))
