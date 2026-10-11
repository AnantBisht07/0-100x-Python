#From nums = [3, 8, 1, 6, 7, 4], build a list of only the even numbers.
nums = [3, 8, 1, 6, 7, 4]
even_nums = [num for num in nums if num%2 == 0]
print(even_nums)