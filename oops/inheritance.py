class dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    def display(self):
        print(f"Name: {self.name}, Breed: {self.breed}, Age: {self.age}")

#single inheritence        
class puppy(dog):
    def sound(self):
        print("Puppy sounds") 

#multilevel inheritence
class GuideDog(puppy):
    def guide(self):
        print(f"{self.name} Guiding the way!")
        
#mutliple inheritence
class friendly:
    def greet(self):
        print(f"{self.name} is friendly!")


class TherapyDog(dog, friendly):
    def sound(self):
        print("therapyDog barks")
        
# Creating objects
puppy1=puppy("Buddy", "Golden Retriever", 1)
puppy1.display()
puppy1.sound()

guide_dog1=GuideDog("Max", "German Shepherd", 3)
guide_dog1.display()
#guide_dog1.sound()
guide_dog1.guide()
    