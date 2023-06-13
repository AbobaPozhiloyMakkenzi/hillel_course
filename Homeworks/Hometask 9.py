import random
import lib


@lib.time_counter
def game():
    while lib.machine_win_counter < 3 and lib.man_win_counter < 3:
        """
        engine of the game 
        data source(players choice, machine element randomizer), game rules and user input control.
        """
        players_choice = input('rock, paper, scissors, 3.... 2..... 1....').strip().lower()
        game_elements = ['paper', 'rock', 'scissors']
        pick = random.choice(game_elements)

        if players_choice not in game_elements:
            break  # paper beats rock, scissors beat paper, rock beats scissors

        lib.logics(players_choice, pick,pick)

        question = input('do you want to continue?')
        if question != 'yes':

            break


game()