from character import *


##Level 1 character

class ChrisDelia(Character):

    def __init__(self, win:graphWin):
        super(Character, self).__init__()
        self.name = "Chris D'elia"
        self.woo = 1

    def question1(self):
        question = "Hey, you look like you could use a coffee."
        resA = "F*** yeah, I'll that sh** right now Player." ##correct
        resB = "I'm good, thanks."
        resC = "I already had a cup."
        resD = "Sure!"

    def question2(self):
        question = "So...where do you work?"
        resA = "I'm a manager for a major corporation. I've been working up the ladder since I was drinking CapriSuns." ##correct
        resB = "I'm currently unemployed."
        resC = "I haven't worked a day in my life."
        resD = "I'm a waitress at a high end restaurant in the city."

    def question3(self):
        question = "Hey yo, grab this gangster a piece of pizza. I need to keep it real like those streets out there."
        resA = "Bring her a slice of Chicago style deep dish."
        resB = "Bring her a slice of the mac and cheese pizza."  ##correct
        resC = "Bring her a slice of the buffalo chicken pizza."
        resD = "What does that have to do with pizza?"

    def question4(self):
        question = "Do you think I'm attractive?"
        resA = "I think you look like a bald eagle."
        resB = "You look like a cool, young Bob Saget."
        resC = "Ya know, you kinda look like that guy from Sleepy Hollow."
        resD = "Yes." ##correct

    def question5(self):
        question = "Do you want to come to my birthday party?"
        resA = "Yeah! I'll get you pants that fit!"
        resB = "No: The Musical" ##correct
        resC = "I'll have to check my schedule."
        resD = "Will there be adult chaperone's?"
