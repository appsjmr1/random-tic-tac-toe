from game_state import GameState


# main.py module has a GameLogic
game_state = GameState()

# Pass True to set_end_of_game_reporting to report on each game
game_state.report_game.set_end_of_game_reporting(False)

# parameter passed to play_games determines the number of games that will be played
game_state.play_game(1000000)
# shows percentage of wins from X and O as well as percentage of ties
game_state.report_many_games.report_outcome_statistics()
