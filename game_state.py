import random
from report_on_game import ReportOnGame
from report_on_many_games import ReportOnManyGames


class GameState:

    def __init__(self):
        # game board
        # Google how to create an initializing function [to create the below double list with loops]
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        # Google how to create an initializing function [to create the below double list with loops]
        self.available_squares = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
        self.next_move = 'X'
        self.previous_move = 'O'
        self.letter_dict = {'X': -1, 'O': 1}

    # Printing an instance of the class will display a standard
    # tic tac toe game image.
    def __str__(self):
        return "\n" + self.board[0][0] + "|" + self.board[0][1] + "|" + self.board[0][2] + "\n"+ self.board[1][0] + "|" + self.board[1][1] + "|" + self.board[1][2] + "\n" + self.board[2][0] + "|" + self.board[2][1] + "|" + self.board[2][2]

    # responsible for playing the number of games requested from main.py
    def play_game(self, number_of_games):
        while number_of_games > 0:
            self.next_move = 'X'
            self.previous_move = 'O'
            game_in_progress = True
            while game_in_progress:
                game_in_progress = self.make_move()
            number_of_games -= 1

    def make_move(self):
        # randomly select an available square from the available_squares set, and store as a list of length 1
        position_as_list_of_list = random.sample(self.available_squares, 1)
        row_index = position_as_list_of_list[0][0]
        column_index = position_as_list_of_list[0][1]
        # remove the available square we will shortly use from the available_squares list
        self.available_squares.remove([row_index, column_index])
        # make move
        self.board[row_index][column_index] = self.next_move
        # call game_over to see if the game is over
        if self.game_over(row_index, column_index):
            return False
        # update who moves next
        temp = self.next_move
        self.next_move = self.previous_move
        self.previous_move = temp
        return True


        # if self.game_won():
           #  return True
        # elif self.game_tied():
            # return True
        # else:
            # return False

    def game_over(self, row_index, column_index):
        pass



    self.report_game.x_won = True
    self.report_many_games.track_game_outcomes('x_won')

    self.report_game.o_won = True
    self.report_many_games.track_game_outcomes('o_won')

    self.report_game.tie = True
    self.report_many_games.track_game_outcomes('tie')

    if self.report_game.end_of_game_report is True:
        self.report_game.end_of_game_reporter(self.game_state.__str__())

