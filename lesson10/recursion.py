def add_one(number):
    if (number >= 9):
        return number + 1
    total = number + 1
    print(total)

    return add_one(total)


new_total = add_one(0)
print(new_total)
