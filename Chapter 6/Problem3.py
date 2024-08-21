# 3. A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams.

k1 = "Make a lot of money"
k2 = "Buy now"
k3 = "Subscribe this"
k4 = "Click this"

comment = input("Enter your comment: ")

if((k1 in comment)or(k2 in comment)or(k3 in comment)or(k4 in comment)):
    print("This is a spam.")

else:
    print("This is not a spam.")

print(comment)    