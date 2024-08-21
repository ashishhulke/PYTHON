# 7. If the names of 2 friends are same; what will happen to the program in problem 6?

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
#o/p ([('ash', 'python'), ('harsh', 'java'), ('khush', 'salesforce')])
# it will not repeat the same name twice beacause keys are unique