import pyautogui
import time
from PIL import Image
from pynput.keyboard import Key, Controller

def get_color(x, y):
    # Get the pixel color at the specified coordinates
    screenshot = pyautogui.screenshot()
    pixel_color = screenshot.getpixel((x, y))
    del screenshot
    return pixel_color

def approach_legendary(keyboard):
    keyboard.press('w')
    time.sleep(0.1)
    keyboard.press('w')
    time.sleep(0.3)

def process_pixel(x, y):
        
    normal_Color = get_color(x, y)
    pixel_color = normal_Color
    print("Standard non-shiny colour:", normal_Color)
    
    keyboard = Controller()

    counter = 1

    while pixel_color == normal_Color:
        print(str(counter) + ".", "Detected Colour:", pixel_color, "- Standard.")
        counter += 1

        #perform soft reset
        keyboard.press('f')
        keyboard.press(Key.space)
        keyboard.press('x')
        keyboard.press('z')
 
        time.sleep(0.2)

        keyboard.release('f')
        keyboard.release(Key.space)
        keyboard.release('x')
        keyboard.release('z')

        time.sleep(0.2)

        for i in range(1, 4):
            time.sleep(0.3)
            keyboard.press('f')
            time.sleep(0.2)
            keyboard.release('f')

        #''' uncomment this part if player has to 'approach' legendary (eg. kyogre and groudon)
        approach_legendary(keyboard)
        #'''

        #change so that it gives enough time for the encounter animation
        time.sleep(1.3)

        pixel_color = get_color(x, y)

    print(str(counter) + ".", "Detected Colour:", pixel_color, "- SHINY DETECTED!!!")

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
