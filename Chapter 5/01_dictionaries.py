# DICTIONARY
#Dictionary is a collection of keys-value pairs.
# PROPERTIES OF PYTHON DICTIONARIES 
# 1. It is unordered. 
# 2. It is mutable. 
# 3. It is indexed. 
# 4. Cannot contain duplicate keys.

D = {} #Empty dictionary
print(type(D))

marks = {
    "Ashish": 90, 
    "Harsh": 95,
    "Rajat": 85
}

print(marks, type(marks))
print(marks["Harsh"])