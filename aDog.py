from character import *


##Level 1 character

class ChrisDelia(Character):
    def __init__(self, win: graphWin):
        super(Character, self).__init__()
        self.name = "Chris D'elia"
        self.woo = 1

    def question1(self):
        question = "Bark! Bark!"
        resA = "Bork!"
        resB = "*Pet the doggo*"
        resC = "Woof woof?"
        resD = "*rub his belly*" ##all are correct
