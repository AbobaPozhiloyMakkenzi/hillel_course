# #task1Дана довільна строка. Напишіть код, який знайде в ній і віведе на екран кількість слів, які містять дві голосні літери підряд.
# vowels = ['a', 'e', 'i', 'o', 'u']
# sentence = input('please, print your sentence').strip().split()
# list = 0
# for word in sentence:
#     for i in range(len(word)-1):
#         if word[i] in vowels and word[i] == word[i+1]:
#             list += 1
# print(list)
#
# #OROROROROROR
#
# def check_word(word):
#     soglasniye = ['b', 'v', 's', 'd', 'n']
#     for i in range(len(word) - 1):
#         if word[i] in soglasniye and  word[i] == word[i+1]:
#             return True
#     return False
#
# def check_sentence():
#     sentence = input('your sentence').strip().split()
#     counter = 0
#
#     for word in sentence:
#         if check_word(word):
#             counter += 1
#     print(counter)
#
#
# check_sentence()
#
# # #task2 Напишіть код, який знайде і виведе на екран назви магазинів, ціни яких попадають в діапазон між мінімальною і максимальною ціною
# lower_limit = 35.9
# upper_limit = 37.339
# shop_list = { "cito": 47.999,
#               "BB_studio": 42.999,
#               "momo": 49.999,
#               "main-service": 37.245,
#               "buy.now": 38.324,
#               "x-store": 37.166,
#               "the_partner": 38.988,
#               "store": 37.720,
#               "rozetka": 38.003}
# for res in shop_list.items():
#     if res[1] >= lower_limit and res[1] <= upper_limit:
#        print(res)

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

userinput = input('type')
determiner = (int(userinput)%10)
def teens(range1):
    list1 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    for i in list1:
        if i == range1:
            res = 'років'
            return res
teens(int(userinput))
def age1(age_ps):
    if age_ps == 2 or age_ps ==3 or age_ps == 4:
        res = 'роки'
        return res
    if age_ps == 1:
        res = 'рік'
        return res
print(age1(determiner))

print(int(userinput))