import sys
from games_engine import GamesEngine
from report_on_game import ReportOnGame
from report_on_many_games import ReportOnManyGames


def run_random_tic_tac_toe_simulation(num_games_to_play, report_all_games=None):

    report_requests = []
    if report_all_games is not None:
        report_on_game_instance = ReportOnGame()
        report_requests.append(report_on_game_instance)
    report_on_many_games_instance = ReportOnManyGames()
    report_requests.append(report_on_many_games_instance)

    games_engine_instance = GamesEngine(*report_requests)

    # parameter passed to play_many_games determines the number of games that will be played
    games_engine_instance.play_many_games(num_games_to_play)

    # shows percentage of wins from X and O as well as percentage of ties
    report_on_many_games_instance.report_outcome_statistics()


if __name__ == '__main__':
    run_random_tic_tac_toe_simulation(10, 'r')

    # uncomment the below code to run from command line

    # game_count_and_report_toggle = [int(sys.argv[1])]
    # if len(sys.argv) == 3:
    #     game_count_and_report_toggle.append(sys.argv[2])
    # run_random_tic_tac_toe_simulation(*game_count_and_report_toggle)
