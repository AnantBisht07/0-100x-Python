#Q11. From items = ["a","b","c"], build a list of "index: value" strings using enumerate inside a list comprehension.
items = ["a","b","c"]
items_list = [f"{index}: {val}" for val, index in enumerate(items)]
print(items_list)