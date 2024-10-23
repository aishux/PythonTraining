## 7.3 String Formatting
#There are several ways to format strings in Python:

# f-strings (Python 3.6+): Embed variables directly inside strings with {}.

name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")  


# format() method: Another way to format strings.
print("My name is {} and I am {} years old.".format(name, age))  


# % operator: Older style for string formatting.
print("My name is %s and I am %d years old." % (name, age)) 
