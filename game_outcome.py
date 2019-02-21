class GameOutcome:

    def __init__(self):
        self._letter_dict = {'X': -1, 'O': 1, ' ': 0}
        self._game_state = None
        self._row = None
        self._col = None
        self._game_outcome = None

    def find_winner_or_tie(self, game_state, row, col):

        """ Check if either player has won, or if a tie has occurred. Return 'X' or 'O'
            for a win, 'Tie' for a tie, and None when the game is not over.

            Parameters:
              game_state:  state of the game
              row:    row of the last move
              col:    column of the last move
        """

        self._set_board_and_move(game_state, row, col)

        if self._check_row():
            return self._game_outcome
        if self._check_column():
            return self._game_outcome
        if self._check_main_diagonal():
            return self._game_outcome
        if self._check_off_diagonal():
            return self._game_outcome
        if self._check_tie():
            return self._game_outcome

        return ''

    def _set_board_and_move(self, state_of_game, row_index_of_move, column_index_of_move):
        self._game_state = state_of_game
        self._row = row_index_of_move
        self._col = column_index_of_move

    def _check_row(self):
        total = sum([self._letter_dict[self._game_state.board[self._row][column]] for column in range(3)])
        if abs(total) == 3:
            winning_letter = self._game_state.board[self._row][self._col]
            self._game_outcome = winning_letter
            return True
        return False

    def _check_column(self):
        total = sum([self._letter_dict[self._game_state.board[row][self._col]] for row in range(3)])
        if abs(total) == 3:
            winning_letter = self._game_state.board[self._row][self._col]
            self._game_outcome = winning_letter
            return True
        return False

    def _check_main_diagonal(self):

        if self._row == self._col:
            total = sum([self._letter_dict[self._game_state.board[diagonal_indexing][diagonal_indexing]] for diagonal_indexing in range(3)])
            if abs(total) == 3:
                winning_letter = self._game_state.board[self._row][self._col]
                self._game_outcome = winning_letter
                return True
        return False

    def _check_off_diagonal(self):
        if self._row + self._col == 2:
            total = sum([self._letter_dict[self._game_state.board[off_diagonal_indexing][2 - off_diagonal_indexing]] for off_diagonal_indexing in range(3)])
            if abs(total) == 3:
                winning_letter = self._game_state.board[self._row][self._col]
                self._game_outcome = winning_letter
                return True
        return False

    def _check_tie(self):
        if len(self._game_state.available_squares) == 0:
            self._game_outcome = 'Tie'
            return True
        return False
