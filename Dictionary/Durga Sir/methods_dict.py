### Important meods in Dictionary ###

print("1. dict() method example")
d=dict()
print(d)

print()
print()

print("2. len() method example")
d={100:'aditya',95:'aniketh'}
print(len(d))

print()
print()

print("3. get() method example")
car = {"brand": "Ford", "model": "Mustang","year": 1964}
print(car.get("model")) 
print(car.get("price")) ### returns None, becasue specified key is not available
print(car.get("price","aditya"))### returns aditya as default value
                                ##syntax - d.get(key,default value

car = {"brand": "Ford", "model": "Mustang","year": 1964}
car.pop("brand")
print(car)
print()
print()
print()

mycar = {"brand": "Ford", "model": "Mustang","year": 1964}
mycar.popitem()
mycar.popitem()
mycar.popitem()
print(mycar)
