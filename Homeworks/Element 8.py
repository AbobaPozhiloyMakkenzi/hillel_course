import random
import time

def time_counter(funct):
    def wrapper():
        time_start = time.time()
        funct()
        time_end = time.time()
        result = (time_end - time_start)
        return result
    return wrapper

machine_win_counter = 0
man_win_counter = 0


def man_goals():
    """
    counting user`s goals
    """
    global machine_win_counter
    global man_win_counter
    man_win_counter = man_win_counter + 1
    print(f'{man_win_counter} : {machine_win_counter}')


def machine_goals():
    """
    counting machines`s goals
    """
    global machine_win_counter
    global man_win_counter
    machine_win_counter = machine_win_counter + 1
    print(f'{man_win_counter} : {machine_win_counter}')


def logics(el1,el2,pick):
    """
    game logic
    :param el1: userinput
    :param el2: machine_random_choice
    :return: compare result
    """
    global machine_win_counter
    global man_win_counter
    print(f'machine choice is {pick}')
    if (el1 == 'scissors' and el2 == 'paper') or (el1 == 'paper' and el2 == 'rock') or (el1 == 'rock' and el2 == 'scissors'):
        print(f'{el1} beat {el2}')
        man_goals()
    if (el1 == 'paper' and el2 == 'scissors') or (el1 == 'rock' and el2 == 'paper') or (el1 == 'scissors' and el2 == 'rock'):
        print(f'{el2} beat {el1}')
        machine_goals()
    if el1 == el2:
        print('It`s a draw!')

@time_counter
def game():
    while machine_win_counter < 3 and man_win_counter < 3:
        """
        engine of the game 
        data source(players choice, machine element randomizer), game rules and user input control.
        """
        players_choice = input('rock, paper, scissors, 3.... 2..... 1....').strip().lower()
        game_elements = ['paper', 'rock', 'scissors']
        pick = random.choice(game_elements)

        if players_choice not in game_elements:
            break  # paper beats rock, scissors beat paper, rock beats scissors

        logics(players_choice, pick,pick)

        question = input('do you want to continue?')
        if question != 'yes':

            break
print(game())