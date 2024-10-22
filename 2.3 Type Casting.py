## 2.3 Type Casting

# Sometimes, you need to convert one data type to another. This is called type casting. 
# For example, you might want to turn an integer into a string or vice versa.


# Converting to String:
age = 25
age_str = str(age)  # Convert integer to string
print("I am " + age_str + " years old.")  


# Converting to Integer:
selling_price = "100"
cost_price = 50
selling_price_int = int(selling_price)  # Convert string to integer
print("Profit = Rs", selling_price_int-cost_price)
