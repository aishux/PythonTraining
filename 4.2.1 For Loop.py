## 4.2 Looping Structures
# Loops allow you to repeat a block of code multiple times, either for a set number of iterations 
# or until a condition is met.

# 4.2.1 For Loop
# A for loop is used to iterate over a sequence (such as a list, tuple, string, or range). 
# The loop runs for each item in the sequence.

'''
Syntax:

for variable in sequence:
    # Code block to execute for each item
    
'''

# Iterating over a list
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

# range function
