class NotCoolException(Exception):
    pass


try:
    print("Starting...")
    x = 2
    # print(x)
    # x / 0
    # if not type(x) is str:
    #     raise TypeError("x must be a string")

    # raise Exception("This is a custom exception")
    raise NotCoolException("This is not cool, man!")
except NameError:
    print("Something went wrong with a variable name")
except ZeroDivisionError:
    print("You can't divide by zero!")
except Exception as exception:
    print("Something went wrong, I dunno what")
    print(exception)
    print(type(exception))
else:
    print("Nothing went wrong")
finally:
    print("This will always run")
