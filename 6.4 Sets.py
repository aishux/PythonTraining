## 6.4 Sets

# 1. Creating Sets
# A set is an unordered collection of unique elements. Sets are defined using curly braces {} or the set() function.


my_set = {1, 2, 3, 4, 4}  # Duplicates are automatically removed
print(my_set)  

another_set = set([5, 6, 7])  # Using the set() function
print(another_set)  


# 2. Set Operations
# Sets support common mathematical operations like union, intersection, and difference.


# Union (|): Combines all elements from both sets (without duplicates).

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print(union_set)  


# Intersection (&): Returns elements common to both sets.

intersection_set = set1 & set2
print(intersection_set)  


# Difference (-): Returns elements present in the first set but not in the second.

difference_set = set1 - set2
print(difference_set) 


# Symmetric Difference (^): Returns elements in either set, but not in both.

symmetric_diff = set1 ^ set2
print(symmetric_diff)  

