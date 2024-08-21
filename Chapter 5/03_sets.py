# SETS IN PYTHON. 
# Set is a collection of non-repetitive elements.
# PROPERTIES OF SETS 
# 1. Sets are unordered => Element’s order doesn’t matter 
# 2. Sets are unindexed => Cannot access elements by index 
# 3. There is no way to change items in sets. 
# 4. Sets cannot contain duplicate values.

e = set()                       # Empty set
print(type(e))

s = {1, 2, 3, 1, 23, 12, 1, 32} # output {32, 1, 2, 3, 23, 12} Sets cannot contain duplicate values.
print(s)                        # output {32, 1, 2, 3, 23, 12} Sets are unordered => Element’s order doesn’t matter

