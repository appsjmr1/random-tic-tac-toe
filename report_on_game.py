from reports import Reports


class ReportOnGame(Reports):

    end_of_game_report = False

    def __init__(self):
        Reports.__init__(self)

    @classmethod
    def turn_on_end_of_game_reporting(cls):
        cls.end_of_game_report = True

    # call turn_on_end_of_game_reporting from main.py to run this report method
    def end_of_game_reporter(self, board):
        print(board)
        if self.x_won:
            print('X won\n')
        elif self.o_won:
            print('O won\n')
        else:
            print('Its a tie\n')
