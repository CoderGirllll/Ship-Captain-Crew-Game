import random
from playsound import playsound

#Defined Functions
def display_score(sc, score_label):
    score_label.config(text=sc)
    score_label.pack()


def calc_score(list, score_label):
    #Calculate score
    score = "YOU GOT A "
    #Check for ship, captain, crew
    if ('\u2685' in list):
        score += "SHIP ,"
        list.remove('\u2685')
        if ('\u2684' in list):
            score += "CAPTAIN ,"
            list.remove('\u2684')
            if ('\u2683' in list):
                score += "CREW ,"
                list.remove('\u2683')
    score += "CARGO OF "
    #Check for cargo
    cargo = calc_cargo(list)
    score += str(cargo)
    #Displaying the score
    display_score(score, score_label)


def dice_display(dice_label, score_label):
    list = []
    for r in range(0, 5, 1):
        list.append(roll_dice())
    dice_label.config(text=list)
    dice_label.pack()
    #Playing the audio for dice roll
    play()
    #Check for score
    calc_score(list, score_label)


def play():
    #Play Dice Roll Audio    
    playsound('Styles\dice_roll.mp3', block=True)


def roll_dice():
    #Dice Roll Stimulation
    dice_num = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    return random.choice(dice_num)


def calc_cargo(list):
    #Cargo Calculation
    cargo = 0
    for i in list:
        match i:
            case '\u2680':
                cargo += 1
            case '\u2681':
                cargo += 2
            case '\u2682':
                cargo += 3
            case '\u2683':
                cargo += 4
            case '\u2684':
                cargo += 5
            case '\u2685':
                cargo += 6
    return cargo