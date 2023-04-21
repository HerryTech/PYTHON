from car import Car

class Battery:
    def __init__(self, battery_size = 75):
        self.battery_size = battery_size
        
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery")
        
    def get_range(self):
        if self.battery_size <= 75:
            range = 260
            print(f"This car can go about {range} miles on a full charge.")
        else:
            range = 315
            print(f"This car can go about {range} miles on a full charge.")
            
    
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
        
        
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank")
    
my_car = Car("audi", "a4", 2019)
print(my_car.descriptive_name())
my_car.odometer_reading = 23_500 #modifying attribute directly
my_car.read_odometer()

my_car.update_odometer(12) #modifying attribute through a method
my_car.read_odometer()
my_car.fill_gas_tank()

print("-" * 10)

my_used_car = Car("Subaru", "outback", 2015)
print(my_used_car.descriptive_name())
my_used_car.update_odometer(30)
my_used_car.read_odometer()

print("-" * 10)
my_used_car.increment_odometer(50)
my_used_car.read_odometer()
my_used_car.fill_gas_tank()

print("-" * 10)
my_tesla = ElectricCar("tesla", "model 5", 2019)
print(my_tesla.descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()