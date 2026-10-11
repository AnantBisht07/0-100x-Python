#From items = ["a","b","c"], build a list of "index: value" strings using enumerate inside a list comprehension.
#enumerate(iterable, start=0)
items = ["a","b","c"]
index_val = {index: val for index, val in enumerate(items, start=1)}
print(index_val)
#['0: a', '1: b', '2: c']