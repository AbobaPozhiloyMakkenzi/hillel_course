Decision = input('Do you want to start a game?')
# def words(letter):
#     for  letter in list(word):
#         res = word.find(letter)
#
#         return res

if Decision == 'Yes'.lower().strip():
    while True:
        available_letters = 'abcdefghijklmnopqrstyuwxvz'
        symbols = '!@#$%^&*()-_+=/\\:;[]{}`~'
        numbers = '1234567890'
        word = input('give the task word').lower().strip() #First_Method

        # import random                                   #Second_Method
        # wordlist = ('kisa', 'Programming', 'MaTh')
        # want = random.choice(wordlist)
        # want = str(want).lower().strip()
        #
        # word = want

        guess_result = '?' * len(word)
        guessed_letters = []
        entered_letters = set()
        attempt_counter = 10

        for elementus in word:
            if elementus not in available_letters:
                print('Please, type your word in english and without any numbers!')
                break
            while guess_result != word and  attempt_counter > 0:

                print(f'Guess the word: {guess_result}')

                while attempt_counter > 0:
                    user_letter = input('Enter the letter: ').lower()
                    if len(user_letter) != 1:
                        attempt_counter = attempt_counter - 1
                        print(f'Too long or too short! Now you have ----> {attempt_counter} attempts left')
                        continue
                    elif user_letter not in available_letters:
                        attempt_counter = attempt_counter - 1
                        print(f'Unavailable! Now you have ----> {attempt_counter} attempts left')
                        continue
                    elif user_letter in entered_letters:
                        attempt_counter = attempt_counter - 1
                        print(f'Duplicate! Now you have ----> {attempt_counter} attempts left')
                        continue
                    else:
                        if user_letter not in word or user_letter in symbols or user_letter in numbers:


                            attempt_counter = attempt_counter - 1
                            print(f'Incorrect! Try again! Now you have ----> {attempt_counter} attempts left')

                    entered_letters.add(user_letter)
                    break

                if user_letter in word:
                    guessed_letters.append(user_letter)
                    guess_result = ''.join(['?' if char not in guessed_letters else char for char in word])
                    print(f'you guessed correctly, the letter {user_letter} is the {word.find(user_letter)+1} in your word')

        if attempt_counter <= 1:
            print('unfortunately, yo`ve lost')
            break
        print(f'Congratulations! You guessed correctly, your word was  -------> {word}')
        Question = input('do you want to play a new game?')
        if Question == 'no'.lower().strip():
            break
