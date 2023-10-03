import pyautogui as pa
print('Press ctrl-C to quit.')
try:
    while True:
        #TODO: Get and print the mouse coordinates
        x,y = pa.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        pixelColor = pa.screenshot().getpixel((x, y))
        positionStr += ' RGB: (' + str(pixelColor[0]).rjust(3)
        positionStr += ', ' + str(pixelColor[1]).rjust(3)
        positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')'
        print(positionStr, end='')
        print('\b' * len(positionStr), end = '', flush=True)
        
except KeyboardInterrupt:
    print('\nDone.')




