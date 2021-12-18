from abc import ABC, abstractmethod
class Transport(ABC):
    def __init__(self, weight, speed, gas_tank, capacity ):
        self.weight = weight
        self.speed = speed
        self.gas_tank = gas_tank
        self.capacity = capacity
        self.people = []
    @abstractmethod
    def add_passenger(self, person):
        pass

    @abstractmethod
    def exit(self,person):
        pass
    @staticmethod
    def driver(name):
        print(f'за рулем сидит {name}')

class Car(Transport):
    def __init__(self, weight, speed, gas_tank, capacity, plays_kid ):
        self.weight = weight
        self.speed = speed
        self.gas_tank = gas_tank
        self.capacity = capacity
        self.people = []
        self.plays_kid = plays_kid
    def __str__(self):
        return f'вес машины- {self.weight}, скорость машины {self.speed}, бензобак -  {self.gas_tank}, места пассажирские {self.capacity}, люди в машине- {self.people}, места для детей {self.plays_kid}'

    def add_passenger(self, person):
        if len(self.people) < self.capacity:
            self.people.append(person)
        else:
            print('You shall not pass')

    def exit(self,person):
        if len(self.people) ==0:
            print('Здесь людей нет ')
        else:
            self.people.remove(person)

    def child_seat(self):
        if self.plays_kid < 4:
            self.plays_kid +=1
        else:
            print('все занято детскими креслами')

class Bike(Transport):
    def add_passenger(self, person):
        if len(self.people) < self.capacity:
            self.people.append(person)
        else:
            print('You shall not pass')

    def exit(self,person):
        if len(self.people) ==0:
            print('Здесь людей нет ')
        else:
            self.people.remove(person)
    def fast_drive(self):
        print('проехать между рядами')

    def __str__(self):
        return f" вес машины - {self.weight}, скорость машины {self.speed}, бензобак - {self.gas_tank}, вместимость машины- {self.capacity}, люди в машине -{self.people},"


class Bus(Transport):
    def __init__(self,weight, speed, gas_tank, capacity,plays_for_things, max_things=70):
        self.weight = weight
        self.speed = speed
        self.gas_tank = gas_tank
        self.capacity = capacity
        self.people = []
        self.plays_for_things = []
        self.max_things = max_things
    def __str__(self):
        return f" вес машины - {self.weight}, скорость машины {self.speed}, бензобак - {self.gas_tank}, вместимость машины- {self.capacity}, люди в машине -{self.people}, места для вещей {self.plays_for_things}, максимальная вместимость вещей {self.max_things}"
    def add_passenger(self, person):
        if len(self.people) < self.capacity:
            self.people.append(person)
        else:
            print('You shall not pass')

    def exit(self,person):
        if len(self.people) ==0:
            print('Здесь людей нет ')
        else:
            self.people.remove(person)
    def append_things(self, thing):
        if len(self.plays_for_things) < self.max_things:
            self.plays_for_things.append(thing)
        else:
            print('места нет ')

class Truck(Transport):
    def add_passenger(self, person):
        if len(self.people) < self.capacity:
            self.people.append(person)
        else:
            print('You shall not pass')

    def exit(self,person):
        if len(self.people) ==0:
            print('Здесь людей нет ')
        else:
            self.people.remove(person)
    def Puton(self, pesok):
        self.weight += pesok
        print(f'погрузили {pesok} кг песка')
    def __str__(self):
        return f" вес машины - {self.weight}, скорость машины {self.speed}, бензобак - {self.gas_tank}, вместимость машины- {self.capacity}, люди в машине -{self.people},"

car = Car(12, 123, 124, 124, 0)
car.add_passenger('Tom')
truck = Truck(12,41,63,423)
truck.Puton(150)
bus  = Bus(213,42,125,123,124)
bus.append_things('рюкзак')
print(car.people)