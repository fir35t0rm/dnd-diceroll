#A D&D Attack Roll app - Harry Cox 2023

#Version History

#v0.1
#Initial build
#Basic hit attack roll with weapon damage

#v0.2
#Added Adv/Dis roll
#Adjusted ACroll = random.randrange to allow NAT 20s

#v0.3
#Added Modifier to adjust critical successes for Champions or has special items

#v0.4
#implemented numchk() function
#implemented yesprmpt() function
#front end print tidy up

#v0.5
#Adjusted BaseDmg to ensure max damage is possible

#v0.6
#Rewrote numchk() function to allow negative values and invalid entrys

#v0.7
#Rewrote Damage code for additional dice rolls other than multiplication of single die roll
#Implemented Additional Die Types (3d6, 2d8, etc)
#Implemented top value limit to numchk()
#Adjusted numchk() to allow flexible bottom value

#v0.8
#Functionalised possibly repeated code for future use
#Functionalised main code in __main__ function

#Import python-code
import random

#Functions

def numchk(text, botval, topval):
    while True:
        try:
            num = int(input(text))
        except:
            print("INVALID ENTRY, try again")
            continue
        if num < botval or num > topval:
            print("Entered value out of range, try again")
            continue
        else:
            break
    return num

def dietype(text, text2):
    while True:
        try:
            num = int(input("Enter Die for '" + text + "' (d4, d6, d8, d10, d20, d100) - enter number: " + str(text2) + "d"))
        except:
            print("INVALID ENTRY, try again")
            continue
        if int(num) not in [4, 6, 8, 10, 12, 20, 100]:
            print("Invalid Dice, try again")
            continue
        else:
            break
    return num

def yesprmpt(text):
    xyn = input(text)
    while xyn.lower() not in ('yes', 'y', 'no', 'n'):
        print("INVALID ENTRY")
        xyn = input(text)
    return xyn

def dieroll():
    roll = random.randrange(1, 21)
    return roll

def advroll(adv):
    dice = 1
    AdvRoll = []
    while dice <= 2:
        diceroll = random.randrange(1, 21)
        AdvRoll.append(diceroll)
        print('\nDice', dice, ':', diceroll)
        dice += 1
    AdvRoll.sort(reverse=adv)
    return AdvRoll[0]

#Start of App
def main():
    loop = "yes"
    TarAC = numchk("Enter Target Character AC: ", 8, 50)
    WeaQtyDie = numchk("Enter how many Hit Die for the weapon: ", 1, 50)
    WeaDmgDie = dietype("Equiped Weapon", WeaQtyDie)
    AckBonus = numchk("Enter Weapon Bonuses: ", -5, 50)
    CricPmpt = yesprmpt('Is your character a champion or has item to reduce your critial hit to 19?: ')

    if CricPmpt in ('y', 'yes'):
        CricMod = 1
    else:
        CricMod = 0

    while loop in ("yes", "y"):
        AdvMod = ''
        while not AdvMod or AdvMod > '3' or AdvMod <= "0" or not bool(AdvMod) and not AdvMod.isdigit:
            AdvMod = input ('''
    Is this attack the following?
    1 - Normal
    2 - Advantage
    3 - Disadvantage
    : ''')

            if AdvMod == '2':
                ACroll = advroll(True)
            elif AdvMod == '3':
                ACroll = advroll(False)
            else:
                ACroll = dieroll()
        ACTot = ACroll + int(AckBonus)
        print ("\nAttack Roll =",ACroll, "+", AckBonus,"=", ACTot)
        
        
        if ACroll >= 20-CricMod:
            dmg = 2
            print("Critical Success!! Roll double for damage!")
        elif ACroll == 1:
            dmg = 0
            print("Critical MISS!!")
        elif ACTot >= int(TarAC):
            dmg = 1
            print("Target Hits, roll for damage!")    
        else:
            dmg = 0
            print("Target misses!")

        if dmg > 0:
            DmgDice = 1
            DmgRolls = []
            while DmgDice <= dmg*WeaQtyDie:
                BaseDmg = random.randrange(1, WeaDmgDie+1)
                print ('Roll', DmgDice, '=', BaseDmg)
                DmgRolls.append(BaseDmg)
                DmgDice += 1
            print('Damage Roll:', sum(DmgRolls), "+", AckBonus, "=", sum(DmgRolls)+AckBonus)
            print("\nYou have damaged your target for", sum(DmgRolls)+AckBonus, "hit points!")

        loop = yesprmpt("Attack Again? (y/n): " )

if __name__ == '__main__':
    main()