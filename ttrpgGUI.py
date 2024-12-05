import random
from breezypythongui import EasyFrame

class TtrpgRoller (EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "TTRPG Dice Roller")
        self.d20Label = self.addLabel(text = "d20", row = 0, column = 0)
        self.d20Rolled = self.addTextField(text = "", row = 0, column = 1, width = 5)
        self.d12Label = self.addLabel(text = "d12", row = 0, column = 2)
        self.d10Label = self.addLabel(text = "d10", row = 0, column = 4)
        self.d100Label = self.addLabel(text = "d100", row = 1, column = 0)
        self.d8Label = self.addLabel(text = "d8", row = 1, column = 2)
        self.d6Label = self.addLabel(text = "d6", row = 1, column = 4)
        self.d4Label = self.addLabel(text = "d4", row = 2, column = 0)
        self.d3Label = self.addLabel(text = "d3", row = 2, column = 2)
        self.d2Label = self.addLabel(text = "d2", row = 2, column = 4)


def main():
    TtrpgRoller().mainloop()

if __name__ == "__main__":
    main()