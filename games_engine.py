import random
from game_state import GameState
from find_game_outcome import FindGameOutcome


class GamesEngine:

    def __init__(self, *reports_requested):
        self.game_state_instance = GameState()
        self.find_game_outcome_instance = FindGameOutcome()
        self.row_index_for_move = None
        self.column_index_for_move = None
        self.reports_requested = reports_requested

    # responsible for playing the number of games requested from main.py
    def play_many_games(self, num_games_to_play):
        while num_games_to_play > 0:
            self.play_one_game()
            num_games_to_play -= 1

    def play_one_game(self):

        self.game_state_instance = GameState()

        game_over = False
        while not game_over:

            self.make_move()
            self.update_who_moves_next()

            game_result_as_string = self.find_game_outcome_instance.find_winner_or_tie(self.game_state_instance, self.row_index_for_move, self.column_index_for_move)

            if game_result_as_string:
                for report_calls in self.reports_requested:
                    report_calls(self.game_state_instance, game_result_as_string)
                game_over = True

    def make_move(self):
        # randomly select an available square for next move
        square_for_next_move_as_list_of_list = random.sample(self.game_state_instance.available_squares, 1)
        self.row_index_for_move = square_for_next_move_as_list_of_list[0][0]
        self.column_index_for_move = square_for_next_move_as_list_of_list[0][1]
        # remove, from the available_squares list, the square we will use
        self.game_state_instance.available_squares.remove([self.row_index_for_move, self.column_index_for_move])
        # make move
        self.game_state_instance.board[self.row_index_for_move][self.column_index_for_move] = self.game_state_instance.next_move

    def update_who_moves_next(self):
        # update who moves next
        temp = self.game_state_instance.next_move
        self.game_state_instance.next_move = self.game_state_instance.previous_move
        self.game_state_instance.previous_move = temp
        return True
