#def outer():
 #   print("outer function started")
    # def inner():
  #    print("Inner function execution")
   # inner()
#outer()

def f1():
    def inner(a,b):
        print("The Sum is:",a+b)
        print("The Average:",(a+b)/2)
    inner(10,20)
    inner(20,30)
    inner(40,50)
f1()
