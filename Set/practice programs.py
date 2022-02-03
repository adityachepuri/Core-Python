        ### WAP to eliminate duplicates present in the list ###

## Method-1 ##

l=eval(input("Enter some list of values:"))
a=set(l)
print(a)

print()
print()

## Method-2 ##
l=eval(input("Enter some values:"))
l1=[]
for x in l:
    if x not in l1:
        l1.append(x)
print(l1)

print()



