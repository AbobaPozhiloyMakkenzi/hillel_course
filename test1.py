# from abc import ABC, abstractmethod
# class vehicle(ABC):
#     @abstractmethod
#     def ride(self):
#         pass
# class car(vehicle):
#     def ride(self):
#         print('the car is driving')
#
# class morotbike(vehicle):
#     pass
# car = car()
# bike = morotbike()

element = input('Bring smth in')

def multiply(element):
    return int(element)*5
def shout(element):
    return element.upper()

def some_element(func):
    res = func(element)
    return res
try:
    print(some_element(multiply))
except:
    print(some_element(shout))

# def multiply(x):
#     def myltiply_on(y):
#         res = y*x
#         return res
#     return myltiply_on
#
# first_data = multiply(100)
#
# print(first_data(5))

