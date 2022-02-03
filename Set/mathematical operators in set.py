### union() function in Set ###

s={1,2,3,4}
t={4,5,6,7}
u={7,8,9,10}
print(s.union(t,u))

print()
## using '|' operator instead of union() ##
s={1,2,3,4}
t={4,5,6,7}
u={7,8,9,10}
print(s|t|u)

print()
### intersection() method in Set ###

s={1,2,3,4}
t={4,5,3,2}
u={4,8,3,3}
print(s.intersection(t,u))

print()
print("Result using & operator")
s={1,2,3,4}
t={4,5,3,2}
u={4,8,3,3}
print(s&t&u)

print()
### difference() ###
x={10,20,30,40}
y={20,30,50,60}
z={20,30,70,80}
print()
print("The result using x.difference(y,z)):",x.difference(y,z))
print()
print("The result using y.difference(x,z):",y.difference(x,z))

print()
### difference() using '-' operator ###
x={10,20,30,40}
y={20,30,50,60}
z={20,30,70,80}
print(x-y-z)

print()
### symmetric difference ###
x={10,20,30,40}
y={20,30,50,60}
z={20,30,70,80}
print(x.symmetric_difference(y))
print()
print(x^y)

