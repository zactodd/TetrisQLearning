import numpy as np


class Board:
    def __init__(self):
        self.matrix = np.zeros((10, 20))
        self.lines = 0
        self.score = 0

    @property
    def level(self):
        return self.lines // 10

    @property
    def lock_delay(self):
        return self.level