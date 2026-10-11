#Given nums = [10,25,30,45], build a list of the INDEXES of all numbers greater than 20.
#enumerate(iterable, start=0)
nums = [10,25,30,45]
greater_than_20 = [index for index, num in enumerate(nums, start=1) if num > 20]
print(greater_than_20)