from report_on_game import ReportOnGame
from report_on_many_games import ReportOnManyGames


class FindAndReportWinner(ReportOnGame, ReportOnManyGames):

    def __init__(self):
        self.letter_dict = {'X': -1, 'O': 1, ' ': 0}

    def find_winner_or_tie(self, game_state, row_index, column_index):

        # check row containing most recent move for win
        total = 0
        for column in range(3):
            total = total + int(self.letter_dict[game_state.board[row_index][column]])
            if abs(total) == 3:
                winning_letter = game_state.board[row_index][column_index]
                return winning_letter

        # check column containing most recent move for win
        total = 0
        for row in range(3):
            total = total + int(self.letter_dict[game_state.board[row][column_index]])
            if abs(total) == 3:
                winning_letter = game_state.board[row_index][column_index]
                return winning_letter

        # check for win on main-diagonal if it contains most recent move
        if row_index == column_index:
            total = 0
            for diagonal_indexing in range(3):
                total = total + int(self.letter_dict[game_state.board[diagonal_indexing][diagonal_indexing]])
                if abs(total) == 3:
                    winning_letter = game_state.board[row_index][column_index]
                    return winning_letter

        # check for win on off-diagonal if it contains most recent move
        if row_index + column_index == 2:
            total = 0
            for off_diagonal_indexing in range(3):
                total = total + int(self.letter_dict[game_state.board[off_diagonal_indexing][2 - off_diagonal_indexing]])
                if abs(total) == 3:
                    winning_letter = game_state.board[row_index][column_index]
                    return winning_letter

        if len(game_state.available_squares) == 0:
            return 'Tie'

        return ''

    def reporting_after_each_game(self, game_state_instance, win_result='Tie'):

        if self.end_of_game_report:
            self.end_of_game_reporter(game_state_instance, win_result)

        self.track_game_outcomes(win_result)

