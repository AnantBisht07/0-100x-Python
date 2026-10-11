'''
You have points = [(1, 2), (3, 4), (5, 6)], a list of (x, y) coordinates. Compute the sum of all x values
and the sum of all y values separately, and print them as a single (sum_x, sum_y) tuple.
'''
points = [(1, 2), (3, 4), (5, 6)]
sum_x = sum(x for x, y in points) 
sum_y = sum(y for x, y in points)
print((sum_x, sum_y))