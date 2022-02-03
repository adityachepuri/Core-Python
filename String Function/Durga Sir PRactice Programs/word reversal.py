         ### WAP to print reversal order of entered words in a strin###

s=input("Enter some string:")
l=s.split()

print(l)

l1=[]
i=len(l)-1
while i>=0:
    l1.append(l[i])
    i=i-1
output=' '.join(l1)
print(output)
