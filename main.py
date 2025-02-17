import cv2
import pyscreeze
import pyautogui
import numpy as np


def game_on():
    while True:
        screenshot = pyautogui.screenshot(region=(200, 650, 600, 300))  # region=(200, 650, 600, 300)
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2RGB)

        img = ["tree.png", "tree1.png", "little_tree.png", "little_tree1.png", "bird.png", "bird1.png"]
        blocks_generate = [pyautogui.locateAllOnScreen(i, confidence=0.9) for i in img]
        try:
            for blocks in blocks_generate:
                for block in blocks:
                    print(block)
                    if block.left <= 900:
                        pyautogui.press("Space")

        except pyscreeze.ImageNotFoundException:
            continue
        cv2.imshow('Screenshot', screenshot)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


game_on()
