def display(**kwargs):
    print("Record Informaiton:")
    for k,v in kwargs.items():
        print(k,".....",v)
display(name="Aditya", marks=100, age=35, loc="Bangalore")
