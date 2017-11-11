from updatedGraphics import *

class Character(object)

    def __init__(self, name, woo:int):
        self.name = name
        self.woo = woo

    def displayHeart(self,heartPicture):
        self.heartPicture = heartPicture.png
        ##display the heart

    def displayFace(self,heartLevel,mehFace,happyFace):
        self.mehFace = mehFace.png
        self.happyFace = happyFace.png
        if heartLevel == 1 or heartLevel == 2:
            ##display meh face
        else:
            ##display happy face
