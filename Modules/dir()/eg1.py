ddef f1():
    if __name__=='__main__':
        print("The code executed directly as a program")
        print("THe value of __name__:",__name__)
    else:
        print("The code executed indirectly as a module from some other program")
        print("THe value of __name__",__name__)
    f1()
    
