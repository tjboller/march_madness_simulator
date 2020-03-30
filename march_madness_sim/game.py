import numpy as np
from random import random
from scipy.interpolate import interp1d

from march_madness_sim.team import Team

HISTORICAL_PROBS = np.array([
    [15, .99],
    [13, .9],
    [11, .85],
    [9, .79],
    [7, .64],
    [5, .62],
    [3, .60],
    [1, .51],
    [0, .50]
])
WIN_PROB_F = interp1d(HISTORICAL_PROBS[:, 0], HISTORICAL_PROBS[:, 1])


class Game:
    def __repr__(self):
        return f'{self.team1.__str__()} - VS - {self.team2.__str__()}'

    def __str__(self):
        return f'{self.team1.__str__()} - VS - {self.team2.__str__()}'

    def __init__(self, team1: Team, team2: Team):
        self.team1 = team1
        self.team2 = team2

    def prob_team1_win(self) -> (float, float):
        seed_diff = self.team1.revised_seed - self.team2.revised_seed
        prob = WIN_PROB_F(abs(seed_diff))
        if seed_diff > 0:
            return 1-prob
        else:
            return prob

    def play_game(self) -> Team:

        winner = self.team2
        loser = self.team1

        rnd = random()
        team1_win_prob = self.prob_team1_win()

        if rnd < team1_win_prob:
            winner = self.team1
            loser = self.team2

        winner.revise_seed(loser.seed)
        return winner
