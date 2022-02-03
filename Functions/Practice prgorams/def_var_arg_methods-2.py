def sum(name,*n):
    result=0
    for x in n:
        result=result+x
        print("The sum by",name,":",result)

sum("Durga")
sum("Ravi",10)
sum("Pavan",10,20)
sum("Shiva",10,20,30)
sum("Aditya",10,20,40)
