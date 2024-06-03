# while looping

value = 0
while value <= 10:
    value = value + 1
    if value == 5:
        continue
    print(value)
else:
    print("Done. Value is now " + str(value))

print('')

# For looping

names = ["Plant", "Page", "Coverdale", "Bonham"]

for name in names:
    print(name)
else:
    print("Done.")

print('')

for x in "Mississippi":
    print(x)

print('')

for name in names:
    if name == "Page":
        break
    print(name)

print('')

for name in names:
    if name == "Page":
        continue
    print(name)

print('')

for x in range(4):
    print(x)

print('')

for x in range(2, 4):
    print(x)

print('')

for x in range(5, 101, 5):
    print(x)
else:
    print("Done")


names = ["Plant", "Page", "Coverdale", "Bonham"]
actions = ["walks", "talks", "runs"]

# for name in names:
#     for action in actions:
#         print(name + " " + action)

for action in actions:
    for name in names:
        print(name + " " + action)
