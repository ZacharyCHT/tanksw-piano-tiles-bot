import keyboard
import pyautogui
import win32api
import win32con
from pyautogui import *
import sys


# This function moves the cursor to the x and y coordinates supplied as arguments and clicks there for a given amount
# of time
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)

    # Leave the left mouse button down for this amount of time in seconds
    # This was a good delay on my computer, it allows me to beat it in roughly 6 seconds
    time.sleep(0.04)

    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def main():
    # Alt-Tab back to the game before this time limit is up otherwise it will automatically exit
    time.sleep(2)

    # Here we set the RGB value for the color of the tiles we want to press
    black = (17, 17, 17)

    # Here we set the location of the black tiles we want to click
    tiles = [(800, 700), (900, 700), (1000, 700), (1100, 700)]

    # Here we set the RGB value of a yellow tile so we can start the game
    yellow_tile = (800, 800)

    # Here we check the location of where our yellow tile is supposed to be and if it is yellow then we
    # 1) Print that the yellow tile was found,
    # 2) Search through the locations of the tiles we set
    # 3) If one is black then we announce that we are clicking it, if it is not then we announce that as well
    # 4) We click the one that is black
    # If the yellow tile was not found then we announce that and exit the program to prevent losing control of your PC
    # NOTE:
    # If you are unaware of what the asterisk does in the following function, it is dereferencing the yellow tile tuple
    # so that we can work with its contents
    # At the time of writing this, I am not sure why this is necessary but it did not work otherwise
    if pyautogui.pixelMatchesColor(*yellow_tile, (249, 231, 23)):
        print("Yellow tile found")
        for tile in tiles:
            if pyautogui.pixelMatchesColor(*tile, black):
                print(f"Clicking {tile}")
                click(*tile)
            else:
                print(f"{tile} not black")
    else:
        print("Yellow tile not found, exiting...")
        sys.exit()

    # This is the main loop of the program and it can be broken by pressing the 'Q' key
    # Dereferencing is used here as well
    while not keyboard.is_pressed('q'):
        for tile in tiles:
            if pyautogui.pixelMatchesColor(*tile, black):
                click(*tile)
                # This is pretty spammy so it is commented out
                # print(f"Clicking tile: {tile}")


# If this python file is the first in the execution sequence then it is allowed to run
if __name__ == "__main__":
    main()
