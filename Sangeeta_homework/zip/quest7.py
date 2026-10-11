#Q7. Given a = [3,8,2] and b = [5,1,9], build a list holding the larger value at each position.
a = [3,8,2] 
b = [5,1,9]
larger_val = [max(x, y) for x, y in zip(a,b)]
print(larger_val)