import pygame
import os
import time
import random
from funcionalidades import *


pygame.init()

#pré definições:
#unlock blocks(1x1):
blockwidth = int(display_width*0.1)
blockheight = int(display_height*0.14)
#unlock position(1x1):
posX = display_width*0.1
posY = display_height*0.14
woodbkgnd = pygame.image.load('../graphics/Puzzles/wood.jpg')
woodbkgnd = pygame.image.load(os.path.join('../graphics/Puzzles','wood.jpg'))
woodbkgnd = scale(woodbkgnd,display_width,display_height)
keyimg = pygame.image.load('C:/Users/thiag/Documents/Thiago/Projeto PA4/key2.png')
goldblock = pygame.image.load('C:/Users/thiag/Documents/Thiago/Projeto PA4/blocodourado.jpg')
lockbg = pygame.image.load('C:/Users/thiag/Documents/Thiago/Projeto PA4/Sprites/lock/lockbg2.png')
lockend = pygame.image.load('C:/Users/thiag/Documents/Thiago/Projeto PA4/Sprites/lock/lockend2.png')

winimg0 = pygame.image.load('C:/Users/thiag/Documents/Thiago/Projeto PA4/Sprites/lock/lock gif/lock_00.png')
winimg1 = pygame.image.load('C:/Users/thiag/Documents/Thiago/Projeto PA4/Sprites/lock/lock gif/lock_01.png')
winimg2 = pygame.image.load('C:/Users/thiag/Documents/Thiago/Projeto PA4/Sprites/lock/lock gif/lock_02.png')
winimg3 = pygame.image.load('C:/Users/thiag/Documents/Thiago/Projeto PA4/Sprites/lock/lock gif/lock_03.png')
winimg4 = pygame.image.load('C:/Users/thiag/Documents/Thiago/Projeto PA4/Sprites/lock/lock gif/lock_04.png')
winimg5 = pygame.image.load('C:/Users/thiag/Documents/Thiago/Projeto PA4/Sprites/lock/lock gif/lock_05.png')
winimg6 = pygame.image.load('C:/Users/thiag/Documents/Thiago/Projeto PA4/Sprites/lock/lock gif/lock_06.png')
winimg7 = pygame.image.load('C:/Users/thiag/Documents/Thiago/Projeto PA4/Sprites/lock/lock gif/lock_07.png')
winimg8 = pygame.image.load('C:/Users/thiag/Documents/Thiago/Projeto PA4/Sprites/lock/lock gif/lock_08.png')
winimg9 = pygame.image.load('C:/Users/thiag/Documents/Thiago/Projeto PA4/Sprites/lock/lock gif/lock_09.png')
winimg10 = pygame.image.load('C:/Users/thiag/Documents/Thiago/Projeto PA4/Sprites/lock/lock gif/lock_10.png')
winimg11 = pygame.image.load('C:/Users/thiag/Documents/Thiago/Projeto PA4/Sprites/lock/lock gif/lock_11.png')
winimg12 = pygame.image.load('C:/Users/thiag/Documents/Thiago/Projeto PA4/Sprites/lock/lock gif/lock_12.png')
winimg13 = pygame.image.load('C:/Users/thiag/Documents/Thiago/Projeto PA4/Sprites/lock/lock gif/lock_13.png')
winimg = []

winimg.append(winimg0)
winimg.append(winimg1)
winimg.append(winimg2)
winimg.append(winimg3)
winimg.append(winimg4)
winimg.append(winimg5)
winimg.append(winimg6)
winimg.append(winimg7)
winimg.append(winimg8)
winimg.append(winimg9)
winimg.append(winimg10)
winimg.append(winimg11)
winimg.append(winimg12)
winimg.append(winimg13)


def unlock():
    global loop
    loop = True
    global clickcounter
    global test
    global lockbg
    global lockend
    global unlockcount
    global loss
    clickcounter = 0
    win = False
    blocks = []
    key = bloco(posX *3 ,posY * 3,keyimg , blockwidth * 2,blockheight * 1)
    block1 = bloco(posX *5, posY * 3,goldblock,blockwidth * 1 ,blockheight * 2)
    block2 = bloco(posX *5, posY * 5,goldblock,blockwidth * 2 ,blockheight * 1)
    block3 = bloco(posX *5, posY * 2,goldblock,blockwidth * 2 ,blockheight * 1)
    blocks.append(key)
    blocks.append(block1)
    blocks.append(block2)
    blocks.append(block3)
    i = 0
    j = 0
    n = 0
    global pause
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
                    pause = True
                    paused()
                if event.key == pygame.K_l:
                    loop = False
        image(woodbkgnd,0,0)
        lockbg = scale(lockbg,int(display_width*0.6),int(display_height*0.84))
        lockend = scale(lockend,int(display_width*0.2),int(display_height*0.14))
        if not win:
            image(lockbg,display_width*0.1,display_height*0.14)
            image(lockend,display_width*0.7 - 1,display_height*0.42)
            while i < len(blocks):
                blocks[i].render()
                j = 0
                while j < len(blocks):
                    if i != j and i == 0:
                        colidelogic(blocks[i],blocks[j],display_width*0.2)
                    elif i != j:
                        colidelogic(blocks[i],blocks[j])
                    j = j + 1
                i = i + 1
            i = 0
        else:
            if n//5 == 14:
                n=0
                sair()
                break
            
            winimg[n//5] = scale(winimg[n//5],display_width,display_height)
            image(winimg[n//5],0,0)
            n+=1
        if key.x >= (display_width*0.7) -1:
            win = True
        points("Moves: ",clickcounter,white)

        pygame.display.update()
        clock.tick(60)

def colidelogic(bm,bt,kextra = 0):
    if(bm.width > bm.height):
        if(bm.movex(display_width*0.1,(display_width*0.7 - 1 + kextra))):
            if(bm.colide(bt)):
                if(bm.x < bt.x):
                    bm.x = bt.x-bm.width
                elif(bm.x > bt.x):
                    bm.x = bt.x + bt.width
    elif(bm.width < bm.height):
        if(bm.movey(display_height*0.14, (display_height * 0.84) + (display_height*0.14))):
            if(bm.colide(bt)):
                if(bm.y < bt.y):
                    bm.y = bt.y - bm.height
                elif(bm.y > bt.y):
                    bm.y = bt.y + bt.height

changer = 0
clickcounter = 0
test = False
class bloco:
    def __init__(self,x,y,img,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.img = scale(img,width,height)
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        self.move = False
    def render(self):
        image(self.img,self.x,self.y)
        
    def movex(self,minlimit,maxlimit):
        global unlockcount
        global clickcounter
        global test
        global loss
        use = False
        self.click = pygame.mouse.get_pressed()
        self.mouse = pygame.mouse.get_pos()
        if (((self.x+self.width > self.mouse[0] > self.x and self.y+self.height > self.mouse[1] > self.y) and (self.x >= minlimit and self.x + self.width <= maxlimit)) and not test) or self.move:
            changer = pygame.mouse.get_rel()
            if self.click[0] == 1:
                self.move = True
                test = True
                use = True
                if(self.x <= minlimit):
                    self.x = minlimit
                elif(self.x + self.width > maxlimit):
                    self.x = maxlimit - self.width
                if blockwidth > changer[0] > -blockwidth:
                    self.x = self.x + changer[0]
                if unlockcount == 0 and changer[1] != 0:
                    clickcounter = clickcounter + 1
                    loss = (clickcounter * 5)
                    unlockcount = 1
            else:
                self.move = False
                unlockcount = 0
        elif(self.x <= minlimit):
            self.x = minlimit
        elif(self.x + self.width > maxlimit):
            self.x = maxlimit - self.width
        elif self.click[0] == 0 and test:
            test = False
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        return use

    def movey(self,minlimit,maxlimit):
        global unlockcount
        global clickcounter
        global loss
        global changer
        global test
        use = False
        self.click = pygame.mouse.get_pressed()
        self.mouse = pygame.mouse.get_pos()
        if ((self.x+self.width > self.mouse[0] > self.x and self.y+self.height > self.mouse[1] > self.y) and (self.y >= minlimit and self.y + self.height <= maxlimit) and not test) or self.move:
            changer = pygame.mouse.get_rel()
            if self.click[0] == 1:
                self.move = True
                use = True
                test = True
                if(self.y <= minlimit):
                    self.y = minlimit
                if(self.y + self.height > maxlimit):
                    self.y = maxlimit - self.height
                if blockheight > changer[1] > -blockheight:
                    self.y = self.y + changer[1]
                if unlockcount == 0 and changer[1] != 0:
                    clickcounter = clickcounter + 1
                    loss = (clickcounter * 5)
                    unlockcount = 1
            else:
                self.move = False
                unlockcount = 0
        elif(self.y <= minlimit):
            self.y = minlimit
        elif(self.y + self.height >= maxlimit):
            self.y = maxlimit - self.height
        elif self.click[0] == 0 and test:
            test = False

        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        return use

    def colide(self,bloco):
        return self.rect.colliderect(bloco.rect)
