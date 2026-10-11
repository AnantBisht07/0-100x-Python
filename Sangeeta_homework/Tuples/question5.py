'''
Given data = [("a", 1), ("b", 2), ("c", 3)], split it back into two separate tuples: one of all the letters,
one of all the numbers. (This is 'unzipping'.)
zipping -> list(zip(tuple1, tuple2))
unzipping -> zip(*listoftuples)
'''
##method 1
data = [("a", 1), ("b", 2), ("c", 3)]
letters = tuple(x for x, y in data)
numbers = tuple(y for x,y in data)
print(letters)
print(numbers)

#using unzipping
letters, numbers = zip(*data)
print(letters)
print(numbers)