from PIL import Image
import pyautogui

screenshot = pyautogui.screenshot(region=(0, 600, 1900, 500))
screenshot.show()

pyautogui.press("space")
pyautogui.keyDown("down")
pyautogui.keyUp("down")

