class MathHelper:
    @staticmethod
    def add(n1, n2):
        return n1 + n2
    
    @staticmethod
    def subtract(n1, n2):
        return n1 - n2
    
    @staticmethod
    def multiply(n1, n2):
        return n1 * n2

result = MathHelper.add(2, 6)
print(result)
result = MathHelper.add(6, 1)
print(result)
result = MathHelper.multiply(19, 10)
print(result)