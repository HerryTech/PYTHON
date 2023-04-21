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
        self.number_served = 20
        
    def describe_restaurant(self):
        print("This is a fine restaurant")
        print(f"The name of this restaurant is {self.restaurant_name}")
        print(f"{self.restaurant_name} restaurant is located all over the world")
        print(f"Our cuisine is {self.cuisine_type}")
        
        print("-" * 10)
    
    def open_restuarant(self):
        print(f"{self.restaurant_name} is opened 24hrs")
        
    def service_rendered(self, served):
        print("How many times were you served?")
        
        if served >= self.number_served:
            self.number_served += served
            print(f"We have served {self.number_served} times")
        else:
            print("Not relevant")
        
restaurant1 = Restaurant("cook_it", "French")
restaurant2 = Restaurant("eat_it", "Italian")
restaurant3 = Restaurant("the_best", "Nigerian")

restaurant1.describe_restaurant()
restaurant1.open_restuarant()
restaurant1.service_rendered(45)

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
        self.login_attempt =  0
    
    def describe_user(self):
        print(f"My name is {self.first_name} {self.last_name}")
        print(f"I am {self.age} years old")
        print(f"I live in {self.resident}")
        print(f"{self.best_food} is my best food")
        
    def increment_login_attempt(self):
        self.login_attempt += 1
        if self.login_attempt == 1:
            print(f"You have logged in {self.login_attempt} time")
        else:
            print(f"You have logged in {self.login_attempt} times")
        
    def reset_login_attempt(self):
        self.login_attempt = 0
        print(f"Your login attempt has been reset to {self.login_attempt}")
            
user1 = User("Ini", "Blessing", 25, "Canada", "Rice and beans")
user2 = User("Heritage", "Thomas", 23, "Nigeria", "Pounded yam")

user1.describe_user()
print("-" * 10)
user1.increment_login_attempt()
user1.increment_login_attempt()
user1.increment_login_attempt()
user1.increment_login_attempt()
user1.increment_login_attempt()
user1.reset_login_attempt()
user1.increment_login_attempt()
user1.increment_login_attempt()
print("-" * 10)
user2.describe_user()

class Car:
    """An attempt to model a car"""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 12
        
    def descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    
    def read_odometer(self):
        print(f"{self.make} car has {self.odometer_reading} miles on it")
        
    def update_odometer(self, mileage):
        #self.odometer_reading = mileage
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        self.odometer_reading += miles
    
my_car = Car("audi", "a4", 2019)
print(my_car.descriptive_name())
my_car.odometer_reading = 23_500 #modifying attribute directly
my_car.read_odometer()

my_car.update_odometer(12) #modifying attribute through a method
my_car.read_odometer()

print("-" * 10)

my_used_car = Car("Subaru", "outback", 2015)
print(my_used_car.descriptive_name())
my_used_car.update_odometer(30)
my_used_car.read_odometer()

print("-" * 10)
my_used_car.increment_odometer(50)
my_used_car.read_odometer()
     