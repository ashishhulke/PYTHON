# 8. If languages of two friends are same; what will happen to the program in problem 6?

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
#([('ash', 'python'), ('harsh', 'java'), ('khush', 'c'), ('tony', 'python')])
#it will print the same language given beacause it allows the values to duplicate but keys must be unique