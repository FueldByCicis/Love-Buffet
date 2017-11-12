from character import *




class Bojack(Character):

    def _init_(self, win:graphWin):
        super(Character, self)._init_()
        self.name = "Riley Abbott"
        self.woo = 1

    def question1(self):
        question = "Do you like Harry Potter?"
        resA = "What's that?"
        resB = "I've seen the movies."
        resC = "Do I look like a muggle to you? Of course!" ##Correct
        resD = "No I read the first three books and then I got bored."

    def question2(self):
        question = "What does Harry dream about during the summer holiday before his fifth year?"
        resA = "Corridors with dead ends and locked doors." ##correct
        resB = "Being locked in his room."
        resC = "Flying motorcycles."
        resD = "Voldemort's snake: nagini."

    def question3(self):
         question = "How does Felix Felicis behave when in the cauldron?"
         resA = "It spills over the sides."
         resB = "It bubbles merrily." ##correct
         resC = "Droplets leap out like goldfish above the surface."
         resD = "Droplets whizz through the air at speed."

    def question4(self):
        question = "Who replaces Cornelius Fudge as Minister for Magic?"
        resA = "Rufus Scrimgeour." ##correct
        resB = "Arthur Weasley."
        resC = "Kingsley Shacklebolt."
        resD = "Remus Lupin."

    def question5(self):
        question = "What is the name of the sweet that Dudley eats when the Weasleys visit Privet Drive in Harry Potter and the Goblet of Fire?"
        resA = "Ton-tongue toffee." ##correct
        resB = "A fainting fancy."
        resC = "Nosebleed nougat."
        resD = "A puking pastille."

