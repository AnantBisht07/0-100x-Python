#Given a list of (item, price) tuples, return a single tuple (cheapest_item, dearest_item) by name.
items = [("pen", 10), ("bag", 500), ("book", 120)]
cheapest_item = min(items, key=lambda item: item[1])[0]
dearest_item = max(items, key=lambda item: item[1])[0]
print((cheapest_item, dearest_item))