
age = int(input('Please, tell your age, darling'))
if age<0:
    print('stop living in the past')
elif len(str(age)) > 2:
     print('seriously, stop it')
elif age<6:
    print('where are your parents')
elif str(age).find('7')!=-1:
    print('you are lucky today')
elif age <16:
    if age>6:
        print('this film is for adults only')
elif age>65:
    print('please show your id')
else:
    print('there are no tikcets left')


