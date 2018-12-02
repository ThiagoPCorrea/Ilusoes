import pygame
from Script.NPC import *

pygame.init()

class Player:
    def __init__(self, name):
        self.name = name
        self.facing = "south"
        self.health = 100
        self.sprite = pygame.image.load("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Personagensfilho.png")
        size = self.sprite.get_size()
        self.width = size[0]
        self.height = size[1]
        self.pressed = False

        #Get Player Faces
        self.faces = get_faces(self.sprite,self.pressed,self.facing)   

    def render(self, surface, pos):
        self.faces = get_faces(self.sprite,self.pressed,self.facing) 
        surface.blit(self.faces[self.facing], pos)

    def vida(self, loss = None):
        self.health -= loss
