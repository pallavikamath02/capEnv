
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
        self.running = False
    def start(self):
        self.running = True
    def stop(self):
        self.running = False
    def __repr__(self):
        state = "running" if self.running else "stopped"
        return f"Engine({self.horsepower}HP, {state})"
class Car:
    def __init__(self, make, horsepower):
        self.make = make
        self.engine = Engine(horsepower)
    def start(self):
        self.engine.start()
    def stop(self):
        self.engine.stop()
    def status(self):
        return f"{self.make} -> {self.engine}"
my_car = Car("Toyota", 150)
print(my_car.status())
my_car.start()
print(my_car.status())
my_car.stop()
print(my_car.status())