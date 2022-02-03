#### Write a Python script to sort (ascending and descending) a dictionary by value ####

record={}
n=eval(input("Enter no.of students data:"))
for i in range(n):
    name=input("Enter the name of the student:")
    marks=int(input("Enter the marks os the student:"))
    record[name]=marks
sort_record = sorted(record.items(),key=lambda t: t[0])
print("Soreted record is:",sort_record)
