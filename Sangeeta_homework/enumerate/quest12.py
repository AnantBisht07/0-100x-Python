#Q12. Given nums = [10,25,30,45], build a list of the INDEXES of all numbers greater than 20
nums = [10,25,30,45]
positions = [i for i, n in enumerate(nums) if n > 20]
print(positions)