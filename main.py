import pyautogui
import time

# Capture User's Screen for Dimensions
screenCapture = pyautogui.screenshot()
screenWidth, screenHeight = screenCapture.size
print(f'Screen Width: {screenWidth} Screen Height: {screenHeight}')

# Collect User's Mouse Position
mouseXPosition, mouseYPosition = pyautogui.position()
print(f'X: {mouseXPosition} Y: {mouseYPosition}')


# Open Commmand Prompt (CMD)
pyautogui.hotkey('win','r')
pyautogui.write('cmd', interval=0.05)
pyautogui.press('enter')

# Open Google
time.sleep(1)
pyautogui.write('explorer "https://google.com"')
pyautogui.press('enter')

# Open Search Bar
time.sleep(2)
pyautogui.click(1201,134)
pyautogui.write('The Minions are Hacking You')
pyautogui.press('enter')

# Open Images
time.sleep(1)
pyautogui.click(455,477)

# Open Random Browsers and Alerts
time.sleep(2)
pyautogui.alert('Program is Starting...')

time.sleep(2)

counter = 0
while counter < 25:
    pyautogui.hotkey('ctrl', 'n')
    counter += 1

# Alert User that Program is Stopping
pyautogui.alert('Program is Stopping')

