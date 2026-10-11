#Given nums = {"a": 10, "b": 15, "c": 20, "d": 7}, build a new dict keeping only the items whose
#value is even.
nums = {"a": 10, "b": 15, "c": 20, "d": 7}
even_dict = {key:val for key, val in nums.items() if val % 2 == 0}
print(even_dict)