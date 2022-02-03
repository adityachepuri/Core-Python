l1=[10,20,30,40,50]
print("entered list is:",l1)
x=int(input("Enter elemet to be remoeved:"))
if x in l1:
 l1.remove(x)
 print("Successfuilly removed")
else:
  print("specified element is not available")
print(l1)
