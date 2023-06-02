# TASK 1 Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент, перетворений на float.####################################################
# Якщо перетворити не вдається функція має повернути 0

element = input('type your element')


def change_to_float(element):
    try:
        element = float(element)
        return element
    except:
        return '0'

print(change_to_float(element))

# TASK 2 Напишіть функцію, що приймає два аргументи. Функція повинна:###############################################################################
# 1)якщо аргументи відносяться до числових типів (int, float) - повернути перемножене значення цих аргументів,
# 2)якщо обидва аргументи це строки (str) - обʼєднати в одну строку та повернути
# 3) у будь-якому іншому випадку повернути кортеж з цих аргументів

def task_2 (element1, element2, *args,**kwargs):
    items = element1 and element2
    try:
        if items == int or float:
            res = element1*element2
            return(res)
    except:
        if items == str(items):
            res1 = ''.join([element1,element2])
            return (f'here you go -----> {res1}')
    if True:
        tuple = (element1, element2)
        return(tuple)

print(task_2(element1 = 2,element2 = 2))
print(task_2(element1='aboba',element2=' pozhiloy makkenzi'))
print(task_2(element1= [2,3,4], element2=[1,2,3]))

#Task 3############################################################
age = int(input('Please, tell your age, darling'))

def age1(age_ps):

    if age_ps > 1 or age_ps < 1:
        res = 'years old'
        return res
    if age_ps == 1:
        res = 'year old'
        return res

def age_check(age):

    if age < 0:
        res = print(f'stop living in the past, you cannot be {age} {age1(age)} ')
        return res
    elif len(str(age)) > 2:
        res = print(f'seriously, stop it! you cannot be  {age} {age1(age)}')
        return res
    elif age<6:
        res = print(f'where are your parents, being {age} { age1(age)} you can`t buy tickets yourself ')
        return res
    elif str(age).find('7')!=-1:
        res = print(f'you are lucky today, because you have number {age} in your age, you are {age} { age1(age)} ')
    elif age <16 and age>6:
            res = print(f'this film is for adults only, and you are just {age} { age1(age)}')
            return res
    elif age>65:
        res = print(f'please show your id, you don`t look like you are {age} { age1(age)}')
        return res
    else:
        res = print(f'No matter that you are {age} { age1(age)} there are no tikcets left')

age_check(age)