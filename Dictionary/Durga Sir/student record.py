### WAP to enter name and % of marks in a dictionary and display info on the screen###

rec={}
n=int(input("Enter number of students:"))
i=1
while i<=n:
    name=input("Enter student name:")
    marks=input("Enter % of marks:")
    rec[name]=marks
    i=i+1
print("Name of student","\t","% of Marks")
for x in rec:
    print("\t",x,"\t\t",rec[x])
