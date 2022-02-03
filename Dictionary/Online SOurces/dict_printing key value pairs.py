### Write a Python program to iterate over dictionaries using for loops###

n=int(input("Enter no.of key value pairs you want to create:"))
d={}
for i in range(n):
    key=input("Enter Key you want to create:")
    value=int(input("Enter hte value of the key:"))
    d[key]=value
for key,value in d.items():
 print(key,"Corresponds to",value)
