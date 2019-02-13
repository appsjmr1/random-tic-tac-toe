import random
from game_state import GameState
from game_rules import GameRules
from report_on_game import ReportOnGame
from report_on_many_games import ReportOnManyGames


class GamesEngine:

    def __init__(self):
        self.game_state_instance = GameState()
        self.game_rules_instance = GameRules()
        self.report_on_many_games_instance = ReportOnManyGames()

    # responsible for playing the number of games requested from main.py
    def play_many_games(self, number_of_games):
        while number_of_games > 0:
            self.initialize_instances_for_new_game()
            self.play_one_game()
            number_of_games -= 1
        # shows percentage of wins from X and O as well as percentage of ties
        self.report_on_many_games_instance.report_outcome_statistics()

    def initialize_instances_for_new_game(self):
        self.game_state_instance = GameState()

    def play_one_game(self):
        game_in_progress = True
        while game_in_progress:
            game_in_progress = self.make_move()

    def make_move(self):

        # randomly select an available square from the available_squares set, and store as a list of length 1
        position_as_list_of_list = random.sample(self.game_state_instance.available_squares, 1)
        row_index = position_as_list_of_list[0][0]
        column_index = position_as_list_of_list[0][1]
        # remove the available square we will shortly use from the available_squares list
        self.game_state_instance.available_squares.remove([row_index, column_index])
        # make move
        self.game_state_instance.board[row_index][column_index] = self.game_state_instance.next_move
        # call game_over to see if the game is over
        game_over_truthy_falsy = self.game_rules_instance.game_over(self.game_state_instance, row_index, column_index)
        if game_over_truthy_falsy:
            self.between_game_reporting(game_over_truthy_falsy)
            return False
        # update who moves next
        temp = self.game_state_instance.next_move
        self.game_state_instance.next_move = self.game_state_instance.previous_move
        self.game_state_instance.previous_move = temp
        return True

    def between_game_reporting(self, win_result='Tie'):

        if ReportOnGame.end_of_game_report:
            ReportOnGame.end_of_game_reporter(self.game_state_instance, win_result)

        self.report_on_many_games_instance.track_game_outcomes(win_result)
