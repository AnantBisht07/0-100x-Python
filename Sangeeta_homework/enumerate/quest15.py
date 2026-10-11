#Q15. Given nums = [3,9,2,9,4], find the index of the largest value using enumerate (return the first if it repeats).
nums = [3,9,2,9,4]
best = 0
for i, n in enumerate(nums):
    if n > nums[best]:
        best = i
print(best)
