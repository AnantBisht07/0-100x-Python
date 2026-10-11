'''
Given prices = {"apple": 50, "banana": 20, "milk": 60}, apply a 10% discount to every value
and produce a new dict.
'''
prices = {"apple": 50, "banana": 20, "milk": 60}
discounted_prices = {}
for item, price in prices.items():
    discount = (price * 10/100)
    print(discount)
    discounted_prices[item] = price - discount
#discounted = {item: p * 0.9 for item, p in prices.items()}
print(discounted_prices)