import numpy as np
from typing import Type
from game import tetromino


class Board:
    def __init__(self):
        self._lines_per_level = 10
        self._max_level = 30
        self._width = 10
        self._height = 20
        self._height_padding = 5
        self._num_visible_tetrominos = 3

        self._matrix = np.zeros((self._width, self._height + self._height_padding))

        self.lines = 0
        self.score = 0

        self._have_b2b = False
        self._combo = 0

        self.queue = []
        self.tetromino = self.next_tetromino()

    @property
    def level(self) -> int:
        return self.lines // self._lines_per_level

    @property
    def lock_delay(self) -> float:
        return self.level

    @property
    def visible_tetrominos(self) -> list:
        return self.queue[:self._num_visible_tetrominos]

    def _update_queue(self) -> None:
        if len(self.queue) < self._num_visible_tetrominos:
            self.queue.extend(list(tetromino.random_bag()))

    def next_tetromino(self) -> tetromino.Tetromino:
        self._update_queue()
        t = self.queue.pop(0)
        return t()

    def is_game_finished(self) -> bool:
        pass

    def update_board(self) -> None:
        pass

    def _determine_action(self):
        lines_cleared = len(np.where((self._matrix == 1).all(axis=1))[0])

        if lines_cleared == 0:
            if self.tetromino.name != "T":
                return None
            else:
                pass
        elif lines_cleared == 1:
            if self.tetromino.name != "T":
                return "SINGLE"
            else:
                return
        elif lines_cleared == 2:
            if self.tetromino.name != "T":
                return "DOUBLE"
            else:
                ...
        elif lines_cleared == 3:
            if self.tetromino.name != "T":
                return "TRIPLE"
            else:
                ...
        elif lines_cleared == 4:
            return "TETRIS"
