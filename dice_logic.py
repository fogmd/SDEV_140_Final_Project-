import random
YES = "Y"
diceSelection = input("Which die would you like to roll: ")
diceNumber = input("How many dice would you like to roll: ")
modifierYN = input("Would you like to apply a modifier to the roll? Answer Y or N: ")
if modifierYN == YES.lower():
    modifierNum = input("Please enter the modifier amount: ")
    if int(diceNumber) > 1:
        modifierOnEach = input("Would you like to apply the modifier to each roll, or the total of all rolls? Answer Y for each or N for total: ")
    else:
        modifierOnEach = ""
cumulativeRoll = 0

# set the type of dice rolled and the range of the random number generator 
for diceRolled in range(int(diceNumber)):
    newestRoll = random.randint(1, int(diceSelection.lower().replace("d", "")))

# logic for if a modifier is applied to the roll
    if modifierYN == YES.lower():
        if modifierOnEach == YES.lower():
            newestRollwModifier = newestRoll + int(modifierNum)
            cumulativeRoll += newestRollwModifier
            print("Roll " + str(diceRolled + 1) + ": " + "(straight roll) " + str(newestRoll) + " (w/ modifier) " \
                       + str(newestRollwModifier))
            if diceRolled == int(diceNumber) - 1:
                print("You rolled " + diceNumber + diceSelection.lower() + "s plus a modifier of " + str(modifierNum) + \
                  " for a total of " + str(cumulativeRoll))
        else:
            cumulativeRoll += newestRoll
            print("Roll " + str(diceRolled + 1) + ": " + str(newestRoll))
            if diceRolled == int(diceNumber) - 1:
                    cumulativeRoll += int(modifierNum)
            if diceRolled == int(diceNumber) - 1:
                if diceRolled > 0:
                    print("You rolled " + diceNumber + diceSelection.lower() + "s plus a modifier of " + str(modifierNum) + \
                  " for a total of " + str(cumulativeRoll))
                else:
                 print("You rolled " + str(newestRoll) + " plus a modifier of " + str(modifierNum) + " for a total of " + str(cumulativeRoll))

# logic for a straight roll
    else:
        print("Roll " + str(diceRolled + 1) + ": " + str(newestRoll))
        cumulativeRoll += newestRoll
        if diceRolled == int(diceNumber) - 1:
            if diceRolled > 0:
                print("You rolled " + diceNumber + diceSelection.lower() + "s for a total of " + str(cumulativeRoll))
            else:
                print("You rolled " + str(cumulativeRoll))