'''
Count how many coordinate tuples in points = [(0, 0), (1, 2), (0, 5), (3, 0)] lie on an axis (that is, x
is 0 OR y is 0).

'''
points = [(0, 0), (1, 2), (0, 5), (3, 0)]
count = 0
for x, y in points:
    if x == 0 or y == 0:
        count += 1

print(count)

##using shortcut
on_axis = sum(1 for x, y in points if x == 0 or y == 0)
print(on_axis)