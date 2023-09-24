import pyautogui as pa, time
time.sleep(5)
pa.click() #click to put drawing program into focus
distance = 200
duration = 0.2
while distance > 0:
    pa.dragRel(distance, 0, duration) #Right
    distance = distance -5
    pa.dragRel(0, distance, duration) #Down
    pa.dragRel(-distance, 0, duration) #Left
    distance = distance - 5
    pa.dragRel(0, -distance, duration) #Up
