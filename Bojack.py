from character import *




class Bojack(Character):

    def _init_(self, win:graphWin):
        super(Character, self)._init_()
        self.name = "Bojack"
        self.woo = 1

    def question1(self):
        question = "Hey can I buy you a drink?"
        resA = "Please do."
        resB = "I don't drink."
        resC = "Who are you?"
        resD = "Are you a horse or is your hair just really curly?"

    def question2(self):
        question = "Could you not sit so close? I hate physical contact."
        resA = "But you just... told me to sit closer to you?"
        resB = "Oh sure. Whatever you say without contradiction."
        resC = "I'm just trying to snuggle up to you! It's cold in here."
        resD = "If you're afraid of physical contact why did you just try to pick me up with a drink?"

    def question3(self):
         question = "Hey grab me a piece of pizza."
         resA = "Bring him a slice of the Chicago style deep dish."
         resB = "Bring him a slice of the mac and cheese pizza."
         resC = "Bring him a slice of the buffalo chicken pizza."
         resD = "Excuse me?"

    def question4(self):
        question = "I'm sad."
        resA = "What do you want me to do about it?"
        resB = "Is there anything I can do to make you feel better??"
        resC = "I thought we were having a good time."
        resD = "I know how that feels, I have problems too."

    def question5(self):
        question = "Does my butt look good in these jeans?"
        resA = "You have the biggest butt I've ever seen!"
        resB = "I mean.. It looks average? Like how it's supposed to look?"
        resC = "I don't think your butt really stands out."
        resD = "It looks kind of flat."

