# soglasniye = ['b','v','s','d']
# sentence = input('your sentence').strip().split()
# counter = 0
# for word  in sentence:
#     print(word)
#     for i in range(len(word)-1):
#         if word[i] in soglasniye and  word[i] == word[i+1]:
#             counter += 1
# print(counter)
#
#
# intlist = '0123456789'
# counter = 0
# userinput = input('print your sentence').strip().split()
# for words in userinput:
#     for i in words:
#         if i in intlist:
#             counter += 1
#
# print(f'----->  {counter}')

# def print_person (name, age):
#     print(name,age)
#
#
# print_person('danya', 21)
#
# def sum(a, b, c):
#     print('vasily')
#     return a+b+c
#
# print(sum(a=1,b=2,c=3))


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

# если сумма чисел меньше 21 выводит - проиграл, если больше - проиграл, если 21 - выиграл
# также, взять 3 игроков, у кого сумма выпала ближе к 21 - выиграл



def plus(number1, number2, number3):
    return(number1+number2+number3)


decision_player1 = input('do you want to take cards? ')
next_decision = print(input('do you want to take another one?'))

if decision_player1 == 'yes':
    cards = input('pick the card')
elif next_decision == 'no':
    pass
if next_decision == 'yes':
    player1cards = input('take another one')
elif next_decision == 'no':
     pass
player1cards = plus()
print(player1cards)

# player2 = input('pick')
# player3 = input('pick')

# for player1cards in player1:
#     var = (player1cards)
#     print(var)
