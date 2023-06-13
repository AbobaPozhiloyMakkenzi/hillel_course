import time
machine_win_counter = 0
man_win_counter = 0

def time_counter(funct):
    def wrapper():
        time_start = time.time()
        function_result = funct()
        time_end = time.time()
        result = (time_end - time_start)
        print(result)
        return function_result
    return wrapper

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
    print(f'machine choice is {pick}')
    if (el1 == 'scissors' and el2 == 'paper') or (el1 == 'paper' and el2 == 'rock') or (el1 == 'rock' and el2 == 'scissors'):
        print(f'{el1} beat {el2}')
        man_goals()
    if (el1 == 'paper' and el2 == 'scissors') or (el1 == 'rock' and el2 == 'paper') or (el1 == 'scissors' and el2 == 'rock'):
        print(f'{el2} beat {el1}')
        machine_goals()
    if el1 == el2:
        print('It`s a draw!')