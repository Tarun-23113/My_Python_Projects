class Vehicle:
    def __init__(self, make, model, year, size=10):
        self.make = make
        self.model = model
        self.year = year
        self.size = size
    
    def start_engine(self):
        print("grr.....    Engine Started")

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors
    
    def drive(self):
        print(f"Driving the {self.make}, {self.model}")

class MotorCycle(Vehicle):
    def __init__(self, make, model, year, has_sidecar):
        super().__init__(make, model, year)
        self.has_sidecar = has_sidecar
    
    def start_engine(self):
        print("MotorCycle Engine Roared to Life!")
    
    def wheelie(self):
        print(f"Doing a wheelie on the {self.make} {self.model}!")

car1 = Car("Mustang", "G Series", "1979", 4)
car1.drive()
car1.start_engine()
print(car1.size)

bike1 = MotorCycle("Apache", "RTR 350", "2010", False)
bike1.start_engine()
bike1.wheelie()
print(bike1.size)