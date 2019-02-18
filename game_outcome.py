class GameOutcome:

    def __init__(self):
        self.letter_dict = {'X': -1, 'O': 1, ' ': 0}
        self.state_of_game = None
        self.row_index_of_move = None
        self.column_index_of_move = None
        self.game_outcome = None

    def find_winner_or_tie(self, state_of_game, row_index_of_move, column_index_of_move):

        self.set_board_and_move(state_of_game, row_index_of_move, column_index_of_move)
        if self.check_row_containing_move_for_win():
            return self.game_outcome
        if self.check_column_containing_move_for_win():
            return self.game_outcome
        if self.check_main_diagonal_for_win_iff_it_contains_move():
            return self.game_outcome
        if self.check_off_diagonal_for_win_iff_it_contains_move():
            return self.game_outcome
        if self.check_for_tie():
            return self.game_outcome

        return ''

    def set_board_and_move(self, state_of_game, row_index_of_move, column_index_of_move):
        self.state_of_game = state_of_game
        self.row_index_of_move = row_index_of_move
        self.column_index_of_move = column_index_of_move

    def check_row_containing_move_for_win(self):
        total = 0
        for column in range(3):
            total = total + int(self.letter_dict[self.state_of_game.board[self.row_index_of_move][column]])
            if abs(total) == 3:
                winning_letter = self.state_of_game.board[self.row_index_of_move][self.column_index_of_move]
                self.game_outcome = winning_letter
                return True
        return False

    def check_column_containing_move_for_win(self):
        total = 0
        for row in range(3):
            total = total + int(self.letter_dict[self.state_of_game.board[row][self.column_index_of_move]])
            if abs(total) == 3:
                winning_letter = self.state_of_game.board[self.row_index_of_move][self.column_index_of_move]
                self.game_outcome = winning_letter
                return True
        return False

    def check_main_diagonal_for_win_iff_it_contains_move(self):
        if self.row_index_of_move == self.column_index_of_move:
            total = 0
            for diagonal_indexing in range(3):
                total = total + int(self.letter_dict[self.state_of_game.board[diagonal_indexing][diagonal_indexing]])
                if abs(total) == 3:
                    winning_letter = self.state_of_game.board[self.row_index_of_move][self.column_index_of_move]
                    self.game_outcome = winning_letter
                    return True
        return False

    def check_off_diagonal_for_win_iff_it_contains_move(self):
        if self.row_index_of_move + self.column_index_of_move == 2:
            total = 0
            for off_diagonal_indexing in range(3):
                total = total + int(self.letter_dict[self.state_of_game.board[off_diagonal_indexing][2 - off_diagonal_indexing]])
                if abs(total) == 3:
                    winning_letter = self.state_of_game.board[self.row_index_of_move][self.column_index_of_move]
                    self.game_outcome = winning_letter
                    return True
        return False

    def check_for_tie(self):
        if len(self.state_of_game.available_squares) == 0:
            self.game_outcome = 'Tie'
            return True
        return False
