from PIL import ImageGrab
import time, pyautogui, random

import keyboard


def Pixel(X, Y, image):
    return image.getpixel((X, Y))


def LumberJack():
    bbox_from = (363, 607)
    bbox_end = (598, 613)
    image_bbox = [bbox_from[0], bbox_from[1], bbox_end[0], bbox_end[1]]

    scoreX = 500
    # scoreX = int(sys.argv[1])
    Score = 0
    time.sleep(2)
    pyautogui.press(' ')

    while Score < scoreX:

        picture_begin = time.time()
        image = ImageGrab.grab(image_bbox)
        picture_end = time.time()

        time_delta=picture_end-picture_begin


        Left = Pixel(0, 0, image)
        Right = Pixel(image._size[0] - 1, image._size[1] - 1, image)

        # time.sleep(0.5)

        if Right[0] < Left[0]:
            print("L")
            # pyautogui.press('left', 2, random.choice([0.09, 0.10]))

            start_time = time.time()

            # time.sleep(0.10)
            # keyboard.send('left')
            keyboard.press('left')
            keyboard.release('left')
            # time.sleep(0.2)
            # keyboard.press('left')
            # keyboard.release('left')
            time.sleep(0.5)

            # keyboard.press('left')
            # keyboard.release('left')
            # time.sleep(0.10)
            # keyboard.send('left')

            end_time = time.time()
        else:
            # pyautogui.press('right', 2, random.choice([0.09, 0.10]))
            print("R")
            start_time = time.time()
            # time.sleep(0.10)

            keyboard.press('right')
            keyboard.release('right')
            # time.sleep(0.2)
            # keyboard.press('right')
            # keyboard.release('right')
            time.sleep(0.5)

            # keyboard.press('right')
            # keyboard.release('right')
            
            # keyboard.send('right')
            # time.sleep(0.10)
            # keyboard.send('right')
            end_time = time.time()
        Score += 2


        # print(str(end_time-start_time))


if __name__ == '__main__':
    LumberJack()
