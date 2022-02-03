### WAP tp merge two dictionaries ###

n=int(input("Enter no.of dict values to be entered:"))
d={}
for i in range(n):
     key=eval(input("Enter the details of key :"))
     value = eval(input("Enter the details of value:"))
     d[key]=value
print(d)
