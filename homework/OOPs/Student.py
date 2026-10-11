class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  
        sum(self.marks)

    
    def average(self):
        return sum(self.marks)/len(self.marks)

    

s1 = Student("Sang", [78, 80, 90, 50])
print(f"{Student.average(s1)}")

