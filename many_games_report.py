class ManyGamesReport:

    def __init__(self):
        self.count_wins_and_ties = {'X': 0, 'O': 0, 'Tie': 0}

    def __repr__(self):
        return "{}".format(self.__class__.__name__)

    def __call__(self, board, win_result):
        self.count_wins_and_ties[win_result] += 1

    def report_outcome_statistics(self):
        total_games = sum(self.count_wins_and_ties.values())
        print('Proportion of X wins: ' + str(self.count_wins_and_ties['X'] / total_games))
        print('Proportion of O wins: ' + str(self.count_wins_and_ties['O'] / total_games))
        print('Proportion of ties: ' + str(self.count_wins_and_ties['Tie'] / total_games))
