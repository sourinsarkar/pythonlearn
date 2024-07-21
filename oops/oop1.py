class Car:
    def __init__(self, userbrand, usermodel):
        self.brand = userbrand
        self.model = usermodel

class ECar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize

myTesla = ECar("Tesla", "Model S", "85kwh")
print(myTesla.model)
print(myTesla.batterySize)

# my_car = Car("Kia", "Seltos")
# print(my_car.brand)
# print(my_car.model)

# new_car = Car("TVS", "Jupiter");
# print(new_car.brand)
# print(new_car.model)