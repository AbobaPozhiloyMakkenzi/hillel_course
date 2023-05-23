#task1
userinput = list(input("Please type the word you need").strip())
print(type(userinput))
res = userinput[2]
print(f'The third element in your word is {res}')

#task2

userprint = input('please, type your suggestion').strip().split(' ')
print(userprint)
res = len(userprint)
print(f'you`ve got {res} words in your sentence')

#task3

user_message = ['1', '2', 3.5, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
res = []
for i in user_message:
    if type(i) == int or type(i) == float:
        res.append(i)
print(res)

