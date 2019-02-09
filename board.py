import random
from statistics import Statistics


class Board(Statistics):

    end_of_game_report = False

    def __init__(self):
        # the following line causes the __init__ method from the Statistics class to still run
        Statistics.__init__(self)
        # game board
        self.board = [' '] * 9
        self.next_move = 'X'
        self.previous_move = 'O'
        self.all_possible_wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        self.letter_dict = {'X': -1, 'O': 1}
        self.x_won = False
        self.o_won = False
        self.tie = False

    # Printing an instance of the class will display a standard
    # tic tac toe game image.
    def __str__(self):
        return "\n" + self.board[0] + "|" + self.board[1] + "|" + self.board[2] + "\n"+ self.board[3] + "|" + self.board[4] + "|" + self.board[5] + "\n" + self.board[6] + "|" + self.board[7] + "|" + self.board[8]

    @classmethod
    def turn_on_end_of_game_reporting(cls):
        cls.end_of_game_report = True

    # call turn_on_end_of_game_reporting from main.py to run this report method
    def end_of_game_reporter(self):
        if self.x_won is True:
            print(self)
            print('X won\n')
        elif self.o_won is True:
            print(self)
            print('O won\n')
        else:
            print(self)
            print('Its a tie\n')

    def get_available_squares(self):
        # creates a list containing the position of all open squares
        list_of_open_squares = []
        i = 0
        for j in self.board:
            if j == ' ':
                list_of_open_squares.append(i)
            i = i + 1
        return list_of_open_squares

    def select_random_square(self):
        list_of_open_squares = self.get_available_squares()
        # return a randomly selected available square
        return random.choice(list_of_open_squares)

    def game_won(self):
        for three_contiguous in self.all_possible_wins:
            row = 0
            for i in three_contiguous:
                if self.board[i] == ' ':
                    break
                row = row + self.letter_dict[self.board[i]]
            if row == -3 or row == 3:
                if row == -3:
                    self.x_won = True
                    self.track_game_outcomes('x_won')
                if row == 3:
                    self.o_won = True
                    self.track_game_outcomes('o_won')
                # self.brain.prep_dict_entry(three_contiguous, self.board, self.previous_move)
                if Board.end_of_game_report is True:
                    self.end_of_game_reporter()
                return True
        return False

    def game_tied(self):
        if ' ' not in self.board[:9]:
            self.tie = True
            self.track_game_outcomes('tie')
            if Board.end_of_game_report is True:
                self.end_of_game_reporter()
            return True
        return False

    def game_over(self):
        if self.game_won():
            return True
        elif self.game_tied():
            return True
        else:
            return False
