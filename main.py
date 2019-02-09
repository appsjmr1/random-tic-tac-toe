from game import Game

# main.py module has a Game
game = Game()

# to suppress end of game reports comment out the following line
# game.b.turn_on_end_of_game_reporting()

# parameter passed to play_games determines the number of games that will be played
game.play_game(1000000)
# shows percentage of wins from X and O as well as percentage of ties
game.b.report_outcome_statistics()
