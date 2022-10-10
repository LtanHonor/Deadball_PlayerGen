import PySimpleGUI as sg
import sys
import random
import webbrowser

#layout = [[sg.Text("Collin is a goof")], [sg.Button("OK")]]

with open('firstNames.txt',encoding = 'utf-8') as f_fNames:
    firstNames = f_fNames.readlines()
f_fNames.close()
firstNames = [x[:-1] for x in firstNames]
with open('surnames.txt',encoding = 'utf-8') as f_sNames:
    secondNames = f_sNames.readlines()
f_sNames.close()
secondNames = [x[:-1] for x in secondNames]

positions = [
    "Utility",
    "Catcher",
    "First Base",
    "Second Base",
    "Third Base",
    "Shortstop",
    "Left Field",
    "Center Field",
    "Right Field",
    "Starting Pitcher",
    "Starting Pitcher",
    "Starting Pitcher",
    "Starting Pitcher",
    "Starting Pitcher",
    "Starting Pitcher",
    "Relief Pitcher",
    "Relief Pitcher",
    "Relief Pitcher",
    "Relief Pitcher",
    "Relief Pitcher"
]

pTraits = [
    "None",
    "None",
    "None",
    "CN-",
    "None",
    "None",
    "None",
    "None",
    "None",
    "None",
    "None",
    "None",
    "None",
    "K+",
    "GB+",
    "CN+",
    "ST+"
]

pDiceMod = [
    "d12",
    "d8",
    "d8",
    "d4",
    "d4",
    "d4",
    "d4",
    "-d4",
    "-d4",
    "-d4"
]

pDiceAnch = [
    "d20",
    "d12",
    "d12",
    "d8",
    "d8",
    "d6",
    "d6",
    "d4",
    "d4",
    "No Dice!",
    "-d4",
    "-d4",
    "-d8"
]

pHanded = [
    "Right Handed",
    "Right Handed",
    "Right Handed",
    "Right Handed",
    "Right Handed",
    "Right Handed",
    "Left Handed",
    "Left Handed",
    "Left Handed",
    "Switch Hitter (Pitchers: Left Handed)"
]

bTraits = [
    "P--",
    "P-",
    "S-",
    "C-",
    "D-",
    "None",
    "None",
    "None",
    "None",
    "None",
    "None",
    "None",
    "None",
    "P+",
    "D+",
    "C+",
    "S+",
    "T+",
    "P++"
]

f_0pen = open("PlayerPool.csv", "a")

sg.theme('DarkBlue8')   # Add a touch of color
# All the stuff inside your window.

textList = [
    [sg.Text("Player Name: ", size=(12,1)), sg.Text('', key='-1stNAMES-'),sg.Text('', key='-2ndNAMES-')],
    [sg.Text("Player Position: ", size=(12,1)), sg.Text('', key='-POSITION-')],
    [sg.Text("Left or Right: ", size=(12,1)), sg.Text("", key='-PHANDED-')],
    [sg.Text("Batter Target: ", size=(12,1)), sg.Text("", key='-BT-')],
    [sg.Text("On Base Target: ", size=(12,1)), sg.Text("", key='-OBT-')],
    [sg.Text("Pitching Trait: ", size=(12,1)), sg.Text("", key='-PTRAITS-')],
    [sg.Text("Pitching Die: ", size=(12,1)), sg.Text("", key='-PDICE-')],
    [sg.Text("Batting Trait: ", size=(12,1)), sg.Text("", key='-BTRAITS-')],
]

layout = [
    [sg.Push(),
     sg.Text("Select for \"Ancient\" Players"),
     sg.Checkbox('Ancient Era', default=False, key='-ERA-')],
    [sg.Column(textList, element_justification='l', expand_x=True)],
    [sg.VPush()],
    [sg.Button("Close"),sg.Push(),
     sg.Button("Randomize", bind_return_key=True),
     sg.Button("Save Player")],
    [sg.Button('Deadball by W.M. Akers', key = 'LINK1')]
]

window = sg.Window("Deadball Player Creator", layout, element_justification='l', size=(900, 600), resizable=True, return_keyboard_events=True)

while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == sg.WIN_CLOSED:
        break

    if event in ('LINK1', 'LINK2'):
        webbrowser.open("https://www.drivethrurpg.com/product/395133/Deadball-Baseball-With-Dice-Second-Edition")

    if event == "Save Player":
        if "Batter" in randomPtraits:
            outputPtraits = ""
        elif "None" in randomPtraits:
            outputPtraits = ""
        else:
            outputPtraits = randomPtraits
        if "Pitcher" in randompos:
            outputPdice = randomPdice
        else:
            outputPdice = ""

        print(outputPdice)
        if outputPdice == "-d4":
            outputPdice = " -d4"
        elif outputPdice == "-d8":
            outputPdice = " -d8"

        if "Pitchers:" in randompHanded:
            if "Pitcher" in randompos:
                outputpHanded = "L"
            else:
                outputpHanded = "S"
        elif "Left" in randompHanded:
            outputpHanded = "L"
        else:
            outputpHanded = "R"
        if "None" in randomBtraits:
            outputBtraits = ""
        else:
            outputBtraits = randomBtraits

        f_0pen.write(prename+" " +surname+","+randompos+","+outputpHanded+","+str(randomBT)+","+str(randomOBT)+","+outputBtraits+","+outputPtraits+","+outputPdice+"\n")

    if event == "Randomize" or values == "":
        farmhandCheck = random.randint(1,100)
        if (farmhandCheck > 25):
            randomBT = random.randint(2,20) + 15
        else:
            randomBT = random.randint(2,20) + 12
        #print(randompos)
        window['-BT-'].update(randomBT)

        randomOBT = random.randint(2,8) + randomBT
        #print(randomPtraits)
        window['-OBT-'].update(randomOBT)

        randompos = random.choice(positions)
        #print(randomPtraits)
        window['-POSITION-'].update(randompos)

        prename = random.choice(firstNames)
        #print(randomPtraits)
        window['-1stNAMES-'].update(prename)
        surname = random.choice(secondNames)
        #print(randomPtraits)
        window['-2ndNAMES-'].update(surname)

        # sg.popup('You entered', randompos)

        if "Pitcher" in randompos:
            randomPtraits = random.choice(pTraits)
            if values["-ERA-"] == True:
                randomPdice = random.choice(pDiceAnch)
            else:
                randomPdice = random.choice(pDiceMod)
            #print(randomPtraits)
        else:
            randomPtraits = "Batter Only"
            randomPdice = "Batter Only"
        window['-PDICE-'].update(randomPdice)
        window['-PTRAITS-'].update(randomPtraits)

        randomBtraits = random.choice(bTraits)
        #print(randomPtraits)
        window['-BTRAITS-'].update(randomBtraits)

        randompHanded = random.choice(pHanded)
        #print(randomPtraits)
        window['-PHANDED-'].update(randompHanded)

    if event == "Close" or event == sg.WIN_CLOSED:
        f_0pen.close()
        break
window.close()
f_0pen.close()
