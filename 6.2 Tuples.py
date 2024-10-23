## 6.2 Tuples

# A tuple is an ordered, immutable collection of elements. Once created, the elements cannot be changed. 
# Tuples are defined using parentheses ().

my_tuple = (1, 2, 3, "hello", True)
print(my_tuple)  # Output: (1, 2, 3, 'hello', True)


#Single-element Tuple: Add a comma after the element to create a tuple with one item.

single_tuple = (42,)

# Tuple Operations

# Indexing: Access elements by their position (starting at 0), just like lists.
print(my_tuple[0]) 

# Slicing: Extract a portion of the tuple.
print(my_tuple[1:3])  

'''
PLEASE NOTE : 
# Immutability: Tuples cannot be modified (no appending, removing, or changing elements). 
# Any operation that attempts to change a tuple will raise an error.
# This will raise an error: my_tuple[0] = 100
'''

# Tuple Concatenation: You can combine tuples using the + operator.

new_tuple = my_tuple + (4, 5)
print(new_tuple)  # Output: (1, 2, 3, 'hello', True, 4, 5)



# That's it! Tuples are like lists, but they are immutable, making them useful when you want to ensure the data remains unchanged.





