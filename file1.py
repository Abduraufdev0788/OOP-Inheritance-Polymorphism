class Animal:
    def speak(self):
        return "Bu hayvon nimadir dedi"

class Dog(Animal):
    def speak(self):
        return "Vov-vov!"

class Cat(Animal):
    def speak(self):
        return "Miyov!"
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())
