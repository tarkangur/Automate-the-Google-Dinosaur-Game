from PIL import Image, ImageGrab
import pyautogui
import time


def screenshot():
    ss = ImageGrab.grab(bbox=(400, 600, 600, 900)).convert("L")
    return ss


def dark_theme(ss):
    ss_data = ss.load()
    if ss_data[0, 0] < 50:
        return True
    elif 170 <= ss_data[0, 0] < 200:
        return False


def check_obstacle(theme, ss):
    ss_data = ss.load()


def game():
    while True:
        ss = screenshot()
        theme = "Dark" if dark_theme(ss) else "Light"
        check_obstacle(theme, ss)
        time.sleep(0.1)


time.sleep(5)
#game()
