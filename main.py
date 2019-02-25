import sys
from games_engine import GamesEngine
from game_report import GameReport
from many_games_report import ManyGamesReport


def play_games(number_of_games, report_all_games=None):
    games_engine = prepare_reports(report_all_games)
    print('Here is the printout of games_engine:')
    print(games_engine)
    games_engine.play_many_games(number_of_games)
    report_on_many_games = list(games_engine.reports_requested).pop()
    report_on_many_games.report_outcome_statistics()


def prepare_reports(report_all_games):
    report_requests = []
    if report_all_games is not None:
        report_on_game = GameReport() ###
        report_requests.append(report_on_game)
    report_on_many_games = ManyGamesReport() ###f
    report_requests.append(report_on_many_games)
    return GamesEngine(*report_requests)


if __name__ == '__main__':
    play_games(10, 'r')

    # uncomment the below code to run from command line

    # game_count_and_report_toggle = [int(sys.argv[1])]
    # if len(sys.argv) == 3:
    #     game_count_and_report_toggle.append(sys.argv[2])
    # play_games(*game_count_and_report_toggle)
