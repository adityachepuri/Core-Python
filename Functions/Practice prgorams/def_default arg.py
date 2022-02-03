def wish(marks,age,name="Guest",msg="Good Morning"):
    print("Hello",name,msg)
    print("Student Age:",age)
    print("Student Marks:",marks)
    print("Message:",msg)

wish(100,48,"Durga") # Valid Entry
wish(age=48,marks=100) 
wish(100,age=48,marks=100) # invalid Entry - Multiple lines of argument for "marks"
