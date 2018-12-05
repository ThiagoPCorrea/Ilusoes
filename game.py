import pygame
import time
import random
from Script.Globals import *
from Player import *


#Inciando pygame: 
pygame.init()


###Variaveis###
#Tamanho da Tela
#display_width = 1366
#display_height = 768

display_width = 1280
display_height = 720

#display_width = 800
#display_height = 600

display_size = display_height * display_width
gameDisplay = pygame.display.set_mode((display_width,display_height)) 
pygame.display.set_caption('Ilusões') #nome do game na parte superior da tela

#globais
pause = False
gameExit = False
loop = True
crashed = True
ruwin = True
loss = 0
buttonDelay = 0
unlockcount = 0

#pré definições:
#unlock blocks(1x1):
blockwidth = int(display_width*0.1)
blockheight = int(display_height*0.14)
#unlock position(1x1):
posX = display_width*0.1
posY = display_height*0.14


#cores pré definidas(RGB):
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
blue = (0,0,200)
yellow = (255,255,0)

bright_red = (225,0,0)
bright_green = (0,255,0)
bright_blue = (0,0,255)
block_color = (102,51,0)

darker_red = (150,0,0)
#car_width = 44
#car_height = 84
char_width = 48
char_height = 48

#Imagens

#run
crashimg = pygame.image.load('C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Puzzles/crash.jpg')
hole = pygame.image.load('C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Puzzles/hole1.png')

charimg0 = pygame.image.load('C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Personagens/charcut_0.png')
charimg1 = pygame.image.load('C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Personagens/charcut_1.png')
charimg2 = pygame.image.load('C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Personagens/charcut_2.png')

charimg = []
charimg.append(charimg0)
charimg.append(charimg1)
charimg.append(charimg2)

runbg = pygame.image.load('C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Puzzles/Cave.jpg')

#menuimgs
backImg0 = pygame.image.load('C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/BackGrounds/menu1.png')
backImg1 = pygame.image.load('C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/BackGrounds/menu2.png')
backImg2 = pygame.image.load('C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/BackGrounds/menu3.png')
backImg3 = pygame.image.load('C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/BackGrounds/menu4.png')
backImg5 = pygame.image.load('C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/BackGrounds/menu5.png')
backImg6 = pygame.image.load('C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/BackGrounds/menu6.png')
backImg8 = pygame.image.load('C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/BackGrounds/menu7.png')
backImg11 = pygame.image.load('C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/BackGrounds/menu8.png')
backImg = []
backImg.append(backImg0)
backImg.append(backImg1)
backImg.append(backImg2)
backImg.append(backImg3)
backImg.append(backImg8)
backImg.append(backImg5)
backImg.append(backImg6)
backImg.append(backImg11)
backImg.append(backImg0)
backImg.append(backImg1)
backImg.append(backImg2)
backImg.append(backImg3)


#unlock puzzle
woodbkgnd = pygame.image.load('C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Puzzles/wood.jpg')
keyimg = pygame.image.load('C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Puzzles/key2.png')
goldblock = pygame.image.load('C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Puzzles/blocodourado.jpg')
lockbg = pygame.image.load('C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Puzzles/lockbg2.png')
lockend = pygame.image.load('C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Puzzles/lockend2.png')

winimg0 = pygame.image.load('C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Puzzles/lock gif/lock_00.png')
winimg1 = pygame.image.load('C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Puzzles/lock gif/lock_01.png')
winimg2 = pygame.image.load('C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Puzzles/lock gif/lock_02.png')
winimg3 = pygame.image.load('C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Puzzles/lock gif/lock_03.png')
winimg4 = pygame.image.load('C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Puzzles/lock gif/lock_04.png')
winimg5 = pygame.image.load('C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Puzzles/lock gif/lock_05.png')
winimg6 = pygame.image.load('C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Puzzles/lock gif/lock_06.png')
winimg7 = pygame.image.load('C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Puzzles/lock gif/lock_07.png')
winimg8 = pygame.image.load('C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Puzzles/lock gif/lock_08.png')
winimg9 = pygame.image.load('C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Puzzles/lock gif/lock_09.png')
winimg10 = pygame.image.load('C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Puzzles/lock gif/lock_10.png')
winimg11 = pygame.image.load('C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Puzzles/lock gif/lock_11.png')
winimg12 = pygame.image.load('C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Puzzles/lock gif/lock_12.png')
winimg13 = pygame.image.load('C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Puzzles/lock gif/lock_13.png')
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

#PassWord Button
simbol1Bright = pygame.image.load('C:/Users/thiag/Documents/Thiago/Projeto PA4/Simbols/Button1Bright.png')
simbol1Dark = pygame.image.load('C:/Users/thiag/Documents/Thiago/Projeto PA4/Simbols/Button1Dark.png')

simbol2Bright = pygame.image.load('C:/Users/thiag/Documents/Thiago/Projeto PA4/Simbols/Button2Bright.png')
simbol2Dark = pygame.image.load('C:/Users/thiag/Documents/Thiago/Projeto PA4/Simbols/Button2Dark.png')

simbol3Bright = pygame.image.load('C:/Users/thiag/Documents/Thiago/Projeto PA4/Simbols/Button3Bright.png')
simbol3Dark = pygame.image.load('C:/Users/thiag/Documents/Thiago/Projeto PA4/Simbols/Button3Dark.png')

simbol4Bright = pygame.image.load('C:/Users/thiag/Documents/Thiago/Projeto PA4/Simbols/Button4Bright.png')
simbol4Dark = pygame.image.load('C:/Users/thiag/Documents/Thiago/Projeto PA4/Simbols/Button4Dark.png')

simbolBox = pygame.image.load('C:/Users/thiag/Documents/Thiago/Projeto PA4/Simbols/SimbolBox.png')
answerBox = pygame.image.load('C:/Users/thiag/Documents/Thiago/Projeto PA4/Simbols/SimbolBox.png')
answerRound = pygame.image.load('C:/Users/thiag/Documents/Thiago/Projeto PA4/Simbols/SimbolBox.png')

checkButtonBright = pygame.image.load('C:/Users/thiag/Documents/Thiago/Projeto PA4/Simbols/checkblockBright.jpg')
resetButtonBright = pygame.image.load('C:/Users/thiag/Documents/Thiago/Projeto PA4/Simbols/resetblockBright.jpg')
checkButtonDark = pygame.image.load('C:/Users/thiag/Documents/Thiago/Projeto PA4/Simbols/checkblockDark.jpg')
resetButtonDark = pygame.image.load('C:/Users/thiag/Documents/Thiago/Projeto PA4/Simbols/resetblockDark.jpg')


#Sons
#crash_sound = pygame.mixer.Sound("C:/Users/thiag/Documents/GitHub/Ilusoes/Sounds/Car-crash-sound-effect.ogg")
#rain_sound = pygame.mixer.Sound("C:/Users/thiag/Documents/GitHub/Ilusoes/Sounds/The-sound-of-rain.ogg")
#menu_sound = pygame.mixer.Sound("C:/Users/thiag/Documents/GitHub/Ilusoes/Sounds/Soft-piano-music-piano-zen.ogg")
#game_sound = pygame.mixer.Sound("C:/Users/thiag/Documents/GitHub/Ilusoes/Sounds/Electro-punk-action-background-music.ogg")
#pygame.mixer.music.load("C:/Users/thiag/Documents/GitHub/Ilusoes/Sounds/Electro-punk-action-background-music.ogg")

#icone
pygame.display.set_icon(pygame.image.load('C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/GameIcon/carIcon.png'))


###Funções###
#Função para mostrar imagem
def scale(img,w,h):
    img = pygame.transform.scale(img,(w,h))
    return img
def points(text,count,color):
    font = pygame.font.SysFont(None, 25)
    text = font.render(text + str(count), True, color)
    gameDisplay.blit(text,(0,0))

def things(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])

def image(img,x,y):
    gameDisplay.blit(img,(x,y))

def text_objects(text, font, color):
    textSurface = font.render(text, True , color)
    return textSurface, textSurface.get_rect()

def message_display(text,color):
    largeText = pygame.font.Font('C:/windows/fonts/comic.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText, color)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

def crash():
    global crashed
    crashed = True
    #pygame.mixer.music.stop()
    #pygame.mixer.Sound.play(crash_sound)
    while crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit()
        gameDisplay.fill(white)
        #image(crashimg,0,0)
        #text
        message_display('Voce perdeu',bright_red)
        #button(msg,x,y,width,height,icolor,acolor)
        button("Continuar",display_width*0.20,display_height*0.75,100,50,green,bright_green,sair)
        button("Exit",display_width*0.70,display_height*0.75,100,50,red,bright_red,game_quit)
        pygame.display.update()
        clock.tick(60)

def sair():
    global loop
    global pause
    global crashed 
    global gameExit
    global ruwin
    loop = False
    crashed = False
    pause = False
    gameExit = True
    ruwin = False

def imageButton(x,y,width,height,OutImage,OverImage,Value = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    OutImage = scale(OutImage,width,height)
    OverImage = scale(OverImage,width,height)
    if x+width > mouse[0] > x and y+height > mouse[1] > y:
        gameDisplay.blit(OverImage,(x,y))
        if click[0] == 1 and Value != None and buttonDelay == 0:
            return Value
    else:
       gameDisplay.blit(OutImage,(x,y))




#Funcionamento do jogo
clock = pygame.time.Clock() # Clock do jogo

#Escalando imgs
crashimg = scale(crashimg,display_width,display_height)
char_height = int(char_height*(((display_height/600)+(display_width/800))/2))
char_width = int(char_width*((((display_height/600)+(display_width/800)))/2))
#carImg = scale(carImg,car_width,car_height)
woodbkgnd = scale(woodbkgnd,display_width,display_height)
#PassWord
simbolBox = scale(simbolBox,60,60)
answerBox = scale(answerBox,int(display_width*0.90),int(display_height*0.6))

def button(msg,x,y,width,height,icolor,acolor,action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+width > mouse[0] > x and y+height > mouse[1] > y:
        pygame.draw.rect(gameDisplay,acolor,(x,y,width,height))
        if click[0] == 1 and action != None and buttonDelay == 0:
            #pygame.mixer.Sound.stop(crash_sound)
            action()
    else:
        pygame.draw.rect(gameDisplay,icolor,(x,y,width,height))
    smallText = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(msg, smallText, black)
    TextRect.center = ((x+(width/2)),(y+(height/2)))
    gameDisplay.blit(TextSurf,TextRect)

def game_quit():
    pygame.quit()
    quit()

#Menu
def game_intro():
    global buttonDelay
    buttonDelay = 10
    intro = True
    #pygame.mixer.Sound.play(rain_sound,-1)
    #pygame.mixer.Sound.set_volume(rain_sound,0.5)
    #pygame.mixer.Sound.play(menu_sound,-1)
    #pygame.mixer.music.stop()
    t = 0
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit()
        gameDisplay.fill(white)
        if t//10 == 12:
            t=0
        backImg[t//10] = scale(backImg[t//10],display_width,display_height)
        image(backImg[t//10],0,0)
        t+=1
        #text
        message_display("Ilusões",blue)
        #button(msg,x,y,width,height,icolor,acolor)
        button("Car",display_width*0.20,display_height*0.75,100,50,green,bright_green,RunPuzzle)
        button("Sair",display_width*0.70,display_height*0.75,100,50,red,bright_red,game_quit)
        button("Lock",display_width*0.45,display_height*0.75,100,50,blue,bright_blue,unlock)
        pygame.display.update()
        clock.tick(60)
        buttonDelay = buttonDelay - 1
        if (buttonDelay < 0):
            buttonDelay = 0
#pause
def unpause():
    global pause
    pause = False
    pygame.mixer.music.unpause()


def paused():
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit()
        gameDisplay.fill(white)
        #text
        message_display("Paused",black)
        #button(msg,x,y,width,height,icolor,acolor)
        button("Continue",display_width*0.20,display_height*0.75,100,50,green,bright_green,unpause)
        button("Exit",display_width*0.70,display_height*0.75,100,50,red,bright_red,game_quit)
        pygame.display.update()
        clock.tick(60)

#clickanterior = []
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
        #global clickanterior
        use = False
        self.click = pygame.mouse.get_pressed()
        self.mouse = pygame.mouse.get_pos()
        #print(self.x+self.width, self.mouse[0], self.x,self.y+self.height, self.mouse[1], self.y)
        if (((self.x+self.width > self.mouse[0] > self.x and self.y+self.height > self.mouse[1] > self.y) and (self.x >= minlimit and self.x + self.width <= maxlimit)) and not test) or self.move:
            changer = pygame.mouse.get_rel()
            #print((self.x+self.width > self.mouse[0] > self.x and self.y+self.height > self.mouse[1] > self.y) and (self.x >= minlimit and self.x + self.width <= maxlimit))
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
                #clickanterior.append(self.mouse[0])
                #if unlockcount < 2 :
                    #self.x = self.x - (clickanterior[0]-self.mouse[0])
                #else:
                    #self.x = self.x - (clickanterior[unlockcount-1]-self.mouse[0])
                #unlockcount = unlockcount + 1
            else:
                #clickanterior[:] = []
                self.move = False
                unlockcount = 0
        elif(self.x <= minlimit):
            self.x = minlimit
        elif(self.x + self.width > maxlimit):
            self.x = maxlimit - self.width
        elif self.click[0] == 0 and test:
            test = False
        #else:
            #print('kkkk')
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        return use

    def movey(self,minlimit,maxlimit):
        global unlockcount
        global clickcounter
        global loss
        #global clickanterior
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
                #clickanterior.append(self.mouse[1])
                #if unlockcount < 2 :
                    #self.y = self.y - (clickanterior[0]-self.mouse[1])
                #else:
                    #self.y = self.y - (clickanterior[unlockcount-1]-self.mouse[1])
                #unlockcount = unlockcount + 1
            else:
                #clickanterior[:] = []
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




#!def unlockblocks(img,imgx,imgy,imgwdt,imghgt,minlimit,maxlimit):
#!    global clickanterior
#!    global unlockcount
#!    click = pygame.mouse.get_pressed()
#!    mouse = pygame.mouse.get_pos()
#!    img = scale(img,imgwdt,imghgt)
#!    image(img,imgx,imgy)
#!    if (imgx+imgwdt > mouse[0] > imgx and imgy+imghgt > mouse[1] > imgy) and (imgx >= minlimit and imgx + imgwdt <= maxlimit):
#!        if click[0] == 1:
#!            clickanterior.append(mouse[0])
#!            if unlockcount < 2 :
#!                imgx = imgx - (clickanterior[0]-mouse[0])
#!            else:
#!                imgx = imgx - (clickanterior[unlockcount-1]-mouse[0])
#!            unlockcount = unlockcount + 1
#!        else:
#!            clickanterior[:] = []
#!            unlockcount = 0
#!    #elif(imgx <= minlimit):
#!     #   imgx = minlimit
#!    #elif(imgx + imgwdt > maxlimit):
#!     #   imgx = maxlimit - imgwdt
#!    return (imgx,imgy)

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
    #pygame.mixer.Sound.stop(rain_sound)
    #pygame.mixer.Sound.stop(menu_sound)
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
    #keyxy = (posX * 2,posY * 3)
    #block1XY = (posX *5, posY * 6)
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
        #Rect(left, top, width, height)
        #pygame.draw.rect(gameDisplay,green,(display_width*0.15,display_height*0.12,display_width*0.6,display_height*0.84))
        #pygame.draw.rect(gameDisplay,yellow,(display_width*0.798,display_height*0.36,display_width*0.2,display_height*0.14))
        lockbg = scale(lockbg,int(display_width*0.6),int(display_height*0.84))
        lockend = scale(lockend,int(display_width*0.2),int(display_height*0.14))
        #pygame.draw.rect(gameDisplay,green,(display_width*0.1,display_height*0.14,display_width*0.6,display_height*0.84))
        #pygame.draw.rect(gameDisplay,yellow,(display_width*0.7 - 1,display_height*0.42,display_width*0.2,display_height*0.14))
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
        #colidelogic(key,block1)
        #colidelogic(block1,key)
        #@if(key.movex(display_width*0.1,(display_width*0.7 - 1 + display_width*0.2))):
         #@   if(key.colide(block1)):
          #@      if(key.x < block1.x):
            #@        key.x = block1.x-key.width
              #@  elif(key.x > block1.x):
                #@    key.x = block1.x + block1.width
       #@ elif(block1.movey(display_height*0.14,display_height * 0.84 + display_height*0.14)):
         #@   if(block1.colide(key)):
           #@     if(block1.y < key.y):
             #@       block1.y = key.y - block1.height
               #@ elif(block1.y > key.y):
                 #@   block1.y = key.y + key.height
        #keyxy = unlockblocks(keyimg,keyxy[0],keyxy[1],blockwidth*2,blockheight,display_width*0.15,(display_width*0.798+display_width*0.2))
        #block1XY = unlockblocks(goldblock,block1XY[0],block1XY[1],blockwidth*2,blockheight*1,display_width*0.15,(display_width*0.798))
        
#        image(keyimg,keyX,keyY)
#        if (keyX+blockwidth > mouse[0] > keyX and keyY+blockheight > mouse[1] > keyY) and keyX >= display_width*0.1 and keyX + blockwidth <= (display_width*0.795+display_width*0.2):
#            if click[0] == 1:
#                teste.append(mouse[0])
#                if i < 2 :
#                    keyX = keyX - (teste[0]-mouse[0])
#                else:
#                    keyX = keyX - (teste[i-1]-mouse[0])
#                i = i + 1
#            else:
#                teste[:] = []
#                i = 0
#        elif(keyX <= display_width*0.1):
#            keyX = display_width*0.1
#        elif( keyX + blockwidth > display_width*0.798):
#            keyX = display_width*0.795

        pygame.display.update()
        clock.tick(60)

def password():
    global loop
    loop = True
    global loss
    clickcounter = 0
    win = False
    passwordValues = []
    passwordAnswer = []
    AnswerSize = 5
    Acertos = []
    clicked = False
    click = pygame.mouse.get_pressed()
    for x in range(AnswerSize):
        passwordValues.append(random.randint(1,4))
    for x in passwordValues:
        print(x)
    respIniPosX = display_width*0.20
    respIniPosY = display_height*0.25
    respFimPosX = display_width*0.25
    respFimPosY = display_height*0.50
    resp = []
    #pygame.mixer.Sound.stop(rain_sound)
    #pygame.mixer.Sound.stop(menu_sound)
    global pause
    while loop:
        click = pygame.mouse.get_pressed()
        if click[0] == 0:
            clicked = False
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
        image(answerBox,display_width*0.05,display_height*0.4)
        if imageButton(display_width*0.20,display_height*0.15,50,50,simbol1Dark,simbol1Bright,1) != None and clicked == False and len(passwordAnswer) < AnswerSize:
            clicked = True
            passwordAnswer.append(1)
        if imageButton(display_width*0.25,display_height*0.15,50,50,simbol2Dark,simbol2Bright,2) != None and clicked == False and len(passwordAnswer) < AnswerSize:
            passwordAnswer.append(2)
            clicked = True
        if imageButton(display_width*0.30,display_height*0.15,50,50,simbol3Dark,simbol3Bright,3) != None and clicked == False and len(passwordAnswer) < AnswerSize:
            passwordAnswer.append(3)
            clicked = True
        if imageButton(display_width*0.35,display_height*0.15,50,50,simbol4Dark,simbol4Bright,4) != None and clicked == False and len(passwordAnswer) < AnswerSize:
            passwordAnswer.append(4)
            clicked = True
        for x in range(AnswerSize):
            image(simbolBox,respIniPosX-5 + (display_width*(x)*0.1)/2,respIniPosY-5)
            if x <= len(passwordAnswer)-1 and len(passwordAnswer) != 0:
                if passwordAnswer[x] == 1:
                    image(simbol1Bright,respIniPosX + (display_width*(x)*0.1)/2,respIniPosY)
                if passwordAnswer[x] == 2:
                    image(simbol2Bright,respIniPosX + (display_width*(x)*0.1)/2,respIniPosY)
                if passwordAnswer[x] == 3:
                    image(simbol3Bright,respIniPosX + (display_width*(x)*0.1)/2,respIniPosY)
                if passwordAnswer[x] == 4:
                    image(simbol4Bright,respIniPosX + (display_width*(x)*0.1)/2,respIniPosY)
        if imageButton(display_width*0.80,display_height*0.10,140,70,checkButtonDark,checkButtonBright,0) != None and clicked == False and len(passwordAnswer) == AnswerSize:
            clicked = True
            clickcounter = clickcounter + 1
            if (passwordAnswer == passwordValues):
                runwin()
            else:
                resp = []
                entered = False
                Acertos = [[passwordValues[i] == passwordAnswer[j] for j in range(0, len(passwordAnswer))] for i in range(0, len(passwordValues))]
            for index,valor in enumerate(Acertos):
                if(valor[index]):
                    resp.append(1)
                else:
                    for x in valor:
                        if(x and entered == False):
                            entered = True
                            resp.append(2)
                    entered = False
            passwordAnswer = []
        for index,i in enumerate(resp):
            if(i == 1):
                pygame.draw.rect(gameDisplay,green,(respFimPosX*(index+1)/2,respFimPosY*((index+5)//5),50,50))
            elif(i == 2):
                pygame.draw.rect(gameDisplay,yellow,(respFimPosX*(index+1)/2,respFimPosY*((index+5)//5),50,50))
        if imageButton(display_width*0.80,display_height*0.25,140,70,resetButtonDark,resetButtonBright,0) != None and clicked == False:
            clicked = True
            passwordAnswer = []  
    
        points("Tentativa: ",clickcounter,white)
        pygame.display.update()
        clock.tick(60)


def runwin():
    global ruwin
    ruwin = True
    #pygame.mixer.music.stop()
    #pygame.mixer.Sound.play(crash_sound)
    while ruwin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit()
        gameDisplay.fill(white)
        #text
        message_display('Voce Ganhou',bright_red)
        #button(msg,x,y,width,height,icolor,acolor)
        button("Continuar",display_width*0.20,display_height*0.75,100,50,green,bright_green,sair)
        button("Exit",display_width*0.70,display_height*0.75,100,50,red,bright_red,game_quit)
        pygame.display.update()
        clock.tick(60)

def perda():
    global loss
    return loss


#Loop para começar o jogo
def RunPuzzle():
    #pygame.mixer.Sound.stop(rain_sound)
    #pygame.mixer.Sound.stop(menu_sound)
    #pygame.mixer.music.play(-1)
    #pygame.mixer.music.set_volume(0.5)
    global pause
    global hole
    global charimg
    global gameExit
    global runbg
    global loss
    gameExit = False
    bateu = False
    hit = 0
    x = (display_width * 0.60)
    y = (display_height * 0.5)
    x_change = 0
    y_change = 0


    thing_startx = random.randrange(0,display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = random.randrange(50,200)
    thing_height = thing_width
    #thing_height = random.randrange(50,200)
    dodged = 0 
    i = 0
    while not gameExit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit()
            #movimentação   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                #if event.key == pygame.K_UP:
                #    y_change = -5
                #if event.key == pygame.K_DOWN:
                #    y_change = 5
                if event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
                    x_change = 0
                    y_change = 0
                    #pygame.mixer.music.pause()
                    pause = True
                    paused()
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
            
        x += x_change
        y += y_change
        gameDisplay.fill(green)
        #pygame.draw.rect(gameDisplay,black,(display_width*0.25,0,display_width*0.5,display_height))
        #pygame.draw.rect(gameDisplay,yellow,(display_width*0.48,0,display_size/display_size*15,display_height))
        #pygame.draw.rect(gameDisplay,yellow,(display_width*0.52,0,display_size/display_size*15,display_height))
        runbg = scale(runbg,display_width,display_height)
        image(runbg,0,0)
        

        #things(thingx,thingy,thingw,thingh,color)
        #things(thing_startx,thing_starty,thing_width,thing_height,block_color)
        hole = scale(hole,thing_width,thing_height)
        thing_starty += thing_speed
        image(hole,thing_startx,thing_starty)
        if i//10 == 3:
            i=0
        charimg[i//10] = scale(charimg[i//10],char_width,char_height)
        image(charimg[i//10],x,y)
        i+=1
        #image(carImg,x,y)
        #points("Esquivados: ",dodged,black)
        
        if x > display_width - char_width:
            x = display_width - char_width
            #crash()

        if x < 0:
            x = 5
        
        if thing_starty > display_height:
            thing_starty =  0 - display_height
            thing_startx = random.randrange(0,display_width-thing_width)
            dodged += 1
            thing_width = 100 + random.randrange(0,300)
            #thing_height = 100 + random.randrange(0,display_height)
            thing_height = thing_width
            thing_speed += 1
            bateu = False

        if y < thing_starty + thing_height and y + char_height >= thing_starty:

            if (x > thing_startx and x < thing_startx + thing_width or x + char_width > thing_startx and x + char_width < thing_startx + thing_width) and not bateu:
                y += display_height* 0.05
                dodged -= 1
                hit += 1
                bateu = True
                #crash()
        if y + char_height >= display_height:
            loss = hit*8
            crash()
        
        if dodged == 15:
            loss = hit*8
            runwin()
         
        pygame.display.update()
        clock.tick(60)
#game_intro()
#RunPuzzle() 
#game_quit()
