class GameReport:

    # call turn_on_end_of_game_reporting from main.py to run_random_tic_tac_toe_simulation this report method
    def __call__(self, board, win_result='Tie'):
        print(board)
        if win_result != 'Tie':
            print(win_result + ' won\n')
        else:
            print(win_result + '\n')
