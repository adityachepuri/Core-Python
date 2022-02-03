d={}
d[100]='Hyderabad'
d[200]='Delhi'
d[300]='Bangalore'
d[400]='Pune'
d[100]='India'
print(d)
print(type(d))
print(d[100])

s={100:'aditya',200:'aniketh',300:'shreeram'}
print(s)
s[400]='ashwini'
print(s)
s[100]='bangalore'
print(s)

print()
print("del function")
del d[100]
print(d)


print()
print("clear function working:", d.clear())
d[100]='aditya'
print(d)



print()
t={100:'aditya',200:'aniketh',300:'shreeram'}
t.clear()
print(t)
#s={100:'aditya',200:'aniketh',300:'shreeram'}
# del s
#print(s)

print()
### Assigning multiple values for a single key object###
t={100:['aditya','madhu','satya'],200:'aniketh',300:'shreeram'}
print(t[100])
print(t)
