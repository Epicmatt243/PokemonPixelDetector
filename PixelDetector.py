import pyautogui
import time
from PIL import Image
from pynput.keyboard import Key, Controller

import pygetwindow as gw

def get_colour(x, y):
    # Get the pixel color at the specified coordinates
    screenshot = pyautogui.screenshot()
    pixel_colour = screenshot.getpixel((x, y))
    del screenshot
    return pixel_colour

def approach_legendary(keyboard):
    gw.getWindowsWithTitle('BlueStacks App Player')[0].activate()
    keyboard.press('w')
    time.sleep(0.1)
    gw.getWindowsWithTitle('BlueStacks App Player')[0].activate()
    keyboard.release('w')
    time.sleep(0.3)

def process_pixel(x, y):
        
    normal_Colour = get_colour(x, y)
    pixel_colour = normal_Colour
    print("Standard non-shiny colour:", normal_Colour)
    
    keyboard = Controller()

    counter = 1

    while pixel_colour == normal_Colour:
        print(str(counter) + ".", "Detected Colour:", pixel_colour, "- Standard.")
        counter += 1

        #perform soft reset
        gw.getWindowsWithTitle('BlueStacks App Player')[0].activate()
        keyboard.press('f')
        keyboard.press(Key.space)
        keyboard.press('x')
        keyboard.press('z')
 
        time.sleep(0.2)

        gw.getWindowsWithTitle('BlueStacks App Player')[0].activate()
        keyboard.release('f')
        keyboard.release(Key.space)
        keyboard.release('x')
        keyboard.release('z')

        time.sleep(0.2)

        for i in range(1, 4):
            time.sleep(0.3)
            gw.getWindowsWithTitle('BlueStacks App Player')[0].activate()
            keyboard.press('f')
            time.sleep(0.2)
            gw.getWindowsWithTitle('BlueStacks App Player')[0].activate()
            keyboard.release('f')

        ''' uncomment this part if player has to 'approach' legendary (eg. kyogre and groudon)
        approach_legendary(keyboard)
        '''

        #change so that it gives enough time for the encounter animation
        time.sleep(1.4)

        pixel_colour = get_colour(x, y)

    print(str(counter) + ".", "Detected Colour:", pixel_colour, "- SHINY DETECTED!!!")

def main():
    
    print("Hover your mouse over the exact location you would like to monitor for shiny pokemon...")
    time.sleep(1)
    print("Make sure you click on window...")
    time.sleep(3)
    
    for i in range(5, 0, -1):
        print("Starting in", i, "...")
        time.sleep(1)

    current_position = pyautogui.position()
    print('Monitoring (', current_position[0], ',', current_position[1], ')')

    process_pixel(current_position[0], current_position[1])

if __name__ == "__main__":
    main()
    