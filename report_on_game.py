class ReportOnGame:

    end_of_game_report = False

    @classmethod
    def set_end_of_game_reporting(cls, boolean_set):
        cls.end_of_game_report = boolean_set

    # call turn_on_end_of_game_reporting from main.py to run_random_tic_tac_toe_simulation this report method
    @staticmethod
    def end_of_game_reporter(board, win_result='Tie'):
        print(board)
        if win_result != 'Tie':
            print(win_result + ' won\n')
        else:
            print(win_result + '\n')
