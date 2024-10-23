# 8. File Handling

# 8.1 Opening Files (open())
# You can open a file using the open() function, which requires the file name and the mode in which you want to open the file (e.g., read, write, etc.).


file = open("example.txt", "r")  # Opens file in read mode


# 8.2 Reading and Writing to Files

# Reading: There are several methods to read the content of a file:
# read(): Reads the entire content.

content = file.read()
print(content)

# readline(): Reads one line at a time.

line = file.readline()
print(line)

# readlines(): Reads all lines and returns them as a list.

lines = file.readlines()
print(lines)

# Writing: To write to a file, open it in write (w) or append (a) mode.

file = open("example.txt", "w")  # Opens file in write mode
file.write("Hello, World!")
file.close()  # Always close the file after writing

# Writing in append mode (a) adds content to the end of the file without overwriting existing content.



# 8.3 File Modes (r, w, a, etc.)
# r: Read mode (default). Opens the file for reading, and raises an error if the file doesn’t exist.
open("file.txt", "r")

# w: Write mode. Creates the file if it doesn’t exist or truncates the file (overwrites) if it exists.
open("file.txt", "w")

# a: Append mode. Creates the file if it doesn’t exist, or adds content to the end if it does.
open("file.txt", "a")



# 8.4 Using the with Statement for Files
# The with statement automatically handles closing the file, ensuring resources are properly released even if an error occurs. 
# It’s the preferred way to work with files.

with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # The file is automatically closed when the block ends

#That's it! File handling in Python is easy and allows you to read, write, and manipulate files efficiently, with the with statement providing a safe and clean way to handle files.
