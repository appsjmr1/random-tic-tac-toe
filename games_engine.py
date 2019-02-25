import random
from game_state import GameState
from game_outcome import GameOutcome


class GamesEngine:

    def __init__(self, *reports_requested):
        self._state_of_game = GameState()
        self._find_game_outcome = GameOutcome()
        self._row_index_for_move = None
        self._column_index_for_move = None
        self.reports_requested = reports_requested

    def __repr__(self):
        return "{}(*{})".format(self.__class__.__name__, self.reports_requested)

    def play_many_games(self, num_games_to_play):
        while num_games_to_play > 0:
            self.play_one_game()
            num_games_to_play -= 1

    def play_one_game(self):
        self._state_of_game = GameState()
        game_over = False
        while not game_over:
            self.make_move()
            self.update_who_moves_next()
            game_over = self.game_is_over()

    def make_move(self):
        # randomly select an available square for next move
        square_for_next_move_as_list_of_list = random.sample(self._state_of_game.available_squares, 1)
        self._row_index_for_move = square_for_next_move_as_list_of_list[0][0]
        self._column_index_for_move = square_for_next_move_as_list_of_list[0][1]
        # remove, from the available_squares list, the square we will use
        self._state_of_game.available_squares.remove([self._row_index_for_move, self._column_index_for_move])
        # make move
        self._state_of_game.board[self._row_index_for_move][self._column_index_for_move] = self._state_of_game.next_move

    def update_who_moves_next(self):
        temp = self._state_of_game.next_move
        self._state_of_game.next_move = self._state_of_game.previous_move
        self._state_of_game.previous_move = temp

    def game_is_over(self):
        game_result_as_string = ''
        if self._row_index_for_move is not None:
            game_result_as_string = self._find_game_outcome.find_winner_or_tie(self._state_of_game, self._row_index_for_move, self._column_index_for_move)
        if game_result_as_string:
            for report_calls in self.reports_requested:
                report_calls(self._state_of_game, game_result_as_string)
            return True
        else:
            return False
