capital = "Topeka"


def present():
    print(f"Welcome to Kansas! Capital is {capital}")


# Runs the method only when the module is run directly, not when it is imported.
if __name__ == "__main__":
    present()
