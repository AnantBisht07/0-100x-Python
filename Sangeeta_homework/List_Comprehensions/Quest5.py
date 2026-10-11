#Given nums = [1, 2, 3, 4], build a list labelling each number "even" or "odd" (use a conditional
#expression inside the comprehension).
nums = [1, 2, 3, 4]
#“Even” if condition else “odd”
new_list = ["even" if num%2 == 0 else "odd" for num in nums]
print(new_list)