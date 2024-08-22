# 1. Write a program using functions to find greatest of three numbers. 

def greatest():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    if(a > b and a > c):
        print("a is Greater")
    elif(b > a and b > c):
        print("b is Greater")
    else:
        print("c is Greater")

greatest()
