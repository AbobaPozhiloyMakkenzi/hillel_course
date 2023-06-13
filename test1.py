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

# element = input('Bring smth in')
#
# def multiply(element):
#     return int(element)*5
# def shout(element):
#     return element.upper()
#
# def some_element(func):
#     res = func(element)
#     return res
# try:
#     print(some_element(multiply))
# except:
#     print(some_element(shout))

# def multiply(x):
#     def myltiply_on(y):
#         res = y*x
#         return res
#     return myltiply_on
#
# first_data = multiply(100)
#
# print(first_data(5))

# numbers = [1,3,5,7,9,12]
# x = 5
# res = map(lambda numbers:numbers*5, numbers)
# for i in res:
#     print(i)

my_friends_list = [('Sanya', 21),("Danya", 22),("Bogdan", 13), ('oleg',13)]

func = lambda my_friends_list: my_friends_list[1] >= 18

allow_to_drink = filter(func, my_friends_list)

for i in allow_to_drink:
    print(i)
