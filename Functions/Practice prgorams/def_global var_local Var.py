### Case -1 : Local and Global variable value both are assigned ###

a=10
def f1():
    a=888
    print("f1:",a)
def f2():
    print("f2:",a)
f1()
f2()
print()

f2()
f1()

### Case-2: How to consider Local Value as Global Value ###
a=10
def f1():
    global b
    b=888
    print("f1:",b)
def f2():
    global b
    b=999
    print("f2:",b)

f1()
f2()

print()
print()

### Case-3: How execution order is considered when local variable is declared as Global variable ###
def f1():
    global b
    b=888
    print("f1:",b)
def f2():
    global b
    b=999
    print("f2:",b)
def f3():
    print("f3:",b)
f3()
f2()
f1()

print()
print()

### Case-4: How to consider Global variable even though local variable is declared ####

a=10
def f1():
    a=20
    print(a)
    print(globals()['a'])
    print(globals())
f1()
