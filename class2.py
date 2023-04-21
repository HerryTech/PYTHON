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
        
#Making instances from the class
my_dog = Dog("Willie", 6)
your_dog = Dog("Lucy", 3)

print(f"The name of my dog is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")
my_dog.sit()
my_dog.roll_over()

print("-" * 10)

print(f"The name of your dog is {your_dog.name}")
print(f"Your dog is {your_dog.age} years old")
your_dog.sit()
your_dog.roll_over()

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print("This is a fine restaurant")
        print(f"The name of this restaurant is {self.restaurant_name}")
        print(f"{self.restaurant_name} restaurant is located all over the world")
        print(f"Our cuisine is {self.cuisine_type}")
        
        print("-" * 10)
    
    def open_restuarant(self):
        print(f"{self.restaurant_name} is opened 24hrs")
        
restaurant1 = Restaurant("cook_it", "French")
restaurant2 = Restaurant("eat_it", "Italian")
restaurant3 = Restaurant("the_best", "Nigerian")

restaurant1.describe_restaurant()
restaurant1.open_restuarant()

print("-" * 10)

restaurant2.describe_restaurant()
restaurant2.open_restuarant()

print("-" * 10)

restaurant3.describe_restaurant()
restaurant3.open_restuarant()


class User:
    def __init__(self, first_name, last_name, age, resident, best_food):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.resident = resident
        self.best_food = best_food
    
    def describe_user(self):
        print(f"My name is {self.first_name} {self.last_name}")
        print(f"I am {self.age} years old")
        print(f"I live in {self.resident}")
        print(f"{self.best_food} is my best food")
        
user1 = User("Ini", "Blessing", 25, "Canada", "Rice and beans")
user2 = User("Heritage", "Thomas", 23, "Nigeria", "Pounded yam")

user1.describe_user()
print("-" * 10)
user2.describe_user()

     