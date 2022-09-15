# The Vampire Hunt

from time import sleep

def type(x):
    words = str(x)
    for char in words:
        sleep(0.015)
        print(char, end='', flush=True)
    print("")
    sleep(0.3)
def pause():
    sleep(0.5)
    print("")
    
def die():
    print("Game over. Thanks for playing!")
    exit()
        
party = ["sambo", "griff", "raven"]
actions = ["help", "enter", "attack", "party", "inspect", "grab", "room"]
subjects = {}



type("You are a group of peasants. You have lived your life under the shadow of the Vampire's Castle.")
type("The " + str(len(party)) + " of you met in secret, and vowed to slay the Vampire this very night.")
pause()
type("Amongst your number are:")
type(party[0].title() + " the Tailor, armed with a pair of scissors.")
type(party[1].title() + " the town crier, armed with a heavy metal bell.")
type(party[2].title() + " the witch, armed with the spell Magic Missile.")
pause()
type("Who is your leader?")
ans = input("> ").lower()

while ans not in party:
    type(ans.title() + ' is not among you. Who is your leader?')
    ans = input("> ").lower()

leader = ans.title()
type(leader + " is your leader. She will be the last to perish.")
type("You can use 'party' to review your compatriots and their inventory. Each peasant can hold one weapon and one item.")
pause()

###############################################################################
#                           CORE GAMEPLAY LOOP
###############################################################################
count = 0            
def do():
    global count
    global subjects
    if count == 0:
        room("room1")
        type("What will you do? Use 'help' for a list of common actions.")
    while True:
        count += 1
        #type(count)
        sbj = None
        act = None
        ans = input("> ").lower()
        if ans == "suicide":
            die()
        elif ans == "room":
            room("subjects")
        elif ans == "help":
            type("These actions are often used: " + (', '.join(actions)) + ".")
            type("Interactable objects are CAPITALISED.")
        elif ans == "party":
            type("You have a stalwart crew!")
        else:
            for key in subjects:
                if key in ans:
                    sbj = key
                    for key in subjects.get(sbj):
                        if key in ans:
                            act = key
            if act is not None and sbj is not None:
                #type("You " + act + " the " + sbj + ".")
                type(subjects.get(sbj).get(act)[0])
                if len(subjects.get(sbj).get(act)) == 3:
                    if subjects.get(sbj).get(act)[1] == "do":
                            subjects.get(sbj).get(act)[2]()
                    elif subjects.get(sbj).get(act)[1] == "go":
                            room(subjects.get(sbj).get(act)[2])
            else:
                for x in actions:
                    if x in ans:
                        act = x
                if act is None and sbj is not None:
                    type("Do what to " + sbj + "?")    
                elif act is not None and sbj is None:
                    type(act.title() + " what?")
                elif act is not None and sbj is not None:
                    type("The " + sbj + " cannot be " + act + "ed.")
                else:
                    type("You all" + ans + ", but nothing happens.")
                    
def room(x):
    global subjects
    subjects = eval(x)                                  #set accessible subjects to subjects in room
    type(subjects.get("d$")[0])                         #describe room
    for subject in subjects:
        if subject != "d$":
            type(subjects.get(subject).get("d$")[0])    #describe accessible subjects

###############################################################################
#                                  ROOMS
###############################################################################
def r1head():
    global room1
    room1.pop("head")
    room1.update({"key":
                    {"d$": ["A KEY is on the floor in a puddle of brain matter."],
                     "inspect": ["The KEY is made of black metal."],
                     "grab": ["The KEY is picked up by " + leader + "."]}})

room1 = {"d$":["The " + str(len(party)) + " of you stand at the entrance to the Vampire's Castle. Inside are monsters, traps... and the dreaded Vampire herself."],
        "door":{
            "d$": ["To the north, there is a colossal dark oak DOOR - the entrance to the castle."],
            "enter":   ["You go inside.", "go", "room2"],
            "inspect": ["The DOOR is large and imposing."]},
        "doormat":{
            "d$": ["At the DOOR's foot there is a DOORMAT."],
            "inspect": ["The DOORMAT is stained with blood."]},
        "head":{
            "d$": ["A HEAD on a spike stands to the left of the DOOR."],
            "inspect": ["Diagonis: decapitation. The tounge is lolling out in a gruesome manner."],
            "attack": [leader + " strikes with her weapon. The HEAD is obliterated. A KEY falls on the floor.", "do", r1head]}
        }    
       
room2 = {"d$":["The " + str(len(party)) + " of you stand in the Vampire's hallway."],
         "door":
                    {   "d$": ["To the south, there is a colossal dark oak DOOR - the exit from the castle."],
                        "enter":   ["You go outside.", "go", "room1"], 
                        "inspect": ["The DOOR is large and imposing."]}}
    

do()