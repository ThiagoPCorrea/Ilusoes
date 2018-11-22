import pygame
import os
import time
import random
from funcionalidades import *

crashimg = pygame.image.load('C:/Users/thiag/Documents/Thiago/Projeto PA4/crash.jpg')
hole = pygame.image.load('C:/Users/thiag/Documents/Thiago/Projeto PA4/Sprites/run/hole1.png')

charimg0 = pygame.image.load('C:/Users/thiag/Documents/Thiago/Projeto PA4/Sprites/sprites cortadas/charcut/charcut_0.png')
charimg1 = pygame.image.load('C:/Users/thiag/Documents/Thiago/Projeto PA4/Sprites/sprites cortadas/charcut/charcut_1.png')
charimg2 = pygame.image.load('C:/Users/thiag/Documents/Thiago/Projeto PA4/Sprites/sprites cortadas/charcut/charcut_2.png')

charimg = []
charimg.append(charimg0)
charimg.append(charimg1)
charimg.append(charimg2)

crashimg = scale(crashimg,display_width,display_height)
char_height = int(char_height*(((display_height/600)+(display_width/800))/2))
char_width = int(char_width*((((display_height/600)+(display_width/800)))/2))

runbg = pygame.image.load('C:/Users/thiag/Documents/Thiago/Projeto PA4/Sprites/run/Cave.jpg')

def RunPuzzle():
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
                if event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
                    x_change = 0
                    y_change = 0
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
        runbg = scale(runbg,display_width,display_height)
        image(runbg,0,0)
        

        hole = scale(hole,thing_width,thing_height)
        thing_starty += thing_speed
        image(hole,thing_startx,thing_starty)
        if i//10 == 3:
            i=0
        charimg[i//10] = scale(charimg[i//10],char_width,char_height)
        image(charimg[i//10],x,y)
        i+=1
        
        if x > display_width - char_width:
            x = display_width - char_width

        if x < 0:
            x = 5
        
        if thing_starty > display_height:
            thing_starty =  0 - display_height
            thing_startx = random.randrange(0,display_width-thing_width)
            dodged += 1
            thing_width = 100 + random.randrange(0,300)
            thing_height = thing_width
            thing_speed += 1
            bateu = False

        if y < thing_starty + thing_height and y + char_height >= thing_starty:

            if (x > thing_startx and x < thing_startx + thing_width or x + char_width > thing_startx and x + char_width < thing_startx + thing_width) and not bateu:
                y += display_height* 0.05
                dodged -= 1
                hit += 1
                bateu = True
        if y + char_height >= display_height:
            loss = hit*8
            crash()
        
        if dodged == 15:
            loss = hit*8
            runwin()
         
        pygame.display.update()
        clock.tick(60)


def runwin():
    global ruwin
    ruwin = True
    while ruwin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit()
        gameDisplay.fill(white)
        #text
        message_display('Voce Ganhou',bright_red)
        button("Continuar",display_width*0.20,display_height*0.75,100,50,green,bright_green,sair)
        button("Exit",display_width*0.70,display_height*0.75,100,50,red,bright_red,game_quit)
        pygame.display.update()
        clock.tick(60)

def perda():
    global loss
    return loss
