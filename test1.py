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
# #     print(i)
#
# my_friends_list = [('Sanya', 21),("Danya", 22),("Bogdan", 13), ('oleg',13)]
#
# func = lambda my_friends_list: my_friends_list[1] >= 18
#
# allow_to_drink = filter(func, my_friends_list)
#
# for i in allow_to_drink:
#     print(i)

import time
# import threading
from multiprocessing import cpu_count, Process

def countdown(arg):
    number = 0
    while number <= arg:
        number += 1

def main():
    a = Process(target=countdown(250000000))
    b = Process(target= countdown(250000000))
    c = Process(target= countdown(250000000))
    d = Process(target= countdown(250000000))

    time1 = time.perf_counter()
    a.start()
    b.start()
    c.start()
    d.start()
    d.join()
    a.join()
    b.join()
    c.join()
    time2 = time.perf_counter()
    result = (time2 - time1)
    print(result)

if __name__ == '__main__':
    main()







# def timer():
#     print()
#     print()
#     counter = 0
#     while True:
#         time.sleep(1)
#         counter += 1
#         print(f'you have been logged for {counter} seconds')
#
#
# x = threading.Thread(target=timer, daemon=True)
#
#
# x.start()
#
# rabor = input('wannaaaa')