class Product:
    def __init__(self, product, price, category):
        self.product = product
        self.price = price
        self.category = category
    
    def __str__(self):
        return f"{self.product} {self.category} ({self.price})"

product = Product("MacBook", 1500, "Laptop")
print(product)