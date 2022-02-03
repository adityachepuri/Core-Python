#### WRITE A PYTHON SCRIPT TO CONCATENATE FOLLOWING DICTIONARIES TO CREATE A NEW ONE ####

##Using update() method

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
print(dic1)
dic1.update(dic2)
dic1.update(dic3)
print("THe result using update() method:",dic1)


## Using for loop ###

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4={}
for d in (dic1, dic2, dic3):
    dic4.update(d)
print("Result using for loop:",dic4)
