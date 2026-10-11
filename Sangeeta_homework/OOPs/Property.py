class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    @property
    def area(self):
        return self.width * self.height #computed, never stored
    
r = Rectangle(5, 5)
print(r.area) # No brackets, used as an attribute