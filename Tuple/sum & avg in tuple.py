t=eval(input("Enter a tuple of numbers:"))
l=len(t)
sum=0
for x in t:
 sum=sum+x
print("The sum of tuple is:",sum)
print("the avg of entered numbers is:", sum/l)
print(type(sum))
