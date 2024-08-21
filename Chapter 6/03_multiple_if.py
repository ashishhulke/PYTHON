# Multiple if statements

Age = int(input("Enter your age: "))
# If statement no 1
if(Age%2  == 0):
    print("Number is even.")

# If statement no 2
if(Age >= 18):
    print("You are eligible to vote.")

elif(Age < 0):
    print("You are entering Invalid age.")

elif(Age == 0):
    print("You are entering 0 which is Invalid age.")    

else:
    print("You are not eligible to vote.")

print("EOP")

