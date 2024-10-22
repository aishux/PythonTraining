## 5. Functions
# Functions allow you to reuse code by grouping statements together. 
# Define a function using the def keyword, followed by the function name and parentheses.

def greet():
    print("Hello!")
# Call the function like this:
greet()  


# Function Arguments and Parameters
# Functions can accept input via parameters:

def greet(name):  # 'name' is a parameter
    print("Hello, " + name + "!")
    
greet("Alice")  


# You can also use default parameters if no argument is passed:

def greet(name="Stranger"):
    print("Hello, " + name + "!")

greet()  

# Return Statement
# The return statement sends a value back to the caller of the function:

def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8


#That's it! Functions make your code modular and reusable, letting you write cleaner and more efficient programs.

# Design a Calculator which can perform addition, subtraction, multiplication and division
