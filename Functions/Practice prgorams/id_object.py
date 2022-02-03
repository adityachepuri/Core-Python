def wish(name):
    print("Hello:",name)
greeting=wish 
print(id(wish))
wish("Aniketh")
print(id(greeting))  ## ids of both wish function and greeting function will be same
greeting("Aditya")
del wish
greeting("Shreeram")
