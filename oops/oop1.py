class Car:
    def __init__(self, userbrand, usermodel):
        self.__brand = userbrand
        self.__model = usermodel

    def get_brand(self):
        return self.__brand + '!'

    def full_name(self):
        return f"Brand: {self.__brand} \n {self.__model}"

    def fuel_type(self):
        return "Petrol or Diesel"
    
    # Marking a function with the "staticmethod" decorator tells the function that the
    # function has no dependencies of the class and can be called independently.
    # This is the way it is called: print(Car.general_disdcription())
    @staticmethod
    def general_discription():
        return "Cars on means transport."
    
    # The "property" decorator makes sure that we can access certain property only and only via
    # the function itis defined upon
    @property
    def model(self):
        return self.__model

class ECar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize
    
    def fuel_type(self):
        return "Electric Charge"

myTesla = ECar("Tesla", "Model S", "85kwh")
# print(myTesla.fuel_type())

# myCar = Car("Mahindra", "Thar")
# print(myCar.fuel_type())

# print(myCar.general_discription());
# print(Car.general_discription());

# print(myTesla.model)
# print(myTesla.batterySize)
# print(myTesla.get_brand())

# my_car = Car("Kia", "Seltos")
# print(my_car.brand)
# print(my_car.model)

# new_car = Car("TVS", "Jupiter");
# print(new_car.brand)
# print(new_car.model)

# Use of "isinstance()"
# print(isinstance(myTesla, Car))
# print(isinstance(myTesla, ECar))

class Battery:
    def battery_info(self):
        return "This is a battery."
    
class Engine:
    def engine_info(self):
        return "This is an engine."
    
class ECars(Battery, Engine, Car):
    pass

newTesla = ECars("Tesla", "Model Y");
print(newTesla.battery_info());
print(newTesla.engine_info());