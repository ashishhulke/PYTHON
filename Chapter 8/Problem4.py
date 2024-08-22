# 4. Write a recursive function to calculate the sum of first n natural numbers. 

# def sum_of_natural_numbers(n):
#     i = 1
#     sum = 0
#     while(i<=n):
#         sum += i
#         i+=1
#     return sum


# n = int(input("Enter the number: "))
# print(f"sum of first {n} natural numbers is = {sum_of_natural_numbers(n)}")

def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n

n = int(input("Enter the number: "))
print(f"sum of first {n} natural numbers is = {sum(n)}")