n=int(input("Enter no.of values:"))
d={}
for i in range(n):
    name=input("Enter the name of the student:")
    marks=int(input("Enter no.of marks:"))
    d[name]=marks
print(d)
while True:
    name = input("Enter students name you want to search for:")
    marks=d.get(name,-1)
    if marks==-1:
     print ("Student record not found")
    else:
        print("The marks of {}:{}".format(name,marks))
    option=input("Do you want to find another students marks [Yes|No]:")
    if option=="No":
     break
print("Thanks for using our application")
