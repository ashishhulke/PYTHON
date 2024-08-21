#02 if elif else ladder
Age = int(input("Enter your age: "))

if(Age >= 18):
    print("You are eligible to vote.")

elif(Age < 0):
    print("You are entering Invalid age.")

elif(Age == 0):
    print("You are entering 0 which is Invalid age.")    

else:
    print("You are not eligible to vote.")

print("EOP")