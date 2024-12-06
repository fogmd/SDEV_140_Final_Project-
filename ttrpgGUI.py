import random
from breezypythongui import EasyFrame

class TtrpgRoller (EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "TTRPG Dice Roller")
        diceRow = self.addPanel(row = 0, column = 0,  background = "gray")
        # diceRow = self.addPanel(row = 2, column = 0, rowspan = 2, background = "blue")
        modifierRow = self.addPanel(row = 4, column = 0)
        rollClearRow = self.addPanel(row = 5, column = 0)

        self.openingLabel = diceRow.addLabel(text = "# of dice to roll", row = 1, column = 0, sticky = "NSEW")

        self.d20Label = diceRow.addLabel(text = "d20", row = 0, column = 2, sticky = "NSEW")
        self.d20Rolled = diceRow.addIntegerField(value = 0, row = 1, column = 2, width = 5, sticky = "NSEW")

        self.d12Label = diceRow.addLabel(text = "d12", row = 0, column = 4, sticky = "NSEW")
        self.d12Rolled = diceRow.addIntegerField(value = 0, row = 1, column = 4, width = 5, sticky = "NSEW")

        self.d10Label = diceRow.addLabel(text = "d10", row = 0, column = 6, sticky = "NSEW")
        self.d10Rolled = diceRow.addIntegerField(value = 0, row = 1, column = 6, width = 5, sticky = "NSEW")

        self.d100Label = diceRow.addLabel(text = "d100", row = 2, column = 0, sticky = "NSEW")
        self.d100Rolled = diceRow.addIntegerField(value = 0, row = 3, column = 0, width = 5, sticky = "NSEW")

        self.d8Label = diceRow.addLabel(text = "d8", row = 2, column = 2, sticky = "NSEW")
        self.d8Rolled = diceRow.addIntegerField(value = 0, row = 3, column = 2, width = 5, sticky = "NSEW")
        
        self.d6Label = diceRow.addLabel(text = "d6", row = 2, column = 4, sticky = "NSEW")
        self.d6Rolled = diceRow.addIntegerField(value = 0, row = 3, column = 4, width = 5, sticky = "NSEW")

        self.d4Label = diceRow.addLabel(text = "d4", row = 2, column = 6, sticky = "NSEW")
        self.d4Rolled = diceRow.addIntegerField(value = 0, row = 3, column = 6, width = 5, sticky = "NSEW")

        modifierRow.addLabel(text = "Add modifier?", row = 4, column = 0, sticky = "NSEW")
        self.modifierToggle = modifierRow.addRadiobuttonGroup(row = 4, column = 1)
        self.defaultRB = self.modifierToggle.addRadiobutton(text = "No", command = self.modifierOff)
        self.modifierToggle.setSelectedButton(self.defaultRB)
        self.modifierToggle.addRadiobutton(text = "Yes", command = self.modifierOn)
        self.modifierAmount = modifierRow.addIntegerField(value = 0, row = 4, column = 2, state = "readonly")

    
        self.rollButton = rollClearRow.addButton(text = "Roll", row = 5, column = 0, command = self.roll)
        self.clearButton = rollClearRow.addButton(text = "Clear", row = 5, column = 1, command = self.clear)
        self.results = rollClearRow.addIntegerField(value = 0, row = 5, column = 2, width = 10, state = "readonly")
    
    def roll(self):
        number = self.d20Rolled.getNumber()
        diceWithD = self.d20Label["text"]
        diceSides = int(diceWithD[1:])
        modifier = self.modifierAmount.getNumber()
        result = 0
        for count in range(number):
            result += random.randint(1, diceSides)
        if modifier != 0:
            result += modifier
        self.results.setNumber(result)
        
    def clear(self):
        self.d20Rolled.setNumber(0)
        self.d12Rolled.setNumber(0)
        self.d10Rolled.setNumber(0)
        self.d100Rolled.setNumber(0)
        self.d8Rolled.setNumber(0)
        self.d6Rolled.setNumber(0)
        self.d4Rolled.setNumber(0)
        self.modifierAmount["state"] = "readonly"
        self.modifierAmount.setNumber(0)
        self.modifierToggle.setSelectedButton(self.defaultRB)
        self.results.setNumber(0)
            
    def modifierOn(self):
        self.modifierAmount["state"] = "normal"

    def modifierOff(self):
        self.modifierAmount.setNumber(0)
        self.modifierAmount["state"] = "readonly"


def main():
    TtrpgRoller().mainloop()

if __name__ == "__main__":
    main()