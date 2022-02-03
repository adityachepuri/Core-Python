#### WAP to sort alphabets and digits in a string ####

s=input("Enter any string:")
s1=s2=output=' '

print(type(s1))
print(type(s2))

for x in s:
 if x.isalpha():
    s1=s1+x
 else:
    s2=s2+x
print(s1)
print(s2)

#### Using sorted() method #####
for x in sorted(s1):
 output=output+x
for x in sorted(s2):
 output=output+x
print(output)
