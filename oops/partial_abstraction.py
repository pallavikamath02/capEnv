from abc import ABC,abstractmethod
class Greet(ABC):
    @abstractmethod
    def say_hello(self):
        pass
class English(Greet):
    def say_hello(self):
        return "Hello!"
g=English()
print(g.say_hello())

class Dog(ABC):
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def sound(self):
        pass
    def display_name(self):
        print(f"Dog's name is {self.name}")
class Bulldog(Dog):
    def sound(self):
        print("Woof Woof")
class Beagle(Dog):
    def sound(self):
        print("Beagle Bark")
dgs=[Bulldog("Bruno"),Beagle("Max")]
for dog in dgs:
    dog.display_name()
    dog.sound()