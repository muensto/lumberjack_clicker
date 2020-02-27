from PIL import ImageGrab
import time, pyautogui, random


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

        image = ImageGrab.grab(image_bbox)

        Left = Pixel(0, 0, image)
        Right = Pixel(image._size[0] - 1, image._size[1] - 1, image)

        if Right[0] < Left[0]:
            pyautogui.press('left', 2, 0.09)
        else:
            pyautogui.press('right', 2, 0.09)
        Score += 2


if __name__ == '__main__':
    Lumberjack()
