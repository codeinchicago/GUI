import pyautogui as pa, time

print(pa.size())

width, height = pa.size()

for i in range(3):
    # pyautogui.moveTo(100,100, duration = .25)
    # pyautogui.moveTo(200,100, duration = .25)
    # pyautogui.moveTo(200,200, duration = .25)
    # pyautogui.moveTo(100,200, duration = .25)

    # pyautogui.moveTo(100,100, duration = 0.5)
    # pyautogui.moveTo(200,100, duration = 0.5)
    # pyautogui.moveTo(200,200, duration = 0.5)
    # pyautogui.moveTo(100,200, duration = 0.5)
    pass

#Where is the mouse right now

#Testing clicking
#pa.click(100,500)
#time.sleep(3)
#pa.scroll(-2000)

# pa.click(100, 100)
# pa.typewrite(['a', 'B', 'left', 'left', 'z','y'], .25)

# pa.locateOnScreen('submit.png')

# pa.center((643, 745, 70, 29))
# pa.click((678, 759))

# pa.hotkey('ctrl', 'c')
#Presses buttons in order, then releases them.


time.sleep(5)
location = pa.locateOnScreen('submit.png')

print(location[0])