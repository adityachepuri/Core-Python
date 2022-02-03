### Write a Python script to add a ket to dictionary ###

#d={0:10, 1:20}
#print(d)
#d1={2:30}
#d.update(d1)
#print(d)


n=int(input("Enter no.of key values you want to enter:"))
d={}
for i in range(n):
      item=input("Enter the name of the item in shopping cart:")
      price=int(input("Enter the price of {}:".format(item)))
      d[item]=price
print(d)
option=input("Let me know if you want to add anything more into cart:[Yes|No]")
if option=="Yes":
    n1=int(input("How many items you want to add in the cart:"))
    d1={}
    for j in range(n1):
           item=input("Enter the name of the item in shopping cart:")
           price=int(input("Enter the price of {}:".format(item)))
           d1[item]=price
           d.update(d1)
else:
  print("Thank you for shopping with us")
s=sum(d.values())
print("The total list of items in the cart are {} and the total price is {}".format(d,s))


