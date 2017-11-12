from character import *


class Glitch(Character):
    def _init_(self, win:graphWin):
        super(Character,self).init()
        self.name = Glitch
        self.woo = 1

    def question1(self):
        question = '1100100101010101010?'
        resA = 'Are you okay?'
        resB = 'Can I help you?'
        resC = "You've got something on your....everywhere."
        resD = '61726520796f75206173206561737920617320796f75206c6f6f6b' #correct

    def question2(self):
        question = '101000100010111101010101?'
        resA = 'What are you saying?'
        resB = 'Is that some new slang term?'
        resC = 'Those are some sick bars.'
        resD = '54686f73652061726520736f6d65206e696365206e756d6265727320796f7520676f74207468657265'#correct

    def question3(self):
        question = '110100101010101010100110010?'
        resA = 'Will you shut up?'
        resB = 'Let me get you a psychologist'
        resC = 'How old are you anyways?'
        resD = '6675636b206d792061737320' #correct

    def question4(self):
        question = '1001010101010100101010?'
        resA = 'Stop following me.'
        resB = "My eyes are up here buddy."
        resC = 'I just want to let you know I have pepper spray on me'
        resD = '707573737373737979797979797979' #correct

    def question5(self):
        question = '1101010101010101001'
        resA = 'Why are you getting so close to me?'
        resB = "You still haven't told me your name"
        resC = 'Are you even human?'
        resD = '796f75726520612077697a61726420686172727920' #correct