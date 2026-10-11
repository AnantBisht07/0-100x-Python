#Unzip pairs = [("a",1),("b",2),("c",3)] back into two separate tuples using zip.
#unzip use *
pairs = [("a",1),("b",2),("c",3)]
letters, nums = zip(*pairs)
print(letters)
print(nums)