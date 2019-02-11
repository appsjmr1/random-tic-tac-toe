import random
from report_on_game import ReportOnGame
from report_on_many_games import ReportOnManyGames


class GameState:

    def __init__(self):
        self.board = None
        self.available_squares = None
        self.initialize_board_and_available_squares()
        self.next_move = 'X'
        self.previous_move = 'O'
        self.letter_dict = {'X': -1, 'O': 1, ' ': 0}
        self.x_won = False
        self.o_won = False
        self.tie = False
        self.report_game = ReportOnGame()
        self.report_many_games = ReportOnManyGames()

    def initialize_board_and_available_squares(self):
        self.board = [[' ' for i in range(3)] for j in range(3)]
        self.available_squares = [[i, j] for i in range(3) for j in range(3)]

    # Printing an instance of the class will display a standard
    # tic tac toe game image.
    def __str__(self):
        return "\n" + self.board[0][0] + "|" + self.board[0][1] + "|" + self.board[0][2] + "\n"+ self.board[1][0] + "|" + self.board[1][1] + "|" + self.board[1][2] + "\n" + self.board[2][0] + "|" + self.board[2][1] + "|" + self.board[2][2]

    # responsible for playing the number of games requested from main.py
    def play_game(self, number_of_games):
        while number_of_games > 0:
            self.report_game = ReportOnGame()
            self.next_move = 'X'
            self.previous_move = 'O'
            self.initialize_board_and_available_squares()
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

    def game_over(self, row_index, column_index):

        # check row containing most recent move for win
        total = 0
        for column in range(3):
            total = total + int(self.letter_dict[self.board[row_index][column]])
            if abs(total) == 3:
                self.end_of_game(self.board[row_index][column_index])
                return True

        # check column containing most recent move for win
        total = 0
        for row in range(3):
            total = total + int(self.letter_dict[self.board[row][column_index]])
            if abs(total) == 3:
                self.end_of_game(self.board[row_index][column_index])
                return True

        # check for win on main-diagonal if it contains most recent move
        if row_index == column_index:
            total = 0
            for diagonal_indexing in range(3):
                total = total + int(self.letter_dict[self.board[diagonal_indexing][diagonal_indexing]])
                if abs(total) == 3:
                    self.end_of_game(self.board[row_index][column_index])
                    return True

        # check for win on off-diagonal if it contains most recent move
        if row_index + column_index == 2:
            total = 0
            for off_diagonal_indexing in range(3):
                total = total + int(self.letter_dict[self.board[off_diagonal_indexing][2-off_diagonal_indexing]])
                if abs(total) == 3:
                    self.end_of_game(self.board[row_index][column_index])
                    return True

        if len(self.available_squares) == 0:
            self.end_of_game()
            return True

        return False

    def end_of_game(self, win_result='Tie'):
        if self.report_game.end_of_game_report:
            self.report_game.end_of_game_reporter(self, win_result)

        if win_result == 'X':
            self.report_game.x_won = True
            self.report_many_games.track_game_outcomes('x_won')

        elif win_result == 'O':
            self.report_game.o_won = True
            self.report_many_games.track_game_outcomes('o_won')

        else:
            self.report_game.tie = True
            self.report_many_games.track_game_outcomes('tie')

