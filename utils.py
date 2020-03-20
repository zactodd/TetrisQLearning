import cv2
import numpy as np
from PIL import ImageGrab
import win32gui

BOARD_COLOUR = np.array([35, 35, 36])
BOARD_HEIGHT, BOARD_WIDTH = 20, 10
EMPTY_BOARD = np.zeros((BOARD_HEIGHT, BOARD_WIDTH))
TETROMINOES_COLOURS = {
    "i": [116, 98, 0],
    "o": [0, 102, 116],
    "t": [127, 0, 106],
    "j": [127, 67, 0],
    "l": [0, 85, 127],
    "s": [35, 127, 0],
    "z": [0, 0, 116]
}


def board_matrix(image):
    """
    Obtains a the board matrix from an image of the game.
    :param image:
    :return:
    """
    rows, cols, _ = image.shape
    board = EMPTY_BOARD.copy()
    board_mask = cv2.inRange(image, BOARD_COLOUR, BOARD_COLOUR)
    contours, _ = cv2.findContours(board_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt = max(contours, key=cv2.contourArea)
    board_x, board_y, board_w, board_h = cv2.boundingRect(cnt)

    for colour in TETROMINOES_COLOURS.values():
        bgr_color = np.array(colour)
        mask = cv2.inRange(image, bgr_color, bgr_color)
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            block_width, block_height = board_w // BOARD_WIDTH, board_h // BOARD_HEIGHT
            for board_row in range(BOARD_HEIGHT):
                for board_col in range(BOARD_WIDTH):
                    block_x = block_width * board_col
                    block_y = block_height * board_row
                    if board_x + block_x <= x < board_x + block_x + block_width and \
                            board_y + block_y <= y < board_y + block_y + block_height:
                        board[board_row, board_col] = 1
    return board


def game_image():
    """
    Obtains a screenshot of the current game state.
    :return:
    """
    windows_list = []

    def enum_win(hwnd, result):
        win_text = win32gui.GetWindowText(hwnd)
        windows_list.append((hwnd, win_text))

    win32gui.EnumWindows(enum_win, [])

    for hwnd, win_text in windows_list:
        if "Play Tetris" in win_text:
            position = win32gui.GetWindowRect(hwnd)
            screenshot = ImageGrab.grab(position)
            return cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    raise Exception("Game Not Found")


