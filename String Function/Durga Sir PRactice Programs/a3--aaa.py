### WAP to print a4b3c2 ==> aaaabbbcc ###

s=input("Enter some string:")
output=''
for x in s:
        if x.isalpha():
         output=output+x
         previous=x
        else:
            output=output+previous*(int(x)-1)
print(output)  
