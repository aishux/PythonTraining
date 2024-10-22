## 4.3 Control Flow Tools: break, continue, and pass
# Python provides additional control over loops using special keywords: break, continue, and pass.


# 4.3.1 break
# break is used to exit a loop early, even if the loop condition hasn’t finished.
for num in range(1, 11):
    if num == 5:
        break  # Exit the loop when num is 5
    print(num)
    
# This will print numbers 1 to 4, then exit the loop when num equals 5.


# 4.3.2 continue
# continue skips the current iteration of the loop and moves on to the next one.

for num in range(1, 6):
    if num == 3:
        continue  # Skip printing when num is 3
    print(num)

# This will print numbers 1, 2, 4, and 5, skipping 3.


# 4.3.3 pass
# pass does nothing and is used when you want to include a placeholder for future code.

for num in range(1, 6):
    if num == 3:
        pass  # Do nothing when num is 3
    print(num)

# This will print all numbers from 1 to 5. 
# The pass keyword doesn’t affect the output but can be useful when designing the structure of a program.


