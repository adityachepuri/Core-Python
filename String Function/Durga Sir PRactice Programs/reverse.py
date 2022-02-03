s=input("Enter some string:")

i=len(s)-1  ## String reversal using While loop##
output=''
while i>=0:
     output=output+s[i]
     i=i-1
print(output)
     
 
print(reversed(s)) ## String reversal using reversed() method##

for x in reversed(s): ## String reversal using reverse() method and printing in one line##
  print(x, end='')


print(''.join(reversed(s))) ## String reversal using  



