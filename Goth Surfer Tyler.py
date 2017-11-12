from character import *


class GothSurfer(Character):
    def _init_(self, win:graphWin):
        super(Character,self).init()
        self.name = GothSurfer
        self.woo = 1

    def question1(self):
        question = 'Like, can i join you brah?'
        resA = 'That would be, like, totally tubular.' #correct
        resB = 'Did you just call me brah?'
        resC = 'You smell like a fish.'
        resD = "Only if you're able of holding intelligent conversation."

    def question2(self):
        question = 'Like, what kind of music do you listen to brah?'
        resA = "I enjoy the sweet symphonies of orchestra music."
        resB = 'I like that gansta rap yo'
        resC = "HEAVY METALLLLLLL!!!" #Correct
        resD = "I don't like music"

    def question3(self):
        question = 'Like, what kind of pizza is way good brah?'
        resA = 'Bring him a slice of the Chicago style deep dish'
        resB = 'Bring him a slice of the Mac and Cheese pizza' #correct
        resC = 'Bring him a slice of the buffalo chicken pizza'
        resD = "Actually, I'm vegan."

    def question4(self):
        question = "Like, isn't the ocean the best thing brah?"
        resA = 'I get seasick easily'
        resB = "I've been afraid of the ocean ever since I watched Jaws"
        resC = 'I love the ocean, especially at high tide.' #correct
        resD = 'You mean like Lake Michigan?'

    def question5(self):
        question = 'Like, what do you do in your free time brah?'
        resA = 'I read history novels.'
        resB = 'I volunteer at the homeless shelter.'
        resC = 'I spend my time at the beach' #correct
        resD = "What's free time? #nodaysoff #studentathlete #alwaysstaygrinding"