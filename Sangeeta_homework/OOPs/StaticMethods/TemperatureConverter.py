class TemperatureConvertor:
    @staticmethod
    def c_to_far(c):
        return (c * 9 / 5) + 32

c = 100
print(f"Cel to Far is {TemperatureConvertor.c_to_far(c)}")

