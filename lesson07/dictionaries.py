# Dictionaries
band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band2))


# Access items

print(band["vocals"])
print(band.get("guitar"))

# List all keys, values, and items
print(band.keys())
print(band.values())
print(band.items())

# Verify if a key exists
print("guitar" in band)
print("bass" in band)

# Change values
band['vocals'] = "Coverdale"
band.update({"bass": "JPJ"})
print(band)

# Remove items
print(band.pop("bass"))
print(band)

band['drums'] = "Bonham"
print(band)
print(band.popitem())   # Pop last items as a tuple
print(band)

# Delete items
band["drums"] = "Bonham"
del band['drums']
print(band)

band2.clear()
print(band2)
del band2
# print(band2)    # Error because band2 has been deleted

# Copy dictionaries
# band2 = band      # Create a reference
# print(band)
# print(band2)
# band2['drums'] = 'Dave'
# print(band)

band2 = band.copy()  # Create a copy
band2['drums'] = 'Dave'
print(band)
print(band2)

band2 = dict(band)  # Create a copy
band2['drums'] = 'Dave'
print(band)
print(band2)


# Nested Dictionaries
member1 = {
    "name": "Plant",
    "instrument": "vocals"
}

member2 = {
    "name": "Page",
    "instrument": "guitar"
}

band = {
    "member1": member1,
    "member2": member2
}

print(band)
print(band["member1"])
print(band["member1"]["name"])


# Sets

nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))
print(nums)
print(nums2)
print(type(nums))
print(type(nums2))

# No duplicates allowed in sets
nums = {1, 2, 3, 2}
print(nums)

# True is a duplicate of 1, False is a duplicate of 0
nums = {1, 2, 3, 2, True, False}
print(nums)

nums = {1, True, 2, 3, 2, False, 0}

# Check if a value is in a set
print(1 in nums)
print(0 in nums)
print(2 in nums)

# But you cannot refer to a element in a set by index

# Add a new element to a set
nums.add(8)
print(nums)

# Remove an element from a set
nums.remove(8)
print(nums)

morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# You can use update with lists, tuples, dictionaries, and sets

# Merge two sets to create a new set
one = {1, 2, 3}
two = {3, 4, 5}
three = one.union(two)
print(three)

# Keep only the duplicates in one set
one = {1, 2, 3}
two = {3, 4, 5}
one.intersection_update(two)
print(one)

# Keep everything except the duplicates in one set
one = {1, 2, 3}
two = {3, 4, 5}
one.symmetric_difference_update(two)
print(one)
