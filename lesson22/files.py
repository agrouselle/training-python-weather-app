# r = Read
# a = Append
# w = Write
# x = Create

# Read - error if file doesn't exist

import os
f = open("names.txt", "r")
# print(f.read())
# print(f.read())
# print(f.readline())
# print(f.readline())

# for line in f:
#     print(line)
# f.close()

try:
    f = open("names.txt", "r")
    print(f.read())
except:
    print("The file you want to read does not exist")
finally:
    f.close()

# Append - creates the file if it doesn't exist
try:
    f = open("names.txt", "a")
    f.write("\nJohn")
    f.write("\nMarc")
except Exception as exception:
    print("An error occurred : {exception}")
finally:
    f.close()

try:
    f = open("names.txt")
    print(f.read())
except Exception as exception:
    print("An error occurred : {exception}")
finally:
    f.close()

# Write (overwrite)
# try:
#     f = open("names.txt", "w")
#     f.write("\nJohn")
# except Exception as exception:
#     print("An error occurred : {exception}")
# finally:
#     f.close()


# Two ways to create a new file

# Opens a file for writing, also creates the file if it doesn't exist
f = open("names_list.txt", "w")
f.close()

# Creates a file, but returns an error if the file already exists
if not os.path.exists("dave.txt"):
    f = open("dave.txt", "x")
    f.close()
else:
    print("The file already exists")


# Delete a file

# Avoid an error if the file doesn't exist
if os.path.exists("dave.txt"):
    os.remove("dave.txt")
else:
    print("The file does not exist")

with open("more_names.txt") as f:
    content = f.read()
    print(content)

with open("names.txt", "w") as f:
    f.write(content)
