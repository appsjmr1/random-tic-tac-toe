class Statistics:

    number_of_x_wins = 0
    number_of_o_wins = 0
    number_of_ties = 0

    @classmethod
    def track_game_outcomes(cls, outcome):
        if outcome == 'x_won':
            cls.number_of_x_wins = cls.number_of_x_wins + 1
        if outcome == 'o_won':
            cls.number_of_o_wins = cls.number_of_o_wins + 1
        if outcome == 'tie':
            cls.number_of_ties = cls.number_of_ties + 1

    @classmethod
    def report_outcome_statistics(cls):
        total_games = cls.number_of_x_wins + cls.number_of_o_wins + cls.number_of_ties
        print('Proportion of X wins: ' + str(cls.number_of_x_wins/total_games))
        print('Proportion of O wins: ' + str(cls.number_of_o_wins / total_games))
        print('Proportion of ties: ' + str(cls.number_of_ties / total_games))


