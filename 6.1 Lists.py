## 6.1 Lists

# Creating Lists
# A list is a collection of items (elements), which can be of different types. 
# Lists are defined using square brackets [].


my_list = [1, 2, 3, "hello", True]
print(my_list)  # Output: [1, 2, 3, 'hello', True]


# List Operations

# 1. Indexing: Access elements by their position (starting at 0).
my_list = [10, 20, 30, 40]
print(my_list[0])  


# 2. Slicing: Extract a portion of the list.
print(my_list[1:3])  


# 3. Appending: Add an element to the end of the list.
my_list.append(50)
print(my_list)  


# 4. Modifying Elements: Change values by index.
my_list[2] = 100
print(my_list)  # Output: [10, 20, 100, 40, 50]


# 5. Removing Elements: Use remove() or pop().
my_list.remove(20)
print(my_list)  # Output: [10, 100, 40, 50]


# That's it! Lists are a versatile tool for managing collections of items.






