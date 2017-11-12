from character import *




class Bojack(Character):

    def _init_(self, win:graphWin):
        super(Character, self)._init_()
        self.name = "Santa"
        self.woo = 1

    def question1(self):
        question = "Wanna share a glass of eggnog?"
        resA = "Only if it's alcoholic."
        resB = "I prefer cookies and milk." ##Correct
        resC = "Eggnog?? It's June."
        resD = "I'm not thirsty."

    def question2(self):
        question = "Ho, ho, ho, you're nice."
        resA = "Thanks! You're nice too!"
        resB = "Are you blushing? Your nose looks red!" ##correct
        resC = "How old are you?"
        resD = "I'm actually very naughty..."

    def question3(self):
         question = "I like to treat my mans. If I got you a gift, what would be on your list?"
         resA = "I don't have a list... but I mean I like gifts I guess."
         resB = "Jewelry"
         resC = "Gift cards"
         resD = "Oh I'll write everything down and send it to you in a letter!" ##Correct

    def question4(self):
        question = "Would you be a good girl and grab me a piece of pizza?"
        resA = "Bring him a slice of the Chicago style deep dish."
        resB = "Bring him a slice of the mac and cheese pizza." ##correct
        resC = "Bring him a slice of the buffalo chicken pizza."
        resD = "You could use the exercise with that bowl of jelly you've got."

    def question5(self):
        question = "I'm Santa."
        resA = "I knew the whoe time." ##correct
        resB = "WHAAAAAAT?"
        resC = "If you're Santa call me Mrs.Claws... meow!!"
        resD = "I'm calling the police."

