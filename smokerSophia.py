from character import *

##Level 1 character

class SmokerSophia(Character):

    def __init__(self,window:graphWin):
        super(Character,self).__init__()
        self.name = "Sophia"
        self.woo = 1

    def question1(self):
        question = "Hey big papa. You looking for a fun time? Wanna smoke?"
        resA = "Sure, I'll take one."
        resB = "No, thank you."
        resC = "I got my own...thanks though." ##correct answer
        resD = "Smoking kills. #theRealCost"

    def question2(self):
        question = "You like kids? I got two of 'em. I didn't start smokin' 'til I was pregnant with the second one."
        resA = "Yeah I love kids! I've always wanted a bunch of lil' rugrats running around."
        resB = "I've never been good with kids...ever since I lost the last one."
        resC = "You really shouldn't be smoking while you're pregnant..."
        resD = "Will they grab me a beer?" ##correct

    def question3(self):
        question = "Hey, why don't you sneak me a slice of that pizza? I didn't pay for the buffet."
        resA = "Bring her a slice of Chicago style deep dish."
        resB = "Bring her a slice of the mac and cheese pizza." ##correct
        resC = "Bring her a slice of the buffalo chicken pizza."
        resD = "That would be stealing."

    def question4(self):
        question = "You like dogs? I got one of those, too; he's a great dane. His name's Grover Cleveland."
        resA = "Doggos!"
        resB = "Doggies!" ##correct
        resC = "I'm more of a cat person."
        resD = "Haven't been since my mom took the last one to the farm, poor Gerald Ford."

    def question5(self):
        question = "You work? I've dated one too many deadbeats in my life."
        resA = "I'm a firefighter..and also I hate wearing shirts." ##correct
        resB = "I work full-time as a couch potato."
        resC = "I received a small loan of a million dollars from my father."
        resD = "I got a job in my dad's company."