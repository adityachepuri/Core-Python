#### Program to print sum squares of first 10 numbers####

### Method-1 Using for loop and append() function

l1=[]
for x in range(1,11):
    l1.append(x*x)
print(l1)

### Methos-2 Using Comprehensive function

l=[x*x for x in range(1,11)]
print(l)
print()
print()

l=[x*x for x in range (1,21)]
print(l)
l1=[x for x in l if x%2==0]
print(l1)
print()
l.extend(l1)
print(l)

print()
print()


##Example##
words = ['Balayya','Nag', 'Venkatesh', 'Chiru']
l=[z for z in words if len(z)>6]
print(l)
print()
print()

##Example##
n1=[10,20,30,40]
n2=[30,40,50,60]
n3=[x for x in n1 if x not in n2]
print(n3)

print()
print()

