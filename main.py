from PIL import ImageOps, ImageGrab
import pyautogui
import time
import keyboard

screen_coords = (115, 310, 195, 380)
obstacle_coords = (600, 780, 660, 880)


def obstacle_screenshot():
    img = ImageGrab.grab(bbox=obstacle_coords)
    gray_img = ImageOps.grayscale(img)
    obstacle_sum = sum(map(sum, gray_img.getcolors()))
 #   print(obstacle_sum)
    return obstacle_sum


def screen_screenshot():
    screen = ImageGrab.grab(bbox=screen_coords)
    gray_screen = ImageOps.grayscale(screen)
    screen_sum = sum(map(sum, gray_screen.getcolors()))
#    print(screen_sum)
    return screen_sum


def game():
    while True:
        obstacle = obstacle_screenshot()
        screen = screen_screenshot()
        if keyboard.is_pressed("q"):
            break
        if screen == 5855:
            if obstacle != 6255:
                pyautogui.press("space")
                time.sleep(0.1)
        elif screen == 5633:
            if obstacle != 6033:
                pyautogui.press("space")
                time.sleep(0.1)


#  time.sleep(5)
#  obstacle_screenshot()  # 6255=Light mode,  6033=Dark mode
#  screen_screenshot()  # 5855=Light mode, 5633=Dark mode
game()
