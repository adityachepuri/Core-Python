### Write a Python program to multiply all items in the dictionary ###

n=int(input("Enter no.of dictionary sets you want to create:"))
d={}
result=1
for i in range(n):
      key=input("Enter the key:")
      value=int(input("Enter the value:"))
      d[key]=value
print(d)
for k in d.values():
 print("The values in the dictionary are:",d.values())
 result=result*k
print("The product of the all the values in dictionary is:",result)
