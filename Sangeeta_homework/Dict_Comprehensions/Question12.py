#Given two lists keys = ["a", "b", "c"] and values = [1, 2, 3], build a dict pairing them.
keys = ["a", "b", "c"]
values = [1, 2, 3]
#mappings = {key : val for key in keys for val in values}
mappings = {key : val for key, val in zip(keys, values)}
print(mappings)