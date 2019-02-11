class ReportOnGame:

    end_of_game_report = False

    @classmethod
    def set_end_of_game_reporting(cls, boolean_set):
        cls.end_of_game_report = boolean_set

    # call turn_on_end_of_game_reporting from main.py to run this report method
    @staticmethod
    def end_of_game_reporter(board, result='Its a tie'):
        print(board)
        if result == 'X':
            print(result + ' won\n')
        elif result == 'O':
            print(result + ' won\n')
        else:
            print(result + '\n')
