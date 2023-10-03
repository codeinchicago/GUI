import pyautogui as pa, time

nameField = (850, 371)
submitButton = (705, 964)
submitButtonColor = (130, 130, 130)
submitAnotherLink = (776, 205)

formData = [{'name': 'Alpha', 'fear': 'perms', 'source': 'wand', 'robocop': 4, 'comments': 'None.' },
{'name': 'Beta', 'fear': 'allergies', 'source': 'amulet', 'robocop': 2, 'comments': 'Dabu.' }
]

pa.Pause = 0.5

#Modification: search for where the first instance of the color match is, declare that to be the submit button.

for person in formData:
    print(' Pause to let user cancel by pressing CTRL-C')
    time.sleep(5)
    print('Starting')

    print(submitButton[0], submitButton[1], submitButtonColor)
    sc = pa.screenshot()
    print(705, 964, sc.getpixel((705, 964)))
    print(pa.pixelMatchesColor(submitButton[0], submitButton[1], submitButtonColor))

    while not pa.pixelMatchesColor(submitButton[0], submitButton[1], submitButtonColor):
        time.sleep(0.5)
    

    #Name field
    print(f'Entering {person["name"]} info')
    pa.click(nameField[0], nameField[1])
    pa.typewrite(person['name'] + '\t')
    pa.typewrite(person['fear'] + '\t')

    #Source field
    if person['source'] == 'wand':
        pa.typewrite(['down', '\t'])
    elif person['source'] == 'amulet':
        pa.typewrite(['down', 'down', '\t'])

    #Robocop field
    if person['robocop'] == 1:
        pa.typewrite([' '], '\t')
    elif person['robocop'] == 2:
        pa.typewrite(['right'], '\t')
    elif person['robocop'] == 3:
        pa.typewrite(['right','right'], '\t')
    elif person['robocop'] == 4:
        pa.typewrite(['right','right','right'], '\t')
    elif person['robocop'] == 5:
        pa.typewrite(['right','right','right','right'], '\t')

    #Comments
    pa.typewrite(person['comments'] + '\t')
    pa.press('enter')

    print('Submitted.')
    time.sleep(5)

    pa.click(submitAnotherLink[0], submitAnotherLink[1])