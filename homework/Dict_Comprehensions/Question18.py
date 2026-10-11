#Given d = {"name": "priya", "city": "delhi"}, build a new dict with all the keys in uppercase (values unchanged).
d = {"name": "priya", "city": "delhi"}
upper_keys = {key.upper():val for key, val in d.items()}
print(upper_keys)