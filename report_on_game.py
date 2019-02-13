class ReportOnGame:

    end_of_game_report = False

    @classmethod
    def set_end_of_game_reporting(cls, boolean_set):
        cls.end_of_game_report = boolean_set

    # call turn_on_end_of_game_reporting from main.py to run this report method
    @staticmethod
    def end_of_game_reporter(board, result='Tie'):
        print(board)
        if result != 'Tie':
            print(result + ' won\n')
        else:
            print(result + '\n')
