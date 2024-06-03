def hello_world():
    print("Hello world")


hello_world()


def sum(num1=0, num2=0):
    if (type(num1) is not int or type(num2) is not int):
        return 0
    return num1 + num2


total = sum(1, 2)
print(total)

str = sum("a", 2)
print(str)

# str = sum()  # missing arguments error if no default values set
total = sum()
print(total)


# Multiple arguments
def multiple_items(*args):
    print(args)
    print(type(args))


multiple_items("a", "b", "c")


def multiple_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


multiple_named_items(first="a", last="c")
