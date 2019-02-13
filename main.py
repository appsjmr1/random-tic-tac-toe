from games_engine import GamesEngine
from report_on_game import ReportOnGame


def run(game_report_on, number_of_games):

    # Pass True to set_end_of_game_reporting to report on each game
    ReportOnGame.set_end_of_game_reporting(game_report_on)

    games_engine_instance = GamesEngine()

    # parameter passed to play_many_games determines the number of games that will be played
    games_engine_instance.play_many_games(number_of_games)


if __name__ == '__main__':
    run(False, 1000000)
