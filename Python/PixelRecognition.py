import pyautogui
from pynput import keyboard
import time

exit_loop = False
def on_press(key):
    global exit_loop
    if key == keyboard.Key.esc:
        exit_loop = True
        return False  # Stop listener

listener = keyboard.Listener(on_press=on_press)
listener.start()
while not exit_loop:
    x,y = pyautogui.position()
    color = pyautogui.pixel(x, y)
    print(f"RGB color at ({x}, {y}): {color}")
    time.sleep(0.5)

listener.stop()