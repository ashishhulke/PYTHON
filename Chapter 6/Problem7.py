# 7. Write a program to find out whether a given post is talking about “Harry” or not.

post = input("Enter a post content: ")

if("Harry".lower() in post.lower()):
    print("The post is talking about Harry.")

else:
    print("The post is not talking about Harry.")

print(post)
