from abc import ABC, abstractmethod

class Greet(ABC):
    @abstractmethod
    def say_hello(self):
        pass
    
class EnglishGreet(Greet):
    def say_hello(self):
        return "Hello!"

g=EnglishGreet()
print(g.say_hello())    