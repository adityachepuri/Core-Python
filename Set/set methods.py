s={10,20,30,40}
t={10,50,60,70}
s.update(t)
print("The result for s.update(t):",(s))
print("The result for s.update(t):",(t))   
print()
print()
a={10,20,30,40}
b={10,50,60,70}
b.update(a)
print("The result for t.update(s):",(a))
print("The result for t.update(s):",(b))

print()
print()
print()

s={1,2,3,4}
l=['A','B','C','D']
s.update(l,'abcd')
print(s)

print()
print()

q={11,12,13,14}
q.update(range(10,100,10),range(2,10,2))
print(q)
q.add(27)
print(q)
