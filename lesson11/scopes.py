name = "Dave"   # global scope
count = 1       # global scope

# def greeting():
#     print(f"Hello {name}")  # prints global scope


def greeting(name):
    color = "blue"
    print(f"Hello {name}")  # prints global scope
    print(f"Color is {color}")  # prints local scope


greeting("Marc")

# Error, variable color does not exist in this scope
# print(f"Color is {color}")


def goodbye():
    another_color = "red"
    # count += 1          # Unable to change global scope variable
    # global count
    # count += 1          # Works
    count = 2
    print(f"Goodbye : count is {count}")    # Prints local scope

    def inside():
        print(f"Inside the greeting function, color is {another_color}")

    greeting("Marc")    # Works as greeting is in the global scope
    inside()            # Works as inside is in the local scope


goodbye()
