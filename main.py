from games_engine import GamesEngine
from find_and_report_winner import FindAndReportWinner


def run_random_tic_tac_toe_simulation(game_report_on, num_games_to_play):
    '''num_games_to_play determines how many games will be played, with random moves,
    during the simulation (X always moves first).
    game_repot_on is a boolean that determines whether the board is printed after each game.'''

    # Pass True to set_end_of_game_reporting to report on each game
    FindAndReportWinner.set_end_of_game_reporting(game_report_on)

    games_engine_instance = GamesEngine()

    # parameter passed to play_many_games determines the number of games that will be played
    games_engine_instance.play_many_games(num_games_to_play)


if __name__ == '__main__':
    run_random_tic_tac_toe_simulation(True, 10)
