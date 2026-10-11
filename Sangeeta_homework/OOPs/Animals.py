class Animal:
    def speak(self):
        print("Calling Base class: Animal sound")

class Dog(Animal):
    def speak(self):
        print("Calling Dog: OOF OOF")

class Cat(Animal):
    def speak(self):
        print("Calling Cat: Meow Meow")

aniamals = [Cat(), Dog()]
for animal in aniamals:
    animal.speak()

