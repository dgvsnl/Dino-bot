import pyautogui
from PIL import Image, ImageGrab
# from numpy import asarray
import time


def hit(key):
    pyautogui.keyDown(key)
    return


def isCollide(data):

    for i in range(790, 810):
        for j in range(375, 390):
            if data[i, j] < 100:
                hit("down")
                return

    for i in range(790, 810):
        for j in range(400, 415):
            if data[i, j] < 100:
                hit("up")
                return
    return

if __name__ == "__main__":
    time.sleep(1)
    print("Hey user can take over your computer..")
    time.sleep(1)
    pyautogui.click(157,844)
    if input() == "why":
        time.sleep(1)
        print("because I m bored and want to play DINO on chrome..")
        if input() == "sure":
            time.sleep(1)
            print("taking control initiated...")

    time.sleep(5)
    pyautogui.click(661,1062)
    time.sleep(1)
    pyautogui.click(759,16)
    time.sleep(1)
    pyautogui.click(747, 50)
    time.sleep(2)
    pyautogui.typewrite("http://www.trex-game.skipser.com/")
    time.sleep(1)
    pyautogui.typewrite(['Enter'])

    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(4)
    pyautogui.click(954,399)
    hit("up")

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)

        # print(asarray(image))
'''
        # Draw the rectangle for cactus
        for i in range(755, 800):
            for j in range(400, 421):
                data[i, j] = 0

        # Draw the rectangle for birds
        for i in range(755, 800):
            for j in range(370, 390):
                data[i, j] = 171

        image.show()
        break

'''
