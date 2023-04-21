class Dog:
    """A simple attempt to model a dog"""
    
    def __init__(self, name, age):
        """Initialize name and age attribute"""
        self.name = name
        self.age = age
        
    def sit(self):
        """Stimulate a dog sitting in response to command"""
        print(f"{self.name} is now sitting")
        
    def roll_over(self):
        """Stimulating a dog rolling over"""
        print(f"{self.name} rolled over")
        
#Making instance from a dog
my_dog = Dog("Willie", 6)

print(f"The name of my dog is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")

my_dog.sit()
my_dog.roll_over()
    