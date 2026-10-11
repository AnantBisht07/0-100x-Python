'''
Validated constructor helper
Build a Date class that stores day, month, and year. Add a static method is_valid(day, month, year) that returns True only if the date is sensible: month between 1 and 12, day between 1 and 31, and year positive. Then use that static method inside __init__ to reject bad dates before creating them.
'''
class DateValidator:
    def __init__(self, day, month, year):
        # use the static method to CHECK before storing
        if not DateValidator.is_valid(day, month, year):
           print("Invalid date, defaulting to 01/01/2000")
           day, month, year = 1,1,2000
        self.day = day
        self.month = month
        self.year = year
           
    @staticmethod
    def is_valid(day, month, year):
        return  1 <= month <= 12 and 1 <= day <= 31 and year > 0
        #return 1 <= month <= 12 and 1 <= day <= 31 and year > 0

    def show(self):
        print(f"{self.day:02d}/{self.month:02d}/{self.year}")

date = DateValidator(1,1,1900)
result = date.show()

#day, month, year = 1, 1, 2000

#if not Date.is_valid(day, month, year): print("Invalid date, defaulting to 01/01/2000") day, month, year = 1, 1, 2000


