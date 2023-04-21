from car import Car
from car import ElectricCar as EC
from car import Battery

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
my_tesla = EC("tesla", "roadster", 2019)
print(my_tesla.descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()