# 5. Write a program which finds out whether a given name is present in a list or not.

list = ["Ashish", "Harshal", "Khush", "Tony", "Tanay"]

Find = input("Enter the name to search for: ")

if(Find in list):
    print(f"{Find} is present in the list.")

else:
    print(f"{Find} is not present in the list.")

    