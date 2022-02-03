### Merging two dictionaries###
n=int(input("Enter the number of dictionaries you want to create:"))
d={}
i=1
while i<=n:
      key=input("Enter the key your want to create:")
      value=int(input("Enter the value of the key:"))
      d[key]=value
      d.update(d)
      i=i+1
print("dictionary iteration using while loop",d)


