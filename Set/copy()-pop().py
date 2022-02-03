#### COPY METHOD####


### ALIASING ###
s={1,2,3,4}
s1=s
print(id(s))
print(id(s1))
print("The type of s is {} and s1 is {}".format ((type(s)),(type(s1))))

print()
### CLONING ####
s={5,6,7,8}
s1=s.copy()
print(id(s))
print(id(s1))
print("s1 is {}, the id of s is {} and s1 is {}". format((s.copy()), (id(s)), (id(s1))))

print()
#### POP Method ####
s={5,6,7,8}
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s)
##print(s.pop()) --- pop() method from an empty set gives error


print()
#### remove() method ###
print("Example - remove() method")
s={5,6,7,8}
s1=s.remove(5)
print(s)
s2=s.remove(100)
print(s2)

#Note: If the intended element to be removed is not there in the set, then
    #  it returns error

print()
#### discard() ####
s={5,6,7,8}
s.discard(120)
print(s)


print()
#### Clear ###

s={5,6,7,8}
s.clear()
print(s)
