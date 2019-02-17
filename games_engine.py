import random
from game_state import GameState
from find_and_report_winner import FindAndReportWinner


class GamesEngine:

    def __init__(self):
        self.game_state_instance = GameState()
        self.find_and_report_winner_instance = FindAndReportWinner()

    # responsible for playing the number of games requested from main.py
    def play_many_games(self, num_games_to_play):
        while num_games_to_play > 0:
            self.initialize_instances_for_new_game()
            self.play_one_game()
            num_games_to_play -= 1
        # shows percentage of wins from X and O as well as percentage of ties
        self.find_and_report_winner_instance.report_outcome_statistics()

    def initialize_instances_for_new_game(self):
        self.game_state_instance = GameState()

    def play_one_game(self):
        game_in_progress = True
        while game_in_progress:
            game_in_progress = self.make_move()

    def make_move(self):

        # randomly select an available square for next move
        square_for_next_move_as_list_of_list = random.sample(self.game_state_instance.available_squares, 1)
        row_index_for_move = square_for_next_move_as_list_of_list[0][0]
        column_index_for_move = square_for_next_move_as_list_of_list[0][1]
        # remove, from the available_squares list, the square we will use
        self.game_state_instance.available_squares.remove([row_index_for_move, column_index_for_move])
        # make move
        self.game_state_instance.board[row_index_for_move][column_index_for_move] = self.game_state_instance.next_move
        # call find_winner_or_tie to see if the game is over
        game_result_as_string = self.find_and_report_winner_instance.find_winner_or_tie(self.game_state_instance, row_index_for_move, column_index_for_move)
        if game_result_as_string:
            self.find_and_report_winner_instance.reporting_after_each_game(self.game_state_instance, game_result_as_string)
            return False
        # update who moves next
        temp = self.game_state_instance.next_move
        self.game_state_instance.next_move = self.game_state_instance.previous_move
        self.game_state_instance.previous_move = temp
        return True
