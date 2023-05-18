
#Task1
# - якщо користувачу менше 6 - вивести повідомлення "Де твої батьки?"
#
# - якщо користувачу менше 16 - вивести повідомлення "Це фільм для дорослих!"
#
# - якщо користувачу більше 65 - вивести повідомлення "Покажіть пенсійне посвідчення!"
#
# - якщо вік користувача містить цифру 7 - вивести повідомлення "Вам пощастить!"
#
# - у будь-якому іншому випадку - вивести повідомлення "А білетів вже немає!"

age = input('Please, tell your age, darling')
if int(age)<6:
    print('where are your parents')
elif int(age) <16:
    if int(age)>6:
        print('this film is for adults only')
elif int(age)>65:
    print('please show your id')
elif age.find('7')!=-1:
    print('you are lucky today')
else:
    print('there are no tikcets left')
