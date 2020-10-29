SCORE_DICT = {
    "SINGLE": 100,
    "DOUBLE": 300,
    "TRIPLE": 400,
    "TETRIS": 800,

    "TSPIN_MINI_NO_LINES": 100,
    "TSPIN_NO_LINES": 400,
    "TSPIN_MINI_SINGLE": 200,
    "TSPIN_SINGLE": 800,
    "TSPIN_MINI_DOUBLE": 400,
    "TSPIN_DOUBLE": 1200,
    "TSPIN_TRIPLE": 1600,
}


B2B_DICT = {
    "SINGLE": False,
    "DOUBLE": False,
    "TRIPLE": False,
    "TETRIS": True,

    "TSPIN_MINI_NO_LINES": True,
    "TSPIN_NO_LINES": True,
    "TSPIN_MINI_SINGLE": True,
    "TSPIN_SINGLE": True,
    "TSPIN_MINI_DOUBLE": True,
    "TSPIN_DOUBLE": True,
    "TSPIN_TRIPLE": True
}


def score(action: str, lvl: int, combo_num: int = 0, is_b2b: bool = False) -> float:
    """
    Calculates the score of a given action.
    :param action: The action occurring
    :param lvl: The current level.
    :param combo_num: The current combo amount.
    :param is_b2b: IF this is a back to back event.
    :return: THe resulting score
    """
    return (SCORE_DICT[action] * (1.5 if is_b2b else 1) + 50 * combo_num) * lvl

