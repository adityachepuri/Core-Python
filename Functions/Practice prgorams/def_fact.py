### Factorial of a number ###

def fact(n):
 result = 1
 while n>=1:
     result = result*n
     n=n-1
 return result

for i in range(1,6):
    print("The factorial of {} is:{}".format(i,fact(i)))
