from typing import List, Tuple
import json
from itertools import zip_longest

import march_madness_sim as mm
from march_madness_sim.team import Team
from march_madness_sim.game import Game


class Tourney:

    def __init__(self):
        self.games = _game_grouper(self._tourney_dto())

    def _tourney_dto(self) -> List[Team]:
        tourney_init = json.load(open(mm.ROOT_DIR + '/tourney_init.json'))
        teams = [Team(
                    list(team.keys())[0],
                    list(team.values())[0])
                 for team in tourney_init['Teams']]
        return teams

    def play_round(self):
        self.games = _game_grouper([game.play_game() for game in self.games])

    def run_tourney(self) -> None:
        while len(self.games) >= 1:
            print(self.games)
            self.play_round()


def _game_grouper(teams: List[Team]) -> List[Game]:
    if len(teams) > 1:
        args = [iter(teams)] * 2
        return [Game(*game) for game in zip_longest(*args)]
    else:
        print(f'Only one team left!! Winner winner chicken dinner: {teams[0].__str__()}')
        return []


if __name__ == "main":
    t = Tourney()
    t.run_tourney()
