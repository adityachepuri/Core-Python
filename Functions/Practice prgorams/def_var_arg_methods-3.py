def sum(*n, name):
    result=0
    for x in n:
        result=result+x
    print("The sum by",name,":",result)

sum(name="Durga")
sum(10,name="Ravi")
