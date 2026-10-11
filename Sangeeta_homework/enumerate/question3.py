#Given nums = [5,6,7,8,9], build a new list where every value at an EVEN index is replaced with 0, and odd-index values stay.
#output [0, 6, 0, 8, 0]
nums = [5,6,7,8,9] 
even_index_values = [0 if index%2 == 0 else num for index, num in enumerate(nums)]
print(even_index_values)