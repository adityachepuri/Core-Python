### WAP to print a2b1c3 ###

s=input("ENter a string:")
output=''
for x in s:
    if x.isalpha():
        output=output+x
        previous=x
    else:
     newch=chr(ord(previous)+int(x))
     output=output+newch
print(output)
