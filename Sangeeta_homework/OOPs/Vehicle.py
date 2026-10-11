class Vehicle:
    def __init__(self, speed, mileage):
        self.speed  = speed
        self.mileage = mileage
    
vehicle = Vehicle("60", "miles")
print(f"mileage: {vehicle.mileage}, speed: {vehicle.speed}")