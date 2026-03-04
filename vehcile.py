
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def start(self):
        print(f"{self.brand} is starting.")

    def stop(self):
        print(f"{self.brand} is stopping.")
class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand, speed)
        self.fuel_type = fuel_type

    def show_fuel_type(self):
        print(f"{self.brand} uses {self.fuel_type} as fuel.")
class Bike(Vehicle):
    def __init__(self, brand, speed, engine_capacity):
        super().__init__(brand, speed)
        self.engine_capacity = engine_capacity

    def show_engine(self):
        print(f"{self.brand} has an engine capacity of {self.engine_capacity} cc.")
class Truck(Vehicle):
    def __init__(self, brand, speed, load_capacity):
        super().__init__(brand, speed)
        self.load_capacity = load_capacity

    def show_load_capacity(self):
        print(f"{self.brand} has a load capacity of {self.load_capacity} tons.")
car = Car("Toyota", 120, "Gasoline")
bike = Bike("Yamaha", 100, 150)
truck = Truck("Volvo", 80, 20)
car.start()
car.show_fuel_type()
bike.start()
bike.show_engine()
truck.start()
truck.show_load_capacity()
car.stop()
bike.stop()
truck.stop()
