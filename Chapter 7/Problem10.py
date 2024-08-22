# 10. Write a program to print multiplication table of n using for loops in reversed order.

a = int(input("Enter a number: "))
i = 1
while(i<11):
    print(f"{a} x {11-i} = {a*(11-i)}")
    i += 1