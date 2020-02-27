from PIL import ImageGrab
import time, pyautogui, random
from ctypes import windll


def get_color(rgb):
    r = rgb & 0xff
    g = (rgb >> 8) & 0xff
    b = (rgb >> 16) & 0xff
    return r, g, b


def get_pixel(x, y):
    screen = windll.user32.GetDC(0)
    rgb = windll.gdi32.GetPixel(screen, x, y)
    return get_color(rgb)


def Lumberjack():
    scoreX = 1000
    Score = 0
    time.sleep(2)
    pyautogui.press(' ')

    while Score < scoreX:
        possible_branch = get_pixel(453, 629)

        if possible_branch == (161, 116, 56):
            pyautogui.press('right', 2, 0.055)

        elif possible_branch == (211, 247, 255) or possible_branch == (241, 252, 255):
            pyautogui.press('left', 2, 0.055)

        Score += 2


if __name__ == '__main__':
    Lumberjack()
