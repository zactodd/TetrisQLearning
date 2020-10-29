import numpy as np
from typing import Tuple
from abc import ABC, abstractmethod


class Tetromino(ABC):
    def __init__(self):
        self.matrix = self._base_matrix.copy()

    @property
    @abstractmethod
    def _base_matrix(self) -> np.ndarray:
        return None

    @property
    @abstractmethod
    def colour(self) -> Tuple[int, int, int]:
        return None

    @property
    @abstractmethod
    def name(self) -> str:
        return None

    def clockwise_rotation(self):
        self.matrix = np.rot90(self.matrix)

    def anticlockwise_rotation(self):
        self.matrix = np.rot90(self.matrix, 3)


class L(Tetromino):
    def __init__(self):
        super().__init__()

    @property
    def _base_matrix(self) -> np.ndarray:
        return np.asarray([
            [0, 0, 1],
            [1, 1, 1],
            [0, 0, 0]
        ])

    @property
    def colour(self) -> Tuple[int, int, int]:
        return 255, 151, 28

    @property
    def name(self) -> str:
        return "L"


class J(Tetromino):
    def __init__(self):
        super().__init__()

    @property
    def _base_matrix(self) -> np.ndarray:
        return np.asarray([
            [1, 0, 0],
            [1, 1, 1],
            [0, 0, 0]
        ])

    @property
    def colour(self) -> Tuple[int, int, int]:
        return 3, 65, 174

    @property
    def name(self) -> str:
        return "J"


class O(Tetromino):
    def __init__(self):
        super().__init__()

    @property
    def _base_matrix(self) -> np.ndarray:
        return np.asarray([
            [1, 1],
            [1, 1]
        ])

    @property
    def colour(self) -> Tuple[int, int, int]:
        return 255, 213, 0

    @property
    def name(self) -> str:
        return "O"


class S(Tetromino):
    def __init__(self):
        super().__init__()

    @property
    def _base_matrix(self) -> np.ndarray:
        return np.asarray([
            [0, 1, 1],
            [1, 1, 0],
            [0, 0, 0]
        ])

    @property
    def colour(self) -> Tuple[int, int, int]:
        return 114, 203, 59

    @property
    def name(self) -> str:
        return "S"


class Z(Tetromino):
    def __init__(self):
        super().__init__()

    @property
    def _base_matrix(self) -> np.ndarray:
        return np.asarray([
            [1, 1, 0],
            [0, 1, 1],
            [0, 0, 0]
        ])

    @property
    def colour(self) -> Tuple[int, int, int]:
        return 255, 50, 19

    @property
    def name(self) -> str:
        return "Z"


class T(Tetromino):
    def __init__(self):
        super().__init__()

    @property
    def _base_matrix(self) -> np.ndarray:
        return np.asarray([
            [0, 1, 0],
            [1, 1, 1],
            [0, 0, 0]
        ])

    @property
    def colour(self) -> Tuple[int, int, int]:
        return 191, 0, 255

    @property
    def name(self) -> str:
        return "T"


class I(Tetromino):
    def __init__(self):
        super().__init__()

    @property
    def _base_matrix(self) -> np.ndarray:
        return np.asarray([
            [1, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ])

    @property
    def colour(self) -> Tuple[int, int, int]:
        return 26, 244, 244

    @property
    def name(self) -> str:
        return "I"


def random_bag() -> np.ndarray:
    bag = np.asarray((L, J, S, Z, O, T, I))
    np.random.shuffle(bag)
    return bag
