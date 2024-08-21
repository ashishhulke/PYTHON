# 9. Can you change the values inside a list which is contained in set S? 
# s = {8, 7, 12, "Harry", [1,2]} 

s = {8, 7, 12, "Harry", [1,2]}
print(s)

# No, you cannot have a list as an element in a set in Python. 
# This is because sets in Python require all their elements to be hashable, 
# which means the elements must be immutable and have a fixed hash value. 
# Lists are mutable (their contents can be changed), 
# so they are not hashable and cannot be added to a set.