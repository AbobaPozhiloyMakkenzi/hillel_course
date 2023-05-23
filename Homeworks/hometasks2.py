#
# age = int(input('Please, tell your age, darling'))
# if age<0:
#     print('stop living in the past')
# elif len(str(age)) > 2:
#      print('seriously, stop it')
# elif age<6:
#     print('where are your parents')
# elif str(age).find('7')!=-1:
#     print('you are lucky today')
# elif age <16:
#     if age>6:
#         print('this film is for adults only')
# elif age>65:
#     print('please show your id')
# else:
#     print('there are no tikcets left')

# template = str(129)
# result = template[len(template) - 1]
# print(result)
# #
# # template = '0123456789'
# # result = template[-3]
# print(result)


# slice
# template = '0123456789'
# result = template[1:5]
# print(result)
# print(len(result))
# #
# result = template[:5]  # [0:5]
# print(result)
#
# result = template[3:]  # [3:len(template)-1]
# print(result)
#
# result = template[3:len(template)]
# print(result)
#
# result = template[:]  # [0:9]
# print(result)
#
# result = template[-3:]  # [7:9]
# print(result)
# #
# result = template[-8:-2]  # [2:7]
# print(result)
#
# result = template[1:8:3]
# print(result)
#
# result = template[9:1:-2]
# print(result)
#
# result = template[len(template)//2:]
# print(result)
# result = template[:len(template)//2]
# print(result)


# condition = None

# name = input('type your name')
# while len(name) < 6:
#     print('men are ashamed of you')
# if len(name) > 6:
#     print('who has let the black guy in?')

# Name1 = input("type your name")
# Name2 = input("and your")
# while  Name1.find('Boghdan') >= 0 and Name2.find('Dima') >= 0:
#     print('buy me a steak, moron')

# import time
#
# for i in range(10, 0, -1):
#     # print(i)
#     time.sleep(1)
# print('happy hannukah')

import time
name1 = input('give me your name')
name2 = input('and your')
moneyway = ' '
if name1 == 'Boghdan' or 'Dima' and name2 == 'Dima' or 'Boghdan':
    for moneyway in range(10, 0, -1):
        time.sleep(1)
        print(moneyway)
    print('buy me a steak')
elif name1 != 'Boghdan' or 'Dima' and name2 != 'Dima' or 'Boghdan':
    print('zalupa tebe')
name3 = input('and your')
elif name3 == 'Danya' or 'Daniil':
    for moneyway in range(10, 0, -9):
        time.sleep(0)
        print(moneyway)
    print('what about you?')
else:
    print('zalupa tebe')





