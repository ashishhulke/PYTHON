# 1. Arithmetic operators: +, -, *, / etc.
a = 8
b = 5
c = a + b
d = a - b
e = a * b
f = a / b
print(c, d, e, f)

# 2. Assignment operators:  =, +=, -= etc. 
z = 10 # assing 10 in z
print(z)
z += 5 # increment z by 5 & assing value in z
print(z)
z -= 4  # decrement z by 4 & assing value in z
print(z)

# 3. Comparison operators: ==, >, >=, <,  != etc.
# 1. Comparison operators always return boolean values 
x = a > b 
print(x)
x = a == b
print(x)
x = a != b
print(x)


# 4. Logical operators: and, or, not. 
m = True or False 
# Truth Table of OR
print("True or False is", True or False)
print("True or True is", True or True)
print("False or True is", False or True)
print("False or False is", False or False)

m = False and True
# Truth Table of AND
print("True and False is", True and False)
print("True and True is", True and True)
print("False and True is", False and True)
print("False and False is", False and False)

#Not Operator
print(not(False)) # NOT operator simply turn true to false and false to true and it works on boolean value onlys