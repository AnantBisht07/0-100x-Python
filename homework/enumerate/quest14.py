#Q14. Given nums = [5,6,7,8,9], build a new list where every value at an EVEN index is replaced with 0, and odd-index values stay.
nums = [5,6,7,8,9]
revised_list = [ 0 if i % 2 == 0 else v for i, v in enumerate(nums)]
#result = [0 if i % 2 == 0 else v for i, v in enumerate(nums)]
print(revised_list)