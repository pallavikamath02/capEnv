class Animal:
    def sound(self):
        return "Some generic animal sound"
    
class Dog(Animal):
    def sound(self):
        return "Bark"   
class Cat(Animal):
    def sound(self):
        return "Meow"   
    
ani=[Dog(), Cat(), Animal()]
for animal in ani:
    print(animal.sound())