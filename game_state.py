class GameState:

    def __init__(self):
        self.board = None
        self.available_squares = None
        self.next_move = 'X'
        self.previous_move = 'O'
        self._initialize_board_and_available_squares()

    def _initialize_board_and_available_squares(self):
        self.board = [[' ' for i in range(3)] for j in range(3)]
        self.available_squares = [[i, j] for i in range(3) for j in range(3)]

    # Printing an instance of the class will display a standard
    # tic tac toe game board.
    def __str__(self):
        return "\n" + self.board[0][0] + "|" + self.board[0][1] + "|" + self.board[0][2] + "\n" + self.board[1][0] + "|" + self.board[1][1] + "|" + self.board[1][2] + "\n" + self.board[2][0] + "|" + self.board[2][1] + "|" + self.board[2][2]

    def __repr__(self):
        return "{}()".format(self.__class__.__name__)
