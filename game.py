from board import Board


class Game:

    # makes Game class a singleton
    _singleton = None

    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = super(Game, cls).__new__(cls, *args, **kwargs)
        return cls._singleton

    def __init__(self):
        self.b = None

    # responsible for playing the number of games requested from main.py
    def play_game(self, number_of_games):
        i = 1
        while i <= number_of_games:
            # create a fresh board object for the next game
            self.b = Board()
            # play one game
            game_in_progress = True
            while game_in_progress:
                game_in_progress = self.make_move()
            i = i + 1

    def make_move(self):
        # randomly select an available square
        position = self.b.select_random_square()
        # make a move
        self.b.board[position] = self.b.next_move
        # call game_over to see if the game is over
        if self.b.game_over():
            return False
        # update who moves next
        temp = self.b.next_move
        self.b.next_move = self.b.previous_move
        self.b.previous_move = temp
        return True
