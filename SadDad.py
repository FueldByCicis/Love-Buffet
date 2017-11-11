from character import *




class SadDad(Character):

    def _init_(self, win:graphWin):
        super(Character, self)._init_()
        self.name = "Sad Dad"
        self.woo = 1

    def question1(self):
        question = "Hey, do you have any aspirin?"
        resA = "Kids screaming a little too loud?"
        resB = "Yeah I have a whole bottle in my bag.It's almost empty though."
        resC = "No"
        resD = "I don't believe in pharmaceuticals. Illness is a mental state. Think differently."

    def question2(self):
         question = "Do they have coffee here?"
         resA = "They'd better. I'll die without a cup."
         resB = "No, I don't think so."
         resC = "You mean like... black? Just black coffee??"
         resD = "Ew I hate coffee."

    def question3(self):
        question = "I had to sell my car to get a bigger one when I had kids. My first born i named after the jeep I sold to have him."
        resA = "I have a jeep."
        resB = "Oh...kay?"
        resC = "I'm not that into cars."
        resD = "You had a jeep? That's so boujee."

    def question4(self):
        question = "I could use a piece of pizza right now."
        resA = "Bring him a slice of the Chicago style deep dish."
        resB = "Bring him a slice of the mac and cheese pizza."
        resC = "Bring him a slice of the buffalo chicken pizza."
        resD = "The buffet is empty. They said they'll refill it in 10 minutes."

    def question5(self):
        question = "Damn.. I just got a text that I'm behind on my Khol's card payments."
        resA = "I just had to cancel my JCPenney card."
        resB = "That's really unfortunate."
        resC = "I get all of my sweaters from Khols!"
        resD = "I only shop at Vineyard Vines."