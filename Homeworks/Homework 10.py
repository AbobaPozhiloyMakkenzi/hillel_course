#Створіть клас "Транспортний засіб" та підкласи "Автомобіль", "Літак", "Корабель", наслідувані від "Транспортний засіб". Наповніть класи атрибутами на свій розсуд.
#Створіть обʼєкти класів "Автомобіль", "Літак", "Корабель".

from abc import abstractmethod
class Transport:

    def __init__(self,make,year, material,opinion):
        self.Alive = False
        self.make = make
        self.year = year
        self.material = material
        self.opinion = opinion
    @abstractmethod
    def move(self):
        print('this is moving!')

    def broken(self):
        print('this is broken')

    def accelerate(self):
        return 'we are accelerating'


class Car(Transport):

    Wheels = 4

    def move(self):
        print('The car is driving')

    def beep(self):
        print('beep, beep,bbeeeeeeep!')

    def speeding_ticket(self):
        print('pay a fine then!')


car1 = Car("Ukrainian", 2005, 'steel', 'good')


class Airplane(Transport):
    Wheels = 0
    Wings = 2

    def move(self):
        print('We are flying')

    def landing(self):
        print('We are landing')

    def depart(self):
        print('We are taking off')


Plane1 = Airplane("Ukrainian",1976, 'alluminium', 'old and shaggy')


class Boat(Transport):
    Wheels = 1  #steering weheel LMAO

    def move(self):
        print('we are sailing!')

    def fishing(self):
        print('We are fishing')

    def meeting_iceberg(self):
        print('WTF ISSS DAT OVER THERE???')


boat = Boat('Ukrainian', 2222, 'Titianium', 'Klichko Boat')

