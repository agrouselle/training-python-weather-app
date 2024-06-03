users = ['Dave', 'John', 'Sarah']
data = ['Dave', 42, True]
empty = []

print('Dave' in empty)
print(users[0])
print(users[-1])
print(users.index("Sarah"))
print(users[0: 2])
print(users[1:])
print(users[-3:-1])

print(len(users))
users.append("Jane")
print(users)

users += ['Jason']
print(users)

users.extend(['Robert'])
print(users)

users.insert(0, "Bob")
print(users)

users[2:2] = ['Eddie', 'Marc']
print(users)

users.remove('Bob')
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del users
# print(users)    # Error

print(data)
data.clear()
print(data)

users[1:2] = ['dave']
users.sort()
print(users)        # 'dave' gets sorted to the last element

users.sort(key=str.lower)
print(users)


nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()  # create a copy
# numscopy = list(nums)  # create a copy
# numscopy = nums[:]  # create a copy
print(numscopy)
print(type(numscopy))
