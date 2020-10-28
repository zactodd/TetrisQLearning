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


def score(action, lvl, combo_num=0, is_b2b=False):
    return (SCORE_DICT[action] * (1.5 if is_b2b else 1) + 50 * combo_num) * lvl
