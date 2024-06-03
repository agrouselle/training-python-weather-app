person = "Dave"
coins = 3

message = person + " has " + str(coins) + " coins."
print(message)

message = "%s has %s coins." % (person, coins)
print(message)

message = "{} has {} coins.".format(person, coins)
print(message)

message = "{1} has {0} coins.".format(coins, person)
print(message)

message = "{person} has {coins} coins.".format(coins=coins, person=person)
print(message)

player = {'person': 'Dave', 'coins': 3}
message = "{person} has {coins} coins.".format(**player)
print(message)

# f-strings

message = f"{person} has {coins} coins."
print(message)

message = f"{person.lower()} has {2*5} coins."
print(message)

message = f"{player['person']} has {player['coins']} coins."
print(message)

message = f"{player['person']} has {player['coins']} coins."
print(message)

# Formatting options

num = 10
print(f"2.25 times {num} is {2.25 * num:.2f}")

for num in range(1, 11):
    print(f"2.25 times {num} is {2.25 * num:.2f}")

for num in range(1, 11):
    print(f"{num} divided by 4.52 is {num / 4.52:.2%}")
