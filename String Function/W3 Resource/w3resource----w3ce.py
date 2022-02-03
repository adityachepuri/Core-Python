s=input("Enter some string:")
print("length of the string is:", len(s))
if len(s)<=2:
 print("Empty String")
else:
    print("The required string is:", s[0:2]+s[-2:])
    
