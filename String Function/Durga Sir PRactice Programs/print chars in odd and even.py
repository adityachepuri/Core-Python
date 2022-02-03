s=input("Enter some string:")

### Using Slice Operator ###

print("charecters at even position:",s[::2])
print("charecters at odd positions:",s[1::2])

### Using while loop###
i=0
print("the charecters in the even indexes are:")
while i<len(s):
   print(s[i],end=' ')
   i=i+2
print()
i=1
print("the charecters in the odd indexes are:")
while (i<len(s)):
    print(s[i],end=' ')
    i=i+2

### Using For loop ###
for index in range(len(s)):
 if index%2==0:
  print(s[index],end=' ')


