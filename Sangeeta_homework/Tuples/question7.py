'''
Given pairs = [(2, 3), (5, 1), (4, 4)], build a new list containing the product of each pair.
'''

pairs = [(2, 3), (5, 1), (4, 4)]
product = []
for x, y in pairs:
    product.append(x*y)
print(product)

#list comprehension
# ["formula" "for loop"]
product = [x*y for x, y in pairs]
print(product)