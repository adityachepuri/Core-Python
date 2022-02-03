t=10,30,50,40,20
l=sorted(t)
l1=tuple(sorted(t))
print(l)
print(t)
print(type(l))


print(type(l1))

l1=tuple(sorted(t,reverse=True))
print(l1)


print(max(l1))
print(min(l1))
print()

z=(10,20,30)
print(max(z))
print(min(z))
print(z.index(10))

print()

y=('aditya','ashwini','aniketh','akshata','shreeram')
print(max(y))
print(min(y))

print()
print()

s=10,20,30,40
a=10,20,30,40.50
print(s<a)
