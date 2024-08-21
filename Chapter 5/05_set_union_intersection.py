
s1 = {1, 2, 3, 23, 8, 12}
s2 = {1,8,2,3,43}


print(s1.union(s2))                 #Returns a new set with all items from both sets no repeated values.o/p {1, 2, 3, 8, 43, 12, 23}

print(s1.intersection(s2))          #Return a set which contains only item commen in both sets. o/p {8, 1, 2, 3}  

print({1, 2, 3,}.issubset(s1))      

print(s2.issuperset({1,2}))         