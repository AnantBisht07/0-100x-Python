#Q3. Build a dict from keys = ["a","b","c"] and values = [1,2,3] using zip.
keys = ["a","b","c"]
values = [1,2,3]
new_dict = {key: val for key, val in zip(keys, values)}
print(new_dict)