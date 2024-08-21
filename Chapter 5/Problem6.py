# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique.

d = {}
name = input("Enter your Name: ")
Lang = input("Enter your Favorite Language: ")
d.update({name : Lang})

name = input("Enter your Name: ")
Lang = input("Enter your Favorite Language: ")
d.update({name : Lang})

name = input("Enter your Name: ")
Lang = input("Enter your Favorite Language: ")
d.update({name : Lang})

name = input("Enter your Name: ")
Lang = input("Enter your Favorite Language: ")
d.update({name : Lang})

print(d.items())
