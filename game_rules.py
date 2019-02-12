class GameRules:

    def __init__(self):
        self.letter_dict = {'X': -1, 'O': 1, ' ': 0}
        self.winning_letter = None

    def game_over(self, game_state, row_index, column_index):

        # check row containing most recent move for win
        total = 0
        for column in range(3):
            total = total + int(self.letter_dict[game_state.board[row_index][column]])
            if abs(total) == 3:
                self.winning_letter = game_state.board[row_index][column_index]
                return True

        # check column containing most recent move for win
        total = 0
        for row in range(3):
            total = total + int(self.letter_dict[game_state.board[row][column_index]])
            if abs(total) == 3:
                self.winning_letter = game_state.board[row_index][column_index]
                return True

        # check for win on main-diagonal if it contains most recent move
        if row_index == column_index:
            total = 0
            for diagonal_indexing in range(3):
                total = total + int(self.letter_dict[game_state.board[diagonal_indexing][diagonal_indexing]])
                if abs(total) == 3:
                    self.winning_letter = game_state.board[row_index][column_index]
                    return True

        # check for win on off-diagonal if it contains most recent move
        if row_index + column_index == 2:
            total = 0
            for off_diagonal_indexing in range(3):
                total = total + int(self.letter_dict[game_state.board[off_diagonal_indexing][2 - off_diagonal_indexing]])
                if abs(total) == 3:
                    self.winning_letter = game_state.board[row_index][column_index]
                    return True

        if len(game_state.available_squares) == 0:
            self.winning_letter = 'Tie'
            return True

        return False
