class Circle:
    @staticmethod
    def circlearea(radius):
        return 3.14 * radius * radius
    
    @staticmethod
    def drawcircle(area):
        for i in range(1, area):
            print("*", end="")

area = Circle.circlearea(10)
print(f"Area of circle is {area}")
#Circle.drawcircle(area)