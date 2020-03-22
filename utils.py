import sys
import os
import time
import cv2
import numpy as np
from PIL import ImageGrab
import win32gui
import exceptions
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


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
    board_rect = cv2.boundingRect(cnt)

    for t in TETROMINOES_COLOURS:
        board = find_tetromino(t, image, board_rect, board)
    return board


def find_tetromino(tetromino, image, board_rect, board=EMPTY_BOARD.copy()):
    """
    Obtaines the a matrix containing the postions of all the tetromino :param tetromino
    :param tetromino: the tetrom to find.
    :param image:
    :param board_rect: the x, y, w, h: x and y being the the top left corner coords and
        w, h being the width and height of the rectangle.
    :param board:A board to update if an existing board exist other wise creates an empty board.
    :return:
    """
    board_x, board_y, board_w, board_h = board_rect
    colour = np.array(TETROMINOES_COLOURS[tetromino])
    mask = cv2.inRange(image, colour, colour)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        x, y, *_ = cv2.boundingRect(cnt)
        block_width, block_height = board_w // BOARD_WIDTH, board_h // BOARD_HEIGHT
        position_x, position_y = block_width + board_x, block_height + board_y
        for board_row in range(BOARD_HEIGHT):
            for board_col in range(BOARD_WIDTH):
                block_x, block_y = block_width * board_col, block_height * board_row
                if board_x + block_x <= x < block_x + position_x and board_y + block_y <= y < block_y + position_y:
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
    raise exceptions.GameNotFoundException()


def game_images(wait=0.25):
    """
    Yields a continuous stream of game images at a specified interval.
    :param wait: wait time in seconds.
    """
    while True:
        yield game_image()
        time.sleep(wait)


def get_chrome_driver():
    """
    Installs the chrome driver if already installed gets the drivers path.
    :return: The driver.
    """
    sys.stdout = open(os.devnull, 'w')
    try:
        path = ChromeDriverManager().install()
    except PermissionError as e:
        if e.errno != 13:
            raise e
        path = e.filename
    finally:
        sys.stdout = sys.__stdout__
    return webdriver.Chrome(path)


