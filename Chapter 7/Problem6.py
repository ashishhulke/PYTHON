# 6. Write a program to calculate the factorial of a given number using for loop. 
n = int(input("Enter the number: "))
i = 1
factorial = 1
while(i <= n):
    factorial *= i
    i += 1

print(f"factorial of {n} = {factorial}")