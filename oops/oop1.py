class Car:
    def __init__(self, userbrand, usermodel):
        self.__brand = userbrand
        self.model = usermodel

    def get_brand(self):
        return self.__brand + '!'

    def full_name(self):
        return f"Brand: {self.__brand} \n {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"
    
    # @staticmethod
    def general_discription():
        return "Cars on means transport."

class ECar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize
    
    def fuel_type(self):
        return "Electric Charge"

myTesla = ECar("Tesla", "Model S", "85kwh")
print(myTesla.fuel_type())

myCar = Car("Mahindra", "Thar")
print(myCar.fuel_type())

# print(myCar.general_discription());
print(Car.general_discription());

# print(myTesla.model)
# print(myTesla.batterySize)
# print(myTesla.get_brand())

# my_car = Car("Kia", "Seltos")
# print(my_car.brand)
# print(my_car.model)

# new_car = Car("TVS", "Jupiter");
# print(new_car.brand)
# print(new_car.model)