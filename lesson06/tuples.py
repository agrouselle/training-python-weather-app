# Tuples are list that cannot be changed
mytuple1 = tuple(('Dave', 42, True))
print(mytuple1)
print(type(mytuple1))


mytuple2 = (1, 4, 8, 12)        # Packing a tuple
# mytuple2.append('Neil')       # Error
print(mytuple2)
print(type(mytuple2))

list = list(mytuple2)
list.append('Neil')
mytuple3 = tuple(list)
print(mytuple3)

(one, *two, three) = mytuple2      # Unpacking a tuple
print(one)
print(two)
print(three)
