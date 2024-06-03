import math

# String data type

# Literal assignment
first = "Dave"
last = "Smith"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructor function
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatenation
fullname = first + ' ' + last
print(fullname)
fullname += '!'
print(fullname)

# Casting
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)

# Multiple lines
multiline = '''
Hey, how you doin'?

I was just checking in.
                            All good?
'''
print(multiline)

# Escaping special characters
sentence = 'I\'m back at work\tHey!\n\nWhere\'s this at\\located?'
print(sentence)


# String Methods
print(first)
print(first.lower())
print(last.upper())
print(fullname.capitalize())
print(multiline.title())
print(multiline.replace("good", "okay"))
print(len(multiline))

# Build a menu
title = "menu".upper()
print(title.center(24, "="))
print("Coffee".ljust(20, '.') + "$1".rjust(5))
print("Tea".ljust(20, '.') + "$1.50".rjust(5))
print("Water".ljust(20, '.') + "$0.50".rjust(5))
print(' ')

# String index values
print(first)
print(first[1])     # Second letter
print(first[-1])    # Last letter
print(first[0:3])   # First three letters
print(first[1:-1])  # Everything but the first and last letter
print(first[1:])    # Everything after the first letter
print(' ')

# Some methods return boolean data
print(first.startswith("D"))
print(first.endswith("e"))
print(' ')

# Boolean data type
print(type(True))
print(type(False))
print(isinstance(True, bool))
print(isinstance(False, bool))
print(isinstance(True, int))
print(isinstance(False, int))
print(' ')

# Numeric data types
price = 100
best_price = int(80)
print(type(price))
print(isinstance(price, int))

gpa = 3.28
y = float(1.28)
print(type(gpa))
print(isinstance(gpa, float))

# Complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)
print(' ')

# Built-in math functions
print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))
print(' ')

# Math library functions
print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))
print(' ')

# Casting a string to a number
zipcode = "10001"
zipcode_value = int(zipcode)
print(type(zipcode_value))
print(' ')
