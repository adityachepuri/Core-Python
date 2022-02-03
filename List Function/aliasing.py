#### TWO WAYS OF CLONING ####

###Method 1: Using copy() function #####

x=[10,20,30,40]

y=x.copy()
y[1]=999
print(x)
print("index of x is:", id(x))
print('Y:',y)
print("index of y is:",id(y))

###Method 2: using index method ###
y=x[:]
print("the new list is:", y)
y[1]=777
print("the modified list is:",y)
print(id(x))
print(id(y))
