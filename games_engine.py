import random
from game_state import GameState
from game_rules import GameRules
from report_on_game import ReportOnGame
from report_on_many_games import ReportOnManyGames


class GamesEngine:

    def __init__(self):
        self.game_state = GameState()
        self.game_rules = GameRules()
        self.report_on_game = None
        self.report_on_many_games = ReportOnManyGames()

    # responsible for playing the number of games requested from main.py
    def play_game(self, number_of_games):
        while number_of_games > 0:
            self.report_on_game = ReportOnGame()
            self.game_state = GameState()
            game_in_progress = True
            while game_in_progress:
                game_in_progress = self.make_move()
            number_of_games -= 1

    def make_move(self):
        # randomly select an available square from the available_squares set, and store as a list of length 1
        position_as_list_of_list = random.sample(self.game_state.available_squares, 1)
        row_index = position_as_list_of_list[0][0]
        column_index = position_as_list_of_list[0][1]
        # remove the available square we will shortly use from the available_squares list
        self.game_state.available_squares.remove([row_index, column_index])
        # make move
        self.game_state.board[row_index][column_index] = self.game_state.next_move
        # call game_over to see if the game is over
        if self.game_rules.game_over(self.game_state, row_index, column_index):
            self.between_game_reporting(self.game_rules.winning_letter)
            return False
        # update who moves next
        temp = self.game_state.next_move
        self.game_state.next_move = self.game_state.previous_move
        self.game_state.previous_move = temp
        return True

    def between_game_reporting(self, win_result='Tie'):

        if self.report_on_game.end_of_game_report:
            self.report_on_game.end_of_game_reporter(self.game_state, win_result)

        self.report_on_many_games.track_game_outcomes(win_result)
