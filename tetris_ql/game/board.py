import numpy as np
from game import tetromino


class Board:
    def __init__(self):
        self._lines_per_level = 10
        self._max_level = 30
        self._width = 10
        self._height = 20
        self._height_padding = 5
        self._num_visible_tetrominos = 5

        self._matrix = np.zeros((self._width, self._height + self._height_padding))

        self.lines = 0
        self.score = 0

        self.queue = []

    @property
    def level(self):
        return self.lines // self._lines_per_level

    @property
    def lock_delay(self):
        return self.level

    @property
    def visible_tetrominos(self):
        return self.queue[:self._num_visible_tetrominos]

    def _update_queue(self):
        if len(self.queue) < self._num_visible_tetrominos:
            self.queue.extend(list(tetromino.random_bag()))

    def next_tetromino(self):
        t = self.queue.pop(0)
        self._update_queue()
        return t


