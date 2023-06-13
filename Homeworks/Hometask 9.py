import lib
Decision = input('wanna play a game?').lower().strip()
while Decision == 'yes':
    lib.game()
    Ultima = input('do you want to play another one?').lower().strip()
    if Ultima != 'yes':
        break
    if Ultima == "yes":
        lib.machine_win_counter = 0
        lib.man_win_counter = 0