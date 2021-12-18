import random
from abc import ABC, abstractmethod


def start_war(attack):
    def wrapper(self, self2):
        print(f'{self.name} готовиться ударить {self2.name}')
        attack(self, self2)
        print(f'{self.name} кинул на прогиб {self2.name}, у него осталось {self2.hp} жизни')
        if self2.hp <= 0:
            print(f'welcome to на Калыму {self.name}')
    return wrapper
class Character(ABC):

    def __init__(self, name,location, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.location = location

    @start_war
    def attack(self, self2):
        self2.hp -= self.damage

class Scout(Character):
    def __init__(self, name, location = [], hp=100, damage=10):
        super().__init__(name, location, hp, damage)
    def who_i_am(self):
        print('i am scout')
    def attack(self, self2):
        super().attack(self2)
    def blocked_hits(self):
        print('i can blocked your hits')
    def double_jump(self):
        print('happen double jump')
    def gangsta_man(self):
        print('yo man i am gangsta')
    def where_characters(self, location):
        self.location = location


    @staticmethod
    def loc(object):
        if object in object.location:
            print(object.location.index(object))
class Medic(Character):
    def __init__(self, name, hp=100, damage=10):
        super().__init__(name, hp, damage)
    def who_i_am(self):
        print('i am medic')
    def attack(self, self2):
        super().attack(self2)
    def help_my_friends(self, self2):
        self2.hp +=30
    def impove_health(self):
        self.hp = 100

    def staff(self):
        print('hey bro i have not morphine')
    def treatment(self):
        print('you not my friend, I will not treat you')

class Boss:
    def __init__(self, name, hp= 1000, damage=40):
        self.hp = hp
        self.damage = damage

    def attack(self, self2):
        super().attack(self2)
    def who_i_am(self):
        print('i am best of the best in this game')
    def teleport(self):
        print('happen teleport me, sorry you cant kill me')
    def treate_me(self):
        self.hp += 200
    def super_hit(self,self2):
        if self2.hp <= 70:
            if random.random() == 1:
                print('на пять баллов произошел прогиб')
                self2.hp = 0
                print(f'{self2.name} случайно умер,  {self.name} не в чем не виноват ')
            else:
                print('прилетела пощечина, но жить можно')
                self2.hp -= self.damage
class Spy:
    def __init__(self, name, hp=100, damage=20):
        super().__init__(name, hp, damage)

    def __Spy_method(self):
        print('i am spy')

    def attack(self, self2):
        super().attack(self2)
    def invisible(self):
        print("you cant see me")

    def backstab(self, self2):
        self2.hp = 0
    def i_am_not(self):
        print('i am not spy')
    def reincarnation(self):
        print('i am medic !!')

scout_1 = Scout('Pablo', ['loc1', 'loc2'])
scout_2 = Scout('Niaz')
al_characters = [scout_1,scout_2]
scout_2.where_characters(al_characters)
Scout.loc('loc2')

