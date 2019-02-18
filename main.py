import sys
from games_engine import GamesEngine
from game_report import GameReport
from many_games_report import ManyGamesReport


def run_random_tic_tac_toe_simulation(num_games_to_play, report_all_games=None):
    games_engine = prepare_reports(report_all_games)
    games_engine.play_many_games(num_games_to_play)
    report_on_many_games = list(games_engine.reports_requested).pop()
    report_on_many_games.report_outcome_statistics()


def prepare_reports(report_all_games):
    report_requests = []
    if report_all_games is not None:
        report_on_game = GameReport()
        report_requests.append(report_on_game)
    report_on_many_games = ManyGamesReport()
    report_requests.append(report_on_many_games)
    return GamesEngine(*report_requests)


if __name__ == '__main__':
    run_random_tic_tac_toe_simulation(10, 'r')

    # uncomment the below code to run from command line

    # game_count_and_report_toggle = [int(sys.argv[1])]
    # if len(sys.argv) == 3:
    #     game_count_and_report_toggle.append(sys.argv[2])
    # run_random_tic_tac_toe_simulation(*game_count_and_report_toggle)
