from games_engine import GamesEngine
from report_on_game import ReportOnGame
from report_on_many_games import ReportOnManyGames

games_engine = GamesEngine()
report_on_game = ReportOnGame()
report_on_many_games = ReportOnManyGames()

# Pass True to set_end_of_game_reporting to report on each game
# report_on_game.set_end_of_game_reporting(True)

# parameter passed to play_games determines the number of games that will be played
games_engine.play_game(1000000)

# shows percentage of wins from X and O as well as percentage of ties
report_on_many_games.report_outcome_statistics()



