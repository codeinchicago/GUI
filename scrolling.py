import pyautogui as pa
im = pa.screenshot()

print(im.getpixel((0,0)))

print(im.getpixel((50,200)))

print()

print(pa.pixelMatchesColor(0,0, (232, 234, 237)))
#x,y coordinates to be checked, then the color to match

print(pa.pixelMatchesColor(50,50, (251, 251, 250)))