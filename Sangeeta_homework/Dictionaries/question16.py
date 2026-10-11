'''
Given a dict stock = {"pen": 3, "book": 0, "bag": 5, "ink": 0}, print a list of only the items that
are out of stock (value 0).
Docstring for DataStructures.Dictionaries.question16
'''
stock = {"pen": 3, "book": 0, "bag": 5, "ink": 0}
for item, quantity in stock.items():
    if quantity == 0:
        print(f"{item} is out of stock")