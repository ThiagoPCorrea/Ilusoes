import pygame, sys, time, math

from Script.ScriptColors import *
from Script.Texturas import *
from Script.Globals import *
from Mapa_engine import *
from Script.NPC import *
from Player import *
from meloonatic_gui import *
#from game import *
from Script.funcionalidades import *
from Script.run import *
from Script.Unlock import *

pygame.init()

cSeg = 0
cFrame = 0
FPS = 0
vida0 = pygame.image.load("C:/Users/thiag/Documents/Thiago/Projeto PA4/Sprites/Brain/brain_00.png")
vida1 = pygame.image.load("C:/Users/thiag/Documents/Thiago/Projeto PA4/Sprites/Brain/brain_01.png")
vida2 = pygame.image.load("C:/Users/thiag/Documents/Thiago/Projeto PA4/Sprites/Brain/brain_02.png")
vida3 = pygame.image.load("C:/Users/thiag/Documents/Thiago/Projeto PA4/Sprites/Brain/brain_03.png")
vida4 = pygame.image.load("C:/Users/thiag/Documents/Thiago/Projeto PA4/Sprites/Brain/brain_04.png")
vida5 = pygame.image.load("C:/Users/thiag/Documents/Thiago/Projeto PA4/Sprites/Brain/brain_05.png")
vida6 = pygame.image.load("C:/Users/thiag/Documents/Thiago/Projeto PA4/Sprites/Brain/brain_06.png")
vida = []

vida.append(vida0)
vida.append(vida1)
vida.append(vida2)
vida.append(vida3)
vida.append(vida4)
vida.append(vida5)
vida.append(vida6)







terrain = Map_engine.load_map("C:/Users/thiag/Documents/Thiago/Projeto PA4/MardoCode/PA4_Jogo/Mapa/Sala.map")

fps_font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 20)
clock = pygame.time.Clock()
#sky = pygame.image.load("C:/Users/thiag/Documents/Thiago/Projeto PA4/MardoCode/PA4_Jogo/graphics/sky.png")
#Sky = pygame.Surface(sky.get_size(), pygame.HWSURFACE)
#Sky.blit(sky,(0, 0))
#del sky

logo_img_temp = pygame.image.load("C:/Users/thiag/Documents/Thiago/Projeto PA4/MardoCode/PA4_Jogo/graphics/menu1.png")
logo_img_temp1 = pygame.image.load("C:/Users/thiag/Documents/Thiago/Projeto PA4/MardoCode/PA4_Jogo/graphics/menu2.png")
logo_img_temp2 = pygame.image.load("C:/Users/thiag/Documents/Thiago/Projeto PA4/MardoCode/PA4_Jogo/graphics/menu3.png")
logo_img_temp3 = pygame.image.load("C:/Users/thiag/Documents/Thiago/Projeto PA4/MardoCode/PA4_Jogo/graphics/menu4.png")
logo_img_temp4 = pygame.image.load("C:/Users/thiag/Documents/Thiago/Projeto PA4/MardoCode/PA4_Jogo/graphics/menu5.png")
logo_img_temp5 = pygame.image.load("C:/Users/thiag/Documents/Thiago/Projeto PA4/MardoCode/PA4_Jogo/graphics/menu6.png")
logo_img_temp6 = pygame.image.load("C:/Users/thiag/Documents/Thiago/Projeto PA4/MardoCode/PA4_Jogo/graphics/menu7.png")
logo_img_temp7 = pygame.image.load("C:/Users/thiag/Documents/Thiago/Projeto PA4/MardoCode/PA4_Jogo/graphics/menu8.png")
backImg = []
backImg.append(logo_img_temp)
backImg.append(logo_img_temp1)
backImg.append(logo_img_temp2)
backImg.append(logo_img_temp3)
backImg.append(logo_img_temp4)
backImg.append(logo_img_temp5)
backImg.append(logo_img_temp6)
backImg.append(logo_img_temp7)
backImg.append(logo_img_temp)
backImg.append(logo_img_temp1)
backImg.append(logo_img_temp2)
backImg.append(logo_img_temp3)

x = 0

window_height, window_width = 0, 0

def show_fps():
    fps_overlay = fps_font.render(str(FPS), True, Color.White)
    window.blit(fps_overlay, (0, 0))

def create_window():
    global window, window_height, window_width, window_title
    #window_width, window_height = 800, 600
    window_width, window_height = display_width,display_height
    window_title = "Ilusões"
    pygame.display.set_caption(window_title)
    #window = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE|pygame.DOUBLEBUF)
    window = gameDisplay



def count_fps():
    global cSeg, cFrame, FPS, deltatime
    if cSeg == time.strftime("%S"):
        cFrame += 1

    else:
        FPS = cFrame
        cFrame = 0
        cSeg = time.strftime("%S")

        if FPS > 0:
            deltatime = 1 / FPS


create_window()
logo_img = pygame.Surface((window_width, window_height), pygame.HWSURFACE)


player = Player("Joao")
player_w, player_h = player.width, player.height
player_x = (window_width / 2 - player_w / 2 - Globals.camera_x) / Tiles.Size
player_y = (window_height / 2 - player_h / 2 - Globals.camera_y) / Tiles.Size


#Initialize GUI
def Play():
    Globals.scene = "game"

def Exit():
    global Aberto
    Aberto = False

btnPlay = Menu.Button(text = "Play", rect = (window_width * 0.70, window_height * 0.80, window_width * 0.2, window_height * 0.1), bg = Color.Gray, fg = Color.White, bgr = Color.CornflowerBlue, tag = ("menu", None))
btnPlay.Command = Play

btnExit = Menu.Button(text = "Exit", rect = (window_width * 0.10, window_height * 0.80, window_width * 0.2, window_height * 0.1), bg = Color.Gray, fg = Color.White, bgr = Color.CornflowerBlue, tag = ("menu", None))
btnExit.Command = Exit

logo = Menu.Image(bitmap = logo_img)

Aberto = True

while Aberto:
    print(player.health)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Aberto = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Aberto = False

            if event.key == pygame.K_w or event.key == pygame.K_UP:
                player.pressed = True
                Globals.camera_move = 1
                player.facing = "north"

            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.pressed = True
                Globals.camera_move = 2
                player.facing = "south"

            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.pressed = True
                Globals.camera_move = 3
                player.facing = "east"

            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.pressed = True
                Globals.camera_move = 4
                player.facing = "west"

        elif event.type == pygame.KEYUP:
            Globals.camera_move = 0
            player.pressed = False
        

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: #left click
                for btn in Menu.Button.All:
                    if btn.Tag[0] == Globals.scene and btn.Rolling:
                        if btn.Command != None:
                            btn.Command()
                        btn.Rolling = False
                        break


    #Render Game Scene
    if Globals.scene == "game":



        #LOGICA
#        if Globals.camera_move == 1:
#            if not Tiles.Blocked_At((round(player_x), math.floor(player_y))):
#                Globals.camera_y += 300 * deltatime
#
#        elif Globals.camera_move == 2:
#            if not Tiles.Blocked_At((round(player_x), math.ceil(player_y))):
#                Globals.camera_y -= 300 * deltatime
#
#        elif Globals.camera_move == 3:
#            if not Tiles.Blocked_At((math.floor(player_x), round(player_y))):
#                Globals.camera_x += 300 * deltatime
#
#        elif Globals.camera_move == 4:
#            if not Tiles.Blocked_At((math.ceil(player_x), round(player_y))):
#                Globals.camera_x -= 300 * deltatime
        #LOGICA
        if Globals.camera_move == 1:
            if not Tiles.Blocked_At((round(player_x), math.floor(player_y))):
                Globals.camera_y += 300 * deltatime

            if Tiles.Acao_list((round(player_x), math.floor(player_y))):
                terrain = Map_engine.load_map("C:/Users/thiag/Documents/Thiago/Projeto PA4/MardoCode/PA4_Jogo/Mapa/QuartoO.map")
                Globals.camera_x = -863.57
                Globals.camera_y = -88.2
                player.facing = "east"

            if Tiles.Descer((round(player_x), math.floor(player_y))):
                terrain = Map_engine.load_map("C:/Users/thiag/Documents/Thiago/Projeto PA4/MardoCode/PA4_Jogo/Mapa/Sala.map")
                Globals.camera_x = -436.3
                Globals.camera_y = -171.42
                player.facing = "south"
            if Tiles.fugir((round(player_x), math.floor(player_y))):
                RunPuzzle()
                player.vida(perda())
                Globals.camera_x = 493
                Globals.camera_move = 0
                player.pressed = False
            if Tiles.destrancar((round(player_x), math.floor(player_y))):
                Globals.camera_y = -142
                Globals.camera_move = 0
                player.pressed = False
                unlock()
                player.vida(perda())
                



        elif Globals.camera_move == 2:
            if not Tiles.Blocked_At((round(player_x), math.ceil(player_y))):
                Globals.camera_y -= 300 * deltatime

            if Tiles.Acao_list((round(player_x), math.ceil(player_y))):
                terrain = Map_engine.load_map("C:/Users/thiag/Documents/Thiago/Projeto PA4/MardoCode/PA4_Jogo/Mapa/QuartoO.map")
                Globals.camera_x = -863.57
                Globals.camera_y = -88.2
                player.facing = "west"

            if Tiles.Descer((round(player_x), math.ceil(player_y))):
                terrain = Map_engine.load_map("C:/Users/thiag/Documents/Thiago/Projeto PA4/MardoCode/PA4_Jogo/Mapa/Sala.map")
                Globals.camera_x = -436.3
                Globals.camera_y = -171.42
                player.facing = "south"
            if Tiles.fugir((round(player_x), math.ceil(player_y))):
                RunPuzzle()
                player.vida(perda())
                Globals.camera_x = 493
                Globals.camera_move = 0
                player.pressed = False
            if Tiles.destrancar((round(player_x), math.ceil(player_y))):
                Globals.camera_y = -142
                Globals.camera_move = 0
                player.pressed = False
                unlock()
                player.vida(perda())

        elif Globals.camera_move == 3:
            if not Tiles.Blocked_At((math.floor(player_x), round(player_y))):
                Globals.camera_x += 300 * deltatime

            if Tiles.Acao_list((math.floor(player_x), round(player_y))):
                terrain = Map_engine.load_map("C:/Users/thiag/Documents/Thiago/Projeto PA4/MardoCode/PA4_Jogo/Mapa/QuartoO.map")
                Globals.camera_x = -863.57
                Globals.camera_y = -88.2
                player.facing = "east"
            
            if Tiles.Descer((math.floor(player_x), round(player_y))):
                terrain = Map_engine.load_map("C:/Users/thiag/Documents/Thiago/Projeto PA4/MardoCode/PA4_Jogo/Mapa/Sala.map")
                Globals.camera_x = -436.3
                Globals.camera_y = -171.42
                player.facing = "south"
            if Tiles.fugir((math.floor(player_x), round(player_y))):
                RunPuzzle()
                player.vida(perda())
                Globals.camera_x = 493
                Globals.camera_move = 0
                player.pressed = False
            if Tiles.destrancar((math.floor(player_x), round(player_y))):
                Globals.camera_y = -142
                Globals.camera_move = 0
                player.pressed = False
                unlock()
                player.vida(perda())
            

        elif Globals.camera_move == 4:
            if not Tiles.Blocked_At((math.ceil(player_x), round(player_y))):
                Globals.camera_x -= 300 * deltatime

            if Tiles.Acao_list((math.ceil(player_x), round(player_y))):
                terrain = Map_engine.load_map("C:/Users/thiag/Documents/Thiago/Projeto PA4/MardoCode/PA4_Jogo/Mapa/QuartoO.map")
                Globals.camera_x = -863.57
                Globals.camera_y = -88.2
                player.facing = "east"
            
            if Tiles.Descer((math.ceil(player_x), round(player_y))):
                terrain = Map_engine.load_map("C:/Users/thiag/Documents/Thiago/Projeto PA4/MardoCode/PA4_Jogo/Mapa/Sala.map")
                Globals.camera_x = -436.3
                Globals.camera_y = -171.42
                player.facing = "south"
            if Tiles.fugir((math.floor(player_x), round(player_y))):
                RunPuzzle()
                player.vida(perda())
                Globals.camera_x = 493
                Globals.camera_move = 0
                player.pressed = False

            if Tiles.destrancar((math.floor(player_x), round(player_y))):
                Globals.camera_y = -142
                Globals.camera_move = 0
                player.pressed = False
                unlock()
                player.vida(perda())

        player_x = (window_width / 2 - player_w / 2 - Globals.camera_x) / Tiles.Size
        player_y = (window_height / 2 - player_h / 2 - Globals.camera_y) / Tiles.Size


        #RENDERIZAÇAO GRAFICA
        #window.blit(Sky, (0, 0))
        window.fill(black)
        window.blit(terrain, (Globals.camera_x, Globals.camera_y))
        player.render(window, (window_width / 2 - player_w / 2, window_height / 2 - player_h / 2))
        if player.health > 75:
            vida[0] = scale(vida[0],int(display_width*0.15),int(display_height*0.15))
            image(vida[0],display_width*0.85,display_height*0.8)
        elif player.health > 50:
            vida[1] = scale(vida[1],int(display_width*0.15),int(display_height*0.15))
            image(vida[1],display_width*0.85,display_height*0.8)
        elif player.health > 30:
            vida[2] = scale(vida[2],int(display_width*0.15),int(display_height*0.15))
            image(vida[2],display_width*0.85,display_height*0.85)
        elif player.health > 25:
            vida[3] = scale(vida[3],int(display_width*0.15),int(display_height*0.15))
            image(vida[3],display_width*0.85,display_height*0.8)
        elif player.health > 10:
            vida[4] = scale(vida[4],int(display_width*0.15),int(display_height*0.15))
            image(vida[4],display_width*0.85,display_height*0.8)
        elif player.health <= 0:
            vida[5] = scale(vida[5],int(display_width*0.1),int(display_height*0.15))
            image(vida[5],display_width*0.85,display_height*0.8)
    #RENDERIZAÇAO GRAFICA - SIMPLES TERRENO
    
    #Render Menu Scene
    elif Globals.scene == "menu":
        window.fill(Color.Fog)
        logo.Render(window)
        message_display("Ilusões",blue)
        Globals.camera_x, Globals.camera_y = 0,0
        if x//10 == 12:
            x = 0
        
        backImg[x//10] = pygame.transform.scale(backImg[x//10], (window_width, window_height))
        #logo_img = pygame.Surface(backImg[x//10].get_size(), pygame.HWSURFACE)
        logo_img.blit(backImg[x//10], (0, 0))
        x = x + 1

        for btn in Menu.Button.All:
            if btn.Tag[0] == "menu":
                btn.Render(window)

    show_fps()
    pygame.display.update()
    count_fps()
    clock.tick(60)

pygame.quit()
sys.exit()