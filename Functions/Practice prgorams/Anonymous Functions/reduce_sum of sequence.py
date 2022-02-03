from functools import reduce
l=[10,20,30,40,50]
result=reduce(lambda x,y:x+y,l)
result1=reduce(lambda x,y:x*y,l)
result2=reduce(lambda x,y:x%y,l)
print(result)
print(result1)
print(result2)
