
class Team:

    def __repr__(self):
        return f'{self.name} ({self.seed})'

    def __str__(self):
        return f'{self.name} ({self.seed})'

    def __init__(self, name, seed, revised_seed=None):
        self.name = name
        self.seed = seed
        if revised_seed:
            self.revised_seed = revised_seed
        else:
            self.revised_seed = seed

    def revise_seed(self, beat_seed):
        self.revised_seed = min(
            self.revised_seed,
            (beat_seed + self.revised_seed)/2
        )
