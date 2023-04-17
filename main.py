# This is a sample Python script.
import pyautogui
import time

# Set the coordinates where you want to click
x, y = 538, 179

# Set the number of times you want to loop
num_clicks = 125

# Loop through the clicks
for i in range(num_clicks):
    # Click the left mouse button at the given coordinates
    pyautogui.click(x, y)

    # Wait for a brief moment to simulate human-like behavior
    time.sleep(0.05)

    # Press the Enter key
    pyautogui.press('enter')

    # Wait for a brief moment before the next iteration
    time.sleep(1)
