class Vehicle:
    def __init__(self, car_brand, name, years: int):
        self.car_brand = car_brand
        self.name = name
        self.years = years
    def show_info(self):
        return f"mashinani modelini chiqaradi"

class Car(Vehicle):
    def show_info(self):
        return f"mashinaning brandi : {self.car_brand} \nmashinaning nomi {self.name} \nmashinaning yili : {self.years}"

class Bike(Vehicle):
    def show_info(self):
        return f" velosipedning brendi : {self.car_brand} \n velosipedning nomi { self.name} \n velosipedning yili: {self.years}"

cars = Car("Gm", "Gentera", 2018)
bikes = Bike("Trek", "Trek Domane SL6", 2023)

print(cars.show_info())
print(bikes.show_info())
