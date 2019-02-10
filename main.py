

# main.py module has a GameLogic
game_logic = GameLogic()

# to suppress end of game reports comment out the following line
# game_logic.report_game.turn_on_end_of_game_reporting()

# parameter passed to play_games determines the number of games that will be played
game_logic.play_game(1000000)
# shows percentage of wins from X and O as well as percentage of ties
game_logic.report_many_games.report_outcome_statistics()
