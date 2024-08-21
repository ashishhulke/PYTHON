# DICTIONARY METHODS 

a={"name":"harry",
    "from":"india", 
    "marks":[92,98,96]} 

print(a.items())                    #Returns a list of (key,value)tuples.
print(a.keys())                     #Returns a list containing dictionary's keys.
print(a.values())                   #Returns a list containing dictionary's Values.
a.update({"name": "Ashish"})        #Updates the dictionary with supplied key-value pairs.
print(a)
print(a.get("from"))                #Returns the value of the specified keys (and value is returned eg."india" is returned here).                

print(a.get("name1"))                #If the key is not exits in the dictionary then it will print  NONE.
print(a["name1"])                    #If the key is not exits in the dictionary then it will print ERROR.