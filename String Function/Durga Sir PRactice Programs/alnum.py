s=input("Enter any charecter:")
if s.isalnum():
    print("Alpha Numeric Charecter:")
    if s.isalpha():
        print("Alphabet Charecter")
        if s.islower():
            print("Lower case alphabet charecter")
        else:
            print("Upper case alphabet charecter")
    else:
        print("it is a digit")
elif s.isspace():
    print("it is space charecter")
else:
    print("Non space special charecter")
                              
