# 1. Write a program to find the greatest of four numbers entered by the user.

Num1 = int(input("Enter a number: "))
Num2 = int(input("Enter a number: "))
Num3 = int(input("Enter a number: "))
Num4 = int(input("Enter a number: "))

if(Num1 > Num2 and Num1 < Num3 and Num1 > Num4):
    greatest = Num1

elif(Num2 > Num1 and Num2 > Num3 and Num2 < Num4):
    greatest = Num2

elif(Num3 > Num1 and Num3 > Num2 and Num3 < Num4):
    greatest = Num3

else:
    greatest = Num4

print("The greatest number is", greatest)    