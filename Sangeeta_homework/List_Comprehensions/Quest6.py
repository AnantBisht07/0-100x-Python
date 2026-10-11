#Build a list of all pairs (x, y) where x and y each come from [1, 2, 3], but only keep pairs where x is less than y
nums = [1, 2, 3]
pairs = [(x,y) for x in nums for y in nums if x < y]
print(pairs)