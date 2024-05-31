import PySimpleGUI as sg
import sys
import random
import webbrowser
import os
#import threading
#from threading import Thread

csvHeader = "PLAYER NAME,POS,AGE,L/R,BT,OBT,Batter TRAITS, Pitcher TRAITS, Pitcher Die \n"

def randAge(randInput):
    justChecked = [element for element in values if values[element]==True
                   and 'AGE' in element]
    #print(len(justChecked)) # Only the checked box

    if len(justChecked) > 1:
        window['-OPTIONERROR-'].update("\n Only ONE age option is allowed.  Nothing Generated!")
    elif len(justChecked) < 1:
        window['-OPTIONERROR-'].update("\n AT LEAST ONE age option is needed.  Nothing Generated!")
    else:
        window['-OPTIONERROR-'].update("")
        rValue = random.randint(1,6)
        age_dict = {4: 32, 3: 27, 2: 21}
        pAge = age_dict.get(randInput, 18) + rValue
    return pAge

def createPlayer(pAge=None):
    if pAge is None:
        justChecked = [element for element, value in values.items() if value and 'AGE' in element]

        if len(justChecked) > 1:
            window['-OPTIONERROR-'].update("\n Only ONE age option is allowed.  Nothing Generated!")
        elif len(justChecked) < 1:
            window['-OPTIONERROR-'].update("\n AT LEAST ONE age option is needed.  Nothing Generated!")
        else:
            window['-OPTIONERROR-'].update("")
            rValue = random.randint(1,6)
            age_dict = {4: 32, 3: 27, 2: 21}
            pAge = age_dict.get(randInput, 18) + rValue

    randomBT = random.randint(2,20) + (12 if values["-FARM-"] else 15)
    randomOBT = random.randint(2,8) + randomBT

    if values["-FARM-"] == True:
        randomBT = random.randint(2,20) + 12
    else:
        randomBT = random.randint(2,20) + 15

    randomOBT = random.randint(2,8) + randomBT

    randompos = random.choice(positions)

    prename = random.choice(firstNames)
    surname = random.choice(secondNames)

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
    randomBtraits = random.choice(bTraits)
    randompHanded = random.choice(pHanded)
    return randomBT,randomOBT,pAge,randompos,prename,surname,pTraits,pDiceAnch,pDiceMod,randomPdice,randomPtraits,randomBtraits,pHanded,randompHanded;

def checkBatter(randomPtraits):
    if "Batter" in randomPtraits:
        outputPtraits = ""
    elif "None" in randomPtraits:
        outputPtraits = ""
    else:
        outputPtraits = randomPtraits
    return outputPtraits

def checkPitcher(randompos,randomPdice):
    if "Pitcher" in randompos:
        outputPdice = randomPdice
    else:
        outputPdice = ""

    if outputPdice == "-d4":
        outputPdice = " -d4"
    elif outputPdice == "-d8":
        outputPdice = " -d8"
    return outputPdice

def checkHand(randompos,randompHanded):
    if "Pitchers:" in randompHanded:
        if "Pitcher" in randompos:
            outputpHanded = "L"
        else:
            outputpHanded = "S"
    elif "Left" in randompHanded:
        outputpHanded = "L"
    else:
        outputpHanded = "R"
    return outputpHanded

def checkbTraits(randomBtraits):
    if "None" in randomBtraits:
        outputBtraits = ""
    else:
        outputBtraits = randomBtraits
    return outputBtraits

def CreateTeam ():
    thisString = []
    thisString.append("Active Roster \n")
    activePlayers = 8
    StartingPitchers = 5
    ReliefPitchers = 7
    InfieldBench = 2
    OutfieldBench = 2
    CatcherBench = 1
    totalPlayers = activePlayers + StartingPitchers + ReliefPitchers + InfieldBench + OutfieldBench + CatcherBench
    print(totalPlayers)

    justChecked = [element for element in values if values[element]==True
                   and 'AGE' in element]
    return_value = sg.popup_get_file('', no_window=True, save_as=True, default_path='filename', file_types=(("Comma Separated Values","*.csv"),))
    pAge = randAge(random.randint(1,4))
    if len(justChecked) > 1:
        window['-OPTIONERROR-'].update("\n Only ONE age option is allowed.  Nothing Generated!")
    elif len(justChecked) < 1:
        window['-OPTIONERROR-'].update("\n AT LEAST ONE age option is needed.  Nothing Generated!")
    else:
        window['-OPTIONERROR-'].update("")
        thisLoop = totalPlayers
        thisLoop = int(thisLoop)
        thisString = [] # Add this line
        randomBT,randomOBT,pAge,randompos,prename,surname,pTraits,pDiceAnch,pDiceMod,randomPdice,randomPtraits,randomBtraits,pHanded,randompHanded = createPlayer(pAge)
        while randompos != "Left Field":
            randomBT,randomOBT,pAge,randompos,prename,surname,pTraits,pDiceAnch,pDiceMod,randomPdice,randomPtraits,randomBtraits,pHanded,randompHanded = createPlayer(pAge)
        pAge = randAge(random.randint(1,4))
        outputPtraits = checkBatter(randomPtraits)
        outputPdice = checkPitcher(randompos,randomPdice)
        outputpHanded = checkHand(randompos,randompHanded)
        outputBtraits = checkbTraits(randomBtraits)
        thisString.append(prename+" " +surname+","+randompos+","+str(pAge)+","+outputpHanded+","+str(randomBT)+","+str(randomOBT)+","+outputBtraits+","+outputPtraits+","+outputPdice+"\n")
        while randompos != "Center Field":
            randomBT,randomOBT,pAge,randompos,prename,surname,pTraits,pDiceAnch,pDiceMod,randomPdice,randomPtraits,randomBtraits,pHanded,randompHanded = createPlayer(pAge)
        pAge = randAge(random.randint(1,4))
        outputPtraits = checkBatter(randomPtraits)
        outputPdice = checkPitcher(randompos,randomPdice)
        outputpHanded = checkHand(randompos,randompHanded)
        outputBtraits = checkbTraits(randomBtraits)
        thisString.append(prename+" " +surname+","+randompos+","+str(pAge)+","+outputpHanded+","+str(randomBT)+","+str(randomOBT)+","+outputBtraits+","+outputPtraits+","+outputPdice+"\n")
        while randompos != "Catcher":
            randomBT,randomOBT,pAge,randompos,prename,surname,pTraits,pDiceAnch,pDiceMod,randomPdice,randomPtraits,randomBtraits,pHanded,randompHanded = createPlayer(pAge)
        pAge = randAge(random.randint(1,4))
        outputPtraits = checkBatter(randomPtraits)
        outputPdice = checkPitcher(randompos,randomPdice)
        outputpHanded = checkHand(randompos,randompHanded)
        outputBtraits = checkbTraits(randomBtraits)
        thisString.append(prename+" " +surname+","+randompos+","+str(pAge)+","+outputpHanded+","+str(randomBT)+","+str(randomOBT)+","+outputBtraits+","+outputPtraits+","+outputPdice+"\n")
        while randompos != "Right Field":
            randomBT,randomOBT,pAge,randompos,prename,surname,pTraits,pDiceAnch,pDiceMod,randomPdice,randomPtraits,randomBtraits,pHanded,randompHanded = createPlayer(pAge)
        pAge = randAge(random.randint(1,4))
        outputPtraits = checkBatter(randomPtraits)
        outputPdice = checkPitcher(randompos,randomPdice)
        outputpHanded = checkHand(randompos,randompHanded)
        outputBtraits = checkbTraits(randomBtraits)
        thisString.append(prename+" " +surname+","+randompos+","+str(pAge)+","+outputpHanded+","+str(randomBT)+","+str(randomOBT)+","+outputBtraits+","+outputPtraits+","+outputPdice+"\n")
        while randompos != "First Base":
            randomBT,randomOBT,pAge,randompos,prename,surname,pTraits,pDiceAnch,pDiceMod,randomPdice,randomPtraits,randomBtraits,pHanded,randompHanded = createPlayer(pAge)
        pAge = randAge(random.randint(1,4))
        outputPtraits = checkBatter(randomPtraits)
        outputPdice = checkPitcher(randompos,randomPdice)
        outputpHanded = checkHand(randompos,randompHanded)
        outputBtraits = checkbTraits(randomBtraits)
        thisString.append(prename+" " +surname+","+randompos+","+str(pAge)+","+outputpHanded+","+str(randomBT)+","+str(randomOBT)+","+outputBtraits+","+outputPtraits+","+outputPdice+"\n")
        while randompos != "Second Base":
            randomBT,randomOBT,pAge,randompos,prename,surname,pTraits,pDiceAnch,pDiceMod,randomPdice,randomPtraits,randomBtraits,pHanded,randompHanded = createPlayer(pAge)
        pAge = randAge(random.randint(1,4))
        outputPtraits = checkBatter(randomPtraits)
        outputPdice = checkPitcher(randompos,randomPdice)
        outputpHanded = checkHand(randompos,randompHanded)
        outputBtraits = checkbTraits(randomBtraits)
        thisString.append(prename+" " +surname+","+randompos+","+str(pAge)+","+outputpHanded+","+str(randomBT)+","+str(randomOBT)+","+outputBtraits+","+outputPtraits+","+outputPdice+"\n")
        while randompos != "Third Base":
            randomBT,randomOBT,pAge,randompos,prename,surname,pTraits,pDiceAnch,pDiceMod,randomPdice,randomPtraits,randomBtraits,pHanded,randompHanded = createPlayer(pAge)
        pAge = randAge(random.randint(1,4))
        outputPtraits = checkBatter(randomPtraits)
        outputPdice = checkPitcher(randompos,randomPdice)
        outputpHanded = checkHand(randompos,randompHanded)
        outputBtraits = checkbTraits(randomBtraits)
        thisString.append(prename+" " +surname+","+randompos+","+str(pAge)+","+outputpHanded+","+str(randomBT)+","+str(randomOBT)+","+outputBtraits+","+outputPtraits+","+outputPdice+"\n")
        while randompos != "Shortstop":
            randomBT,randomOBT,pAge,randompos,prename,surname,pTraits,pDiceAnch,pDiceMod,randomPdice,randomPtraits,randomBtraits,pHanded,randompHanded = createPlayer(pAge)
        pAge = randAge(random.randint(1,4))
        outputPtraits = checkBatter(randomPtraits)
        outputPdice = checkPitcher(randompos,randomPdice)
        outputpHanded = checkHand(randompos,randompHanded)
        outputBtraits = checkbTraits(randomBtraits)
        thisString.append(prename+" " +surname+","+randompos+","+str(pAge)+","+outputpHanded+","+str(randomBT)+","+str(randomOBT)+","+outputBtraits+","+outputPtraits+","+outputPdice+"\n")
        thisString.append("Bench \n")
        while InfieldBench > 0:
            randomBT,randomOBT,pAge,randompos,prename,surname,pTraits,pDiceAnch,pDiceMod,randomPdice,randomPtraits,randomBtraits,pHanded,randompHanded = createPlayer(pAge)
            while randompos in("Left Field", "Right Field", "Center Field", "Catcher", "Starting Pitcher", "Relief Pitcher"):
                randomBT,randomOBT,pAge,randompos,prename,surname,pTraits,pDiceAnch,pDiceMod,randomPdice,randomPtraits,randomBtraits,pHanded,randompHanded = createPlayer(pAge)
            pAge = randAge(random.randint(1,4))
            outputPtraits = checkBatter(randomPtraits)
            outputPdice = checkPitcher(randompos,randomPdice)
            outputpHanded = checkHand(randompos,randompHanded)
            outputBtraits = checkbTraits(randomBtraits)
            if randompos in ("First Base", "Second Base", "Third Base", "Shortstop", "Utility"):
                randompos = "INF"
            thisString.append(prename+" " +surname+","+randompos+","+str(pAge)+","+outputpHanded+","+str(randomBT)+","+str(randomOBT)+","+outputBtraits+","+outputPtraits+","+outputPdice+"\n")
            InfieldBench = InfieldBench - 1
        while OutfieldBench > 0:
            randomBT,randomOBT,pAge,randompos,prename,surname,pTraits,pDiceAnch,pDiceMod,randomPdice,randomPtraits,randomBtraits,pHanded,randompHanded = createPlayer(pAge)
            while randompos in ("First Base", "Second Base", "Third Base", "Shortstop", "Starting Pitcher", "Relief Pitcher", "Catcher"):
                randomBT,randomOBT,pAge,randompos,prename,surname,pTraits,pDiceAnch,pDiceMod,randomPdice,randomPtraits,randomBtraits,pHanded,randompHanded = createPlayer(pAge)
            pAge = randAge(random.randint(1,4))
            outputPtraits = checkBatter(randomPtraits)
            outputPdice = checkPitcher(randompos,randomPdice)
            outputpHanded = checkHand(randompos,randompHanded)
            outputBtraits = checkbTraits(randomBtraits)
            if randompos in ("Left Field", "Right Field", "Center Field", "Utility"):
                randompos = "OF"
            thisString.append(prename+" " +surname+","+randompos+","+str(pAge)+","+outputpHanded+","+str(randomBT)+","+str(randomOBT)+","+outputBtraits+","+outputPtraits+","+outputPdice+"\n")
            OutfieldBench = OutfieldBench - 1
        while CatcherBench > 0:
            randomBT,randomOBT,pAge,randompos,prename,surname,pTraits,pDiceAnch,pDiceMod,randomPdice,randomPtraits,randomBtraits,pHanded,randompHanded = createPlayer(pAge)
            while randompos in ("First Base", "Second Base", "Third Base", "Shortstop", "Starting Pitcher", "Relief Pitcher", "Left Field", "Right Field", "Center Field", "Utility"):
                randomBT,randomOBT,pAge,randompos,prename,surname,pTraits,pDiceAnch,pDiceMod,randomPdice,randomPtraits,randomBtraits,pHanded,randompHanded = createPlayer(pAge)
            pAge = randAge(random.randint(1,4))
            outputPtraits = checkBatter(randomPtraits)
            outputPdice = checkPitcher(randompos,randomPdice)
            outputpHanded = checkHand(randompos,randompHanded)
            outputBtraits = checkbTraits(randomBtraits)
            if randompos in ("Catcher"):
                randompos = "C"
            thisString.append(prename+" " +surname+","+randompos+","+str(pAge)+","+outputpHanded+","+str(randomBT)+","+str(randomOBT)+","+outputBtraits+","+outputPtraits+","+outputPdice+"\n")
            CatcherBench = CatcherBench - 1
        thisString.append("Pitchers \n")
        while StartingPitchers > 0:
            randomBT,randomOBT,pAge,randompos,prename,surname,pTraits,pDiceAnch,pDiceMod,randomPdice,randomPtraits,randomBtraits,pHanded,randompHanded = createPlayer(pAge)
            while randompos in ("First Base", "Second Base", "Third Base", "Shortstop", "Catcher", "Relief Pitcher", "Left Field", "Right Field", "Center Field", "Utility"):
                randomBT,randomOBT,pAge,randompos,prename,surname,pTraits,pDiceAnch,pDiceMod,randomPdice,randomPtraits,randomBtraits,pHanded,randompHanded = createPlayer(pAge)
            pAge = randAge(random.randint(1,4))
            outputPtraits = checkBatter(randomPtraits)
            outputPdice = checkPitcher(randompos,randomPdice)
            outputpHanded = checkHand(randompos,randompHanded)
            outputBtraits = checkbTraits(randomBtraits)
            if randompos in ("Starting Pitcher"):
                randompos = "SP"
            thisString.append(prename+" " +surname+","+randompos+","+str(pAge)+","+outputpHanded+","+str(randomBT)+","+str(randomOBT)+","+outputBtraits+","+outputPtraits+","+outputPdice+"\n")
            StartingPitchers = StartingPitchers - 1
        while ReliefPitchers > 0:
            randomBT,randomOBT,pAge,randompos,prename,surname,pTraits,pDiceAnch,pDiceMod,randomPdice,randomPtraits,randomBtraits,pHanded,randompHanded = createPlayer(pAge)
            while randompos in ("First Base", "Second Base", "Third Base", "Shortstop", "Catcher", "Starting Pitcher", "Left Field", "Right Field", "Center Field", "Utility"):
                randomBT,randomOBT,pAge,randompos,prename,surname,pTraits,pDiceAnch,pDiceMod,randomPdice,randomPtraits,randomBtraits,pHanded,randompHanded = createPlayer(pAge)
            pAge = randAge(random.randint(1,4))
            outputPtraits = checkBatter(randomPtraits)
            outputPdice = checkPitcher(randompos,randomPdice)
            outputpHanded = checkHand(randompos,randompHanded)
            outputBtraits = checkbTraits(randomBtraits)
            if randompos in ("Relief Pitcher"):
                randompos = "RP"
            thisString.append(prename+" " +surname+","+randompos+","+str(pAge)+","+outputpHanded+","+str(randomBT)+","+str(randomOBT)+","+outputBtraits+","+outputPtraits+","+outputPdice+"\n")
            ReliefPitchers = ReliefPitchers - 1
    r_0pen = open(return_value, 'w',encoding='utf-8')
    r_0pen.write(csvHeader)
    for line in thisString:
        r_0pen.write(line)
    r_0pen.close()
    #del(r_0pen)
    #r_0pen = open(retur, 'w',encoding='utf-8')
    #thisString.clear()
    return

def updatePlayer(randomBtraits,randompHanded,randomPdice,randomPtraits,surname,prename,randompos,randomOBT,randomBT,pAge):
    #print(randomPtraits)
    window['-BTRAITS-'].update(randomBtraits)
    #print(randomPtraits)
    window['-PHANDED-'].update(randompHanded)
    window['-PDICE-'].update(randomPdice)
    window['-PTRAITS-'].update(randomPtraits)
    #print(randomPtraits)
    window['-2ndNAMES-'].update(surname)
    #print(randomPtraits)
    window['-1stNAMES-'].update(prename)
    #print(randomPtraits)
    window['-POSITION-'].update(randompos)
    #print(randomPtraits)
    window['-OBT-'].update(randomOBT)
    #print(randompos)
    window['-BT-'].update(randomBT)
    window['-AGE-'].update(pAge)

with open('firstNames.txt',encoding = 'utf-8') as f_fNames:
    firstNames = f_fNames.readlines()
f_fNames.close()
firstNames = [x[:-1] for x in firstNames]
with open('surnames.txt',encoding = 'utf-8') as f_sNames:
    secondNames = f_sNames.readlines()
f_sNames.close()
secondNames = [x[:-1] for x in secondNames]

# The following arrays are created to replicate the chances that are in the rules
positions = [
    "Utility", "Catcher", "First Base", "Second Base", "Third Base", "Shortstop",
    "Left Field", "Center Field", "Right Field", "Starting Pitcher",
    "Starting Pitcher", "Starting Pitcher", "Starting Pitcher", "Starting Pitcher",
    "Starting Pitcher", "Relief Pitcher", "Relief Pitcher", "Relief Pitcher",
    "Relief Pitcher", "Relief Pitcher"
]

pTraits = [
    "None", "None", "None", "CN-", "None", "None", "None", "None", "None",
    "None", "None", "None", "None", "K+", "GB+", "CN+", "ST+"
]

pDiceMod = [
    "d12", "d8", "d8", "d4", "d4", "d4", "d4", "-d4", "-d4", "-d4"
]

pDiceAnch = [
    "d20", "d12", "d12", "d8", "d8", "d6", "d6", "d4", "d4", "No Dice!",
    "-d4", "-d4", "-d8"
]

pHanded = [
    "Right Handed", "Right Handed", "Right Handed", "Right Handed",
    "Right Handed", "Right Handed", "Left Handed", "Left Handed",
    "Left Handed", "Switch Hitter (Pitchers: Left Handed)"
]

bTraits = [
    "P--", "P-", "S-", "C-", "D-", "None", "None", "None", "None", "None",
    "None", "None", "None", "P+", "D+", "C+", "S+", "T+", "P++"
]

sg.theme('DarkBlue8')   # Add a touch of color

# All the stuff inside your window.
textList = [
    [sg.Text("Player Name: ", size=(12,1)), sg.Text('', key='-1stNAMES-'),sg.Text('', key='-2ndNAMES-')],
    [sg.Text("Player Age: ", size=(12,1)), sg.Text('', key='-AGE-')],
    [sg.Text("Player Position: ", size=(12,1)), sg.Text('', key='-POSITION-')],
    [sg.Text("Left or Right: ", size=(12,1)), sg.Text("", key='-PHANDED-')],
    [sg.Text("Batter Target: ", size=(12,1)), sg.Text("", key='-BT-')],
    [sg.Text("On Base Target: ", size=(12,1)), sg.Text("", key='-OBT-')],
    [sg.Text("Pitching Trait: ", size=(12,1)), sg.Text("", key='-PTRAITS-')],
    [sg.Text("Pitching Die: ", size=(12,1)), sg.Text("", key='-PDICE-')],
    [sg.Text("Batting Trait: ", size=(12,1)), sg.Text("", key='-BTRAITS-')],
]

Options = [
    [sg.Push(background_color="lightgray"),
     sg.Text("Select the \"Age\" of the Players", background_color="lightgray", text_color="black")],
    [sg.Push(background_color="lightgray"),
     sg.Checkbox('Prospect ', default=True, key='-AGE1-', background_color="lightgray", text_color="black"),sg.Push(background_color="lightgray")],
    [sg.Push(background_color="lightgray"),
     sg.Checkbox('Rookie    ', default=False, key='-AGE2-',background_color="lightgray", text_color="black"),sg.Push(background_color="lightgray")],
    [sg.Push(background_color="lightgray"),
     sg.Checkbox('Veteran   ', default=False, key='-AGE3-', background_color="lightgray", text_color="black"),sg.Push(background_color="lightgray")],
    [sg.Push(background_color="lightgray"),
     sg.Checkbox('Old Timer', default=False, key='-AGE4-', background_color="lightgray", text_color="black"),sg.Push(background_color="lightgray")],
    [sg.Push(background_color="lightgray"),
     sg.Text("", justification='center', key="-OPTIONERROR-", background_color="lightgray", text_color="black")],
]

NoteBlock = [
    [sg.Text("\t Welcome to a simple player and team creation app." +
             "\n\n To use this generator, click on the \"Randomize\" button to create a random player. \n" +
             "When there is a likable player, click on the \"Save Player\" button to store the player \n" +
             "into the PlayerPool.csv file. \n\n" +
             "To generate a large number of players, fill out the \"Number to Generate\" field, then \n" +
             "click on the \"Bulk Generate\" button.  This adds the specified number of players to the \n" +
             "csv file. \n\n" +
             "To generate a random team, click on the \"Random Team\" button to have a random \n" +
             "created and saved into a specified csv file. \n" +
             "\t\t\t\t app created by Mountain Monkeys - tiqdreng",
             background_color="lightgray", text_color="black")],
]

CreateButtons = [
    [sg.VPush()],
    [sg.Push(),sg.Text("Bulk Player Creation")],
    [sg.Push(),sg.Text("How many Players to generate: ",size =(23, 1)), sg.InputText('',size=(16,1), key='pAmount')],
    [sg.Push(),sg.Button("Bulk Generate")],
]

# This is where the actual layout is setup for the window components
layout = [
    [sg.Button('Get Deadball by W.M. Akers', key = 'LINK1'),sg.Push(),
     sg.Image('./images/BasedOnAkersGames_sm.png', subsample=3),
     sg.Text("Select for \"Ancient\" Players"),
     sg.Checkbox('Ancient Era', default=False, key='-ERA-')],
    [sg.Push(),
     sg.Text("Select for \"Farm Hand\" Players"),
     sg.Checkbox('Farm Hand', default=False, key='-FARM-')],
    [sg.Column(textList, element_justification='l', expand_x=True),sg.Column(Options, element_justification='l', background_color="lightgray")],
    [sg.Column(NoteBlock, element_justification='l', expand_x=True),
     sg.Column(CreateButtons, element_justification='r', expand_x=True)],
    [sg.VPush()],
    [sg.Button("Close"),sg.Push(),
     sg.Button("Randomize", bind_return_key=True),
     sg.Button("Save Player"),
     sg.Button("Random Team")]
]
# This is where the window is called and created
window = sg.Window("Deadball Player Creator", layout, element_justification='l', size=(900, 600), resizable=True, return_keyboard_events=True)

# Until something is done, continue running the program
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == sg.WIN_CLOSED:
        break

    if event in ('LINK1', 'LINK2'):
        webbrowser.open("https://www.drivethrurpg.com/product/395133/Deadball-Baseball-With-Dice-Second-Edition")

    if event == "Save Player":
        f_0pen = open('PlayerPool.csv', 'a',encoding='utf-8')
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
        f_0pen.write(prename+" " +surname+","+randompos+","+str(pAge)+","+outputpHanded+","+str(randomBT)+","+str(randomOBT)+","+outputBtraits+","+outputPtraits+","+outputPdice+"\n")
        f_0pen.close()

    if event == "Random Team":
        CreateTeam()

    if event == "Bulk Generate":
        f_0pen = open('PlayerPool.csv', 'a',encoding='utf-8')
        justChecked = [element for element in values if values[element]==True
                       and 'AGE' in element]
        #print(len(justChecked)) # Only the checked box
        if len(justChecked) > 1:
            window['-OPTIONERROR-'].update("\n Only ONE age option is allowed.  Nothing Generated!")
        elif len(justChecked) < 1:
            window['-OPTIONERROR-'].update("\n AT LEAST ONE age option is needed.  Nothing Generated!")
        else:
            window['-OPTIONERROR-'].update("")
            thisLoop = values['pAmount']
            thisLoop = int(thisLoop)
            while thisLoop > 0:
                pAge = randAge(random.randint(1,4))
                randomBT,randomOBT,pAge,randompos,prename,surname,pTraits,pDiceAnch,pDiceMod,randomPdice,randomPtraits,randomBtraits,pHanded,randompHanded = createPlayer(pAge)
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
                f_0pen.write(prename+" " +surname+","+randompos+","+str(pAge)+","+outputpHanded+","+str(randomBT)+","+str(randomOBT)+","+outputBtraits+","+outputPtraits+","+outputPdice+"\n")
                thisLoop = thisLoop - 1
        f_0pen.close()

    if event == "Randomize" or values == "":
        justChecked = [element for element in values if values[element]==True
                       and 'AGE' in element]
        #print(len(justChecked)) # Only the checked box

        if len(justChecked) > 1:
            window['-OPTIONERROR-'].update("\n Only ONE age option is allowed.  Nothing Generated!")
            updatePlayer("","","","","","","","","","")
            continue
        elif len(justChecked) < 1:
            window['-OPTIONERROR-'].update("\n AT LEAST ONE age option is needed.  Nothing Generated!")
            updatePlayer("","","","","","","","","","")
            continue
        else:
            window['-OPTIONERROR-'].update("")
            rValue = random.randint(1,6)
            if values['-AGE4-']:
                pAge = 32 + rValue
            elif values['-AGE3-']:
                pAge = 27 + rValue
            elif values['-AGE2-']:
                pAge = 21 + rValue
            else:
                pAge = 18 + rValue
            randomBT,randomOBT,pAge,randompos,prename,surname,pTraits,pDiceAnch,pDiceMod,randomPdice,randomPtraits,randomBtraits,pHanded,randompHanded = createPlayer(pAge)
            updatePlayer(randomBtraits,randompHanded,randomPdice,randomPtraits,surname,prename,randompos,randomOBT,randomBT,pAge)
#Something is done... stop the program
    if event == "Close" or event == sg.WIN_CLOSED:
        break
window.close()
