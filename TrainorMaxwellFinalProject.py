import random
from breezypythongui import EasyFrame
from tkinter import PhotoImage

class TtrpgRoller (EasyFrame):
    """Creates a window object in which the dice roller program operates"""
    def __init__(self):
        # sets up EasyFrame
        EasyFrame.__init__(self, title = "TTRPG Dice Roller")

        # disables resizing of the window
        self.setResizable(False)

        # creates a panel for the header image
        header = self.addPanel(row = 0, column = 0,background = "#2F446D")

        # creates a panel for the top row of dice
        topRow = self.addPanel(row = 1, column = 0, rowspan = 2, background = "#2F446D")

        # creates a panel for the bottom row of dice
        bottomRow = self.addPanel(row = 3, column = 0, rowspan = 2, background = "#2F446D")

        # creates a panel for the modifier options and roll/clear buttons and results
        modifierRollRow = self.addPanel(row = 5, column = 0, rowspan = 2, background = "#2F446D")
        
        # creates a label for the header image
        self.diceImageLabel = header.addLabel(text = "", row = 0, column = 0)

        # creates a label for the dragon image
        self.dragonImageLabel = topRow.addLabel(text = "", row = 0, column = 0, sticky = "NSEW")

        # the following lines of code create labels for the top row of dice as well as text fields for entering
        # number of dice to roll
        self.openingLabel = topRow.addLabel(text = "# of dice to roll", row = 1, column = 0, sticky = "NSEW")
        self.d20Label = topRow.addLabel(text = "d20", row = 0, column = 2, sticky = "NSEW")
        self.d20Rolled = topRow.addTextField(text= "", row = 1, column = 2, width = 5, sticky = "NSEW")
        self.d12Label = topRow.addLabel(text = "d12", row = 0, column = 4, sticky = "NSEW")
        self.d12Rolled = topRow.addTextField(text= "", row = 1, column = 4, width = 5, sticky = "NSEW")
        self.d10Label = topRow.addLabel(text = "d10", row = 0, column = 6, sticky = "NSEW")
        self.d10Rolled = topRow.addTextField(text= "", row = 1, column = 6, width = 5, sticky = "NSEW")

        # does the same as above section but for bottom row
        self.d100Label = bottomRow.addLabel(text = "d100", row = 2, column = 0, sticky = "NSEW")
        self.d100Rolled = bottomRow.addTextField(text= "", row = 3, column = 0, width = 5, sticky = "NSEW")
        self.d8Label = bottomRow.addLabel(text = "d8", row = 2, column = 2, sticky = "NSEW")
        self.d8Rolled = bottomRow.addTextField(text= "", row = 3, column = 2, width = 5, sticky = "NSEW")
        self.d6Label = bottomRow.addLabel(text = "d6", row = 2, column = 4, sticky = "NSEW")
        self.d6Rolled = bottomRow.addTextField(text= "", row = 3, column = 4, width = 5, sticky = "NSEW")
        self.d4Label = bottomRow.addLabel(text = "d4", row = 2, column = 6, sticky = "NSEW")
        self.d4Rolled = bottomRow.addTextField(text= "", row = 3, column = 6, width = 5, sticky = "NSEW")

        # creates labels for the modifier selection, and a radio button group, as well as the buttons for
        # rolling, clearing, and the result field
        modifierRollRow.addLabel(text = "Add modifier?", row = 4, column = 0, sticky = "NSEW")
        self.modifierToggle = modifierRollRow.addRadiobuttonGroup(row = 4, column = 1)
        self.defaultRB = self.modifierToggle.addRadiobutton(text = "No", command = self.modifierOff)
        self.modifierToggle.setSelectedButton(self.defaultRB)
        self.modifierToggle.addRadiobutton(text = "Yes", command = self.modifierOn)
        self.modifierAmount = modifierRollRow.addIntegerField(value = 0, row = 4, column = 2, state = "readonly", sticky = "NSEW")
        self.rollButton = modifierRollRow.addButton(text = "Roll", row = 5, column = 0, command = self.roll)
        self.clearButton = modifierRollRow.addButton(text = "Clear", row = 5, column = 1, command = self.clear)
        self.results = modifierRollRow.addIntegerField(value = 0, row = 5, column = 2, state = "readonly", sticky = "NSEW")

        # imports photos and sets them to labels
        self.diceImage = PhotoImage(file = "diceImage.gif")
        self.dragonImage = PhotoImage(file = "dragon.gif")
        self.diceImageLabel["image"] = self.diceImage
        self.dragonImageLabel["image"] = self.dragonImage
        

    def roll(self):
        """Command for the roll button"""

        # initializes a dictionary with each type of dice acting as a key to the number of
        # dice selected to roll
        diceAndRolls = {20 : self.d20Rolled.getText(), 12 : self.d12Rolled.getText(), 10 : self.d10Rolled.getText(),
        100 : self.d100Rolled.getText(), 8 : self.d8Rolled.getText(), 6 : self.d6Rolled.getText(), 4 : self.d4Rolled.getText()}
        
        # initializes some important variables for the scope of the roll command
        emptyCount = 0
        rollTotal = 0
        finalTotal = 0

        # for loop that iterates through each dictionary entry
        for key in diceAndRolls:

            # assigns the modifier (if there is one) to a variable
            modifier = self.modifierAmount.getNumber()

            # checks if a dice needs to be rolled, adds to empty count if not
            if diceAndRolls.get(key) == "":
                emptyCount += 1

                # checks if every box is empty, opens an error window if so
                if emptyCount == 7:
                    self.messageBox(title = "ERROR", message = "Please enter at least one die to be rolled")
                    modifier = 0
            
            # code that carries out if not every box is empty
            else:
                # opens try-except to test if text was entered instead of numbers
                try:

                    # assigns the number of dice to be rolled and converts to an integer 
                    number = int(diceAndRolls.get(key))

                    # tests if a negative number is entered, displays an error window if so, then 
                    # resets modifier amount and rollTotal so nothing is displayed in the application
                    if number <= 0:
                        self.messageBox(title = "ERROR", message = "Please enter only positive numbers")
                        modifier = 0
                        rollTotal = 0
                        break

                    # assigns the number of sides on a die
                    sides = key   

                    # starts a running total of all dice rolls  
                    rollTotal += rollDice(number, sides)

                    # used for testing to monitor the roll total as the program proceeds, commented out
                    # for users
                    print("R: ", rollTotal)
                
                # if text is entered instead of an integer, displays an error window, and resets variables
                except ValueError:
                    self.messageBox(title = "ERROR: ", message = "Please enter numbers only")
                    modifier = 0
                    rollTotal = 0
                    break
        
        # calculates the final total by adding the modifier to the rolled total
        finalTotal = rollTotal + modifier

        # sets the result to the integer field in the application
        self.results.setNumber(finalTotal)
        
    def clear(self):
        """Command for the clear button, which resets all fields and buttons
        to their default values"""

        self.d20Rolled.setText("")
        self.d12Rolled.setText("")
        self.d10Rolled.setText("")
        self.d100Rolled.setText("")
        self.d8Rolled.setText("")
        self.d6Rolled.setText("")
        self.d4Rolled.setText("")
        self.modifierAmount["state"] = "readonly"
        self.modifierAmount.setNumber(0)
        self.modifierToggle.setSelectedButton(self.defaultRB)
        self.results.setNumber(0)
            
    def modifierOn(self):
        """Command for the modifier radio button, activating the modifier integer field"""

        self.modifierAmount["state"] = "normal"

    def modifierOff(self):
        """Command for the modifier radio button, deactivating the modifier integer field"""

        self.modifierAmount.setNumber(0)
        self.modifierAmount["state"] = "readonly"

def rollDice(number, sides):
    """Function defined for rolling many or one dice/die"""

    # initializes a variable for the running total
    total = 0

    # initializes a for loop to iterate through the number of 
    # dice to be rolled
    for count in range(number):

        # randomly generates a rolled dice
        newRoll = random.randint(1, sides)

        # implemented for testing, commented out for users
        print("NR: ", newRoll)

        # updates the total
        total += newRoll
    
    # returns said total
    return total

def main():
    """The main loop of the program"""
    TtrpgRoller().mainloop()

if __name__ == "__main__":
    main()