## 6.3 Dictionaries

# Creating Dictionaries
# A dictionary is a collection of key-value pairs, where each key is unique. Dictionaries are defined using curly braces {}.
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict)  



# Accessing and Modifying Values

# Accessing Values: Use the key inside square brackets to access the corresponding value.
print(my_dict["name"])  

#Modifying Values: Assign a new value to a key to update it.
my_dict["age"] = 26
print(my_dict)  

# Adding New Key-Value Pairs: Just assign a value to a new key.
my_dict["country"] = "USA"
print(my_dict)  

# Removing Key-Value Pairs: Use the del keyword.
del my_dict["city"]
print(my_dict)  



# Dictionary Methods

#.get(): Safely access values without raising an error if the key doesn’t exist.
print(my_dict.get("name"))  
print(my_dict.get("email", "Not Found"))  

#.keys() and .values(): Return lists of keys or values in the dictionary.
print(my_dict.keys())   
print(my_dict.values()) 

# .items(): Returns key-value pairs as tuples.
print(my_dict.items()) 

#.update(): Merges another dictionary or key-value pairs into the current one.
my_dict.update({"email": "alice@example.com"})
print(my_dict)  


# That's it! Dictionaries are a versatile way to store and manipulate key-value pairs in Python.






