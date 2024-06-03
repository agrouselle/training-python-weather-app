from functools import reduce
def squared(num): return num * num
# squared = lambda num: num * num


print(squared(2))


def add_two(num): return num + 2
# add_two = lambda num: num + 2


print(add_two(12))


def sum_total(a, b): return a + b
# sum = lambda a, b: a + b


print(sum_total(10, 8))

#####################################


def funcBuilder(x):
    return lambda num: num + x


addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(5))
print(addTwenty(5))

#####################################

numbers = [3, 7, 12, 18, 20, 21]
squared_nums = map(lambda num: num*num, numbers)

print(list(squared_nums))

#####################################

numbers = [1, 2, 3, 4, 5, 1]
total = reduce(lambda acc, curr: acc + curr, numbers)
print(total)

#####################################

print(sum(numbers))
