from PIL import ImageGrab
import time, pyautogui, random
from ctypes import windll


def get_color(rgb):
    r = rgb & 0xff
    g = (rgb >> 8) & 0xff
    b = (rgb >> 16) & 0xff
    return r, g, b


def get_pixel(x, y):  # Modify class atribute
    screen = windll.user32.GetDC(0)
    rgb = windll.gdi32.GetPixel(screen, x, y)
    return get_color(rgb)

def Pixel(X, Y, image):
    return image.getpixel((X, Y))


def Lumberjack():
    bbox_from = (363, 607)
    bbox_end = (598, 613)
    image_bbox = [bbox_from[0], bbox_from[1], bbox_end[0], bbox_end[1]]

    scoreX = 500
    # scoreX = int(sys.argv[1])
    Score = 0
    time.sleep(2)
    pyautogui.press(' ')


    while Score < scoreX:

        # image = ImageGrab.grab(image_bbox)
        #
        # Left = Pixel(0, 0, image)
        # Right = Pixel(image._size[0] - 1, image._size[1] - 1, image)
        possible_branch = get_pixel(449, 633)

        if possible_branch == (161, 116, 56):
            pyautogui.press('right', 2, 0.065)

        elif possible_branch == (211, 247, 255) or possible_branch == (241, 252, 255):
            pyautogui.press('left', 2, 0.065)
        # if Right[0] < Left[0]:
        #     pyautogui.press('left', 2, 0.09)
        #
        # else:
        #     pyautogui.press('right', 2, 0.09)

        Score += 2


if __name__ == '__main__':
    Lumberjack()
