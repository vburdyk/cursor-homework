import random

class Person:
    def __init__(self, name, age, money, have_home):
        self.name = name
        self.age = age
        self.money = money
        self.have_home = have_home

    def provide_info(self):
        print(f"Привіт я {self.name}, мені {self.age} років, маю {self.money} грн, я маю будинок {self.have_home}")

    def make_money(self, salary):
        self.money += salary

    def buy_house(self, house):
        if self.money >= house.cost:
            self.money -= house.cost
            self.have_home = True

class House:
    def __init__(self, area, cost):
        self.area = area
        self.cost = cost

    def purchase_discount(self, discount):
        self.cost *= (1 - (discount/100))

class Realtor:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        Realtor.__instance = None

    def __init__(self, realtor_name, houses, discount):
        self.name = realtor_name
        self.houses = houses
        self.discount = discount

    def provide_information(self):
        for home in self.houses:
            print(f"У наявності будинок із площею {home.area} метрів квадратних та вартістю {home.cost} грн")

    def give_discount(self, house):
        house.purchase_discount(self.discount)
        print(f"Знижка на будинок {self.discount}%")

    def steal_money(self):
        if random.random() <= 0.1:
            print(f"{self.name} вкрав ваші гроші!")
            return True
        else:
            print(f"На щастя, {self.name} не вкрав ваші гроші!")
            return False

person = Person("Володя", 18, 1000, False)
house = House(40, 100)
house2 = House(30, 7000)
realtor = Realtor("Андрій", [house, house2], 10)


realtor.provide_information()
realtor.give_discount(house)
realtor.steal_money()


person.provide_info()
person.buy_house(house)
person.provide_info()
person.make_money(8000)
person.provide_info()
person.buy_house(house2)
person.provide_info()

