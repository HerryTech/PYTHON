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
        
    def fill_gas_tank(self):
        print(f"You can fill the gas for {self.make}")
        
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
    