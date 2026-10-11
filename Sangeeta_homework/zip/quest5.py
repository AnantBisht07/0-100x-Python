#Given prices = [10,500] and qtys = [3,2], build a list of the total cost per item (price times quantity)
prices = [10,500] 
qtys = [3,2]
total_cost = [price*qty for price, qty in zip(prices, qtys)]
print(f"total cost for each item {total_cost}")