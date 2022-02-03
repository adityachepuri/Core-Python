### WAP to print unique charecters in a string ###

s=input("Enter some string")
l= []
for x in s:
  if x not in l:
   l.append(x)
output=''.join(l)
print(output)
        
