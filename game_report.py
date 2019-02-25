class GameReport:

    def __repr__(self):
        return "{}()".format(self.__class__.__name__)

    # call turn_on_end_of_game_reporting from main.py to play_games this report method
    def __call__(self, board, win_result='Tie'):
        print(board)
        if win_result != 'Tie':
            print(win_result + ' won\n')
        else:
            print(win_result + '\n')
