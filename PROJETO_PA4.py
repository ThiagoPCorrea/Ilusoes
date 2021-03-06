import pygame, sys, time, math

from Script.ScriptColors import *
from Script.Texturas import *
from Script.Globals import *
from Mapa_engine import *
from NPC import *
from Player import *
from meloonatic_gui import *
from game import *
from Timer import *
from NPCcc import *
#from Script.funcionalidades import *
#from Script.run import RunPuzzle
#from Script.Unlock import unlock


pygame.init()


cSeg = 0
cFrame = 0
FPS = 0
vida0 = pygame.image.load("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Personagens/brain_00.png")
vida1 = pygame.image.load("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Personagens/brain_01.png")
vida2 = pygame.image.load("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Personagens/brain_02.png")
vida3 = pygame.image.load("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Personagens/brain_03.png")
vida4 = pygame.image.load("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Personagens/brain_04.png")
vida5 = pygame.image.load("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Personagens/brain_05.png")
vida6 = pygame.image.load("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Personagens/brain_06.png")
vida = []

vida.append(vida0)
vida.append(vida1)
vida.append(vida2)
vida.append(vida3)
vida.append(vida4)
vida.append(vida5)
vida.append(vida6)


terrain = Map_engine.load_map("C:/Users/thiag/Documents/GitHub/Ilusoes/Mapa/Sala.map")
terrainValue = 1

fps_font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 20)
clock = pygame.time.Clock()
#sky = pygame.image.load("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/BackGrounds/sky.png")
#Sky = pygame.Surface(sky.get_size(), pygame.HWSURFACE)
#Sky.blit(sky,(0, 0))
#del sky

logo_img_temp = pygame.image.load("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/BackGrounds/menu1.png")
logo_img_temp1 = pygame.image.load("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/BackGrounds/menu2.png")
logo_img_temp2 = pygame.image.load("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/BackGrounds/menu3.png")
logo_img_temp3 = pygame.image.load("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/BackGrounds/menu4.png")
logo_img_temp4 = pygame.image.load("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/BackGrounds/menu5.png")
logo_img_temp5 = pygame.image.load("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/BackGrounds/menu6.png")
logo_img_temp6 = pygame.image.load("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/BackGrounds/menu7.png")
logo_img_temp7 = pygame.image.load("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/BackGrounds/menu8.png")
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

#dialog
dialog_background = pygame.image.load("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/gui/dialog1.png")
Dialog_Background = pygame.Surface(dialog_background.get_size(), pygame.HWSURFACE|pygame.SRCALPHA)
Dialog_Background.blit(dialog_background, (0, 0))
Dialog_Background_Width, Dialog_Background_Height = Dialog_Background.get_size()
del dialog_background
#/dialog

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

# NPCs
father = Male1(name = "Steve", pos = (125 , 180), image = pygame.image.load("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Personagens/ppp.png"), dialog = Dialog(text =  [("Hello", "Fine?")]))
daughter = Male1(name = "Anne", pos = (250, 100), image = pygame.image.load("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Personagens/anne.png"), dialog = Dialog(text =  [("hi you", " :)")]))
# /NPC


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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Aberto = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Aberto = False

            if event.key == pygame.K_w or event.key == pygame.K_UP and not Globals.dialog_open:
                player.pressed = True
                Globals.camera_move = 1
                player.facing = "north"

            elif event.key == pygame.K_s or event.key == pygame.K_DOWN and not Globals.dialog_open:
                player.pressed = True
                Globals.camera_move = 2
                player.facing = "south"

            elif event.key == pygame.K_a or event.key == pygame.K_LEFT and not Globals.dialog_open:
                player.pressed = True
                Globals.camera_move = 3
                player.facing = "east"

            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT and not Globals.dialog_open:
                player.pressed = True
                Globals.camera_move = 4
                player.facing = "west"

            if event.key == pygame.K_RETURN:
                if Globals.dialog_open:
                    #HANDLE NEXT PAGE OF OPEN DIALOG
                    if Globals.active_dialog.Page < len(Globals.active_dialog.Text) - 1:
                        Globals.active_dialog.Page += 1
                    else:
                        Globals.dialog_open = False
                        Globals.active_dialog.Page = 0
                        Globals.active_dialog = None
                else:
                    #IF DIALOG ISNT OPEN
                    for npc in NPC.AllNPCs:
                        #IS A PLAYER IN SPEECH BOUNDS
                        #PLAYER COORDS ARE BY TILE!!!
                        #NPC COORDS ARE BY PIXEL!!!
                        #THIS CAUSES CONFUSION!!!
                        npc_x = npc.X / Tiles.Size
                        npc_y = npc.X / Tiles.Size
                        print (npc_y,player_y)
                        if player_x >= npc_x- 2 and player_x <= npc_x + 2 and  player_y >= npc_y - 2 and player_y <= npc_y + 2:
                            #PLAYER IS NEXT TO AN NPX, HOWEVER IS PLAYER FACING NPC?
                            if player.facing == "north" and npc_y < player_y:
                                Globals.dialog_open = True
                                Globals.active_dialog = npc.Dialog
                                npc.Timer.Pause()
                                npc.walking = True
                            elif player.facing == "south" and npc_y > player_y:
                                Globals.dialog_open = True
                                Globals.active_dialog = npc.Dialog
                                npc.Timer.Pause()
                                npc.walking = True 
                            elif player.facing  == "east" and npc_x < player_x:
                                Globals.dialog_open = True
                                Globals.active_dialog = npc.Dialog
                                npc.Timer.Pause()
                                npc.walking = True 
                            elif player.facing == "west" and npc_x > player_x:
                                Globals.dialog_open = True
                                Globals.active_dialog = npc.Dialog
                                npc.Timer.Pause()
                                npc.walking = True

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
            if not Tiles.Blocked_At((round(player_x), math.floor(player_y))) and player.pressed == True:
                Globals.camera_y += 300 * deltatime

            if Tiles.Acao_list((round(player_x), math.floor(player_y))):
                terrain = Map_engine.load_map("C:/Users/thiag/Documents/GitHub/Ilusoes/Mapa/QuartoO.map")
                Globals.camera_x = -863.57
                Globals.camera_y = -88.2
                player.facing = "east"
                terrainValue = 0

            if Tiles.left((round(player_x), math.floor(player_y))):
                terrain = Map_engine.load_map("C:/Users/thiag/Documents/GitHub/Ilusoes/Mapa/Rua.map")
                Globals.camera_x = -86.78
                Globals.camera_y = 131.034
                player.facing = "south"
                terrainValue = 0
            
            if Tiles.enter((round(player_x), math.floor(player_y))):
                terrain = Map_engine.load_map("C:/Users/thiag/Documents/GitHub/Ilusoes/Mapa/Sala.map")
                Globals.camera_x = -146.26
                Globals.camera_y = -364.81
                player.facing = "north"
                terrainValue = 1
            
            if Tiles.senha((round(player_x), math.floor(player_y))):
                password()
                player.pressed = False
                Globals.camera_x = -428.869
                Globals.camera_y = -195.393
                Globals.camera_move = 0
                player.facing = "east"

            if Tiles.Descer((round(player_x), math.floor(player_y))):
                terrain = Map_engine.load_map("C:/Users/thiag/Documents/GitHub/Ilusoes/Mapa/Sala.map")
                Globals.camera_x = -436.3
                Globals.camera_y = -171.42
                player.facing = "south"
                terrainValue = 1
            
            if Tiles.fugir((round(player_x), math.floor(player_y))):
                RunPuzzle()
                player.vida(perda())
                Globals.camera_x = 493
                Globals.camera_y = -81
                Globals.camera_move = 0
                player.pressed = False

            if Tiles.destrancar((round(player_x), math.floor(player_y))):
                player.pressed = False
                unlock()
                player.vida(perda())
                Globals.camera_y = -142
                Globals.camera_x = 379
                Globals.camera_move = 0
                



        elif Globals.camera_move == 2:
            if not Tiles.Blocked_At((round(player_x), math.ceil(player_y))) and player.pressed == True:
                Globals.camera_y -= 300 * deltatime

            if Tiles.Acao_list((round(player_x), math.ceil(player_y))):
                terrain = Map_engine.load_map("C:/Users/thiag/Documents/GitHub/Ilusoes/Mapa/QuartoO.map")
                Globals.camera_x = -863.57
                Globals.camera_y = -88.2
                player.facing = "west"
                terrainValue = 0
            
            if Tiles.left((round(player_x), math.ceil(player_y))):
                terrain = Map_engine.load_map("C:/Users/thiag/Documents/GitHub/Ilusoes/Mapa/Rua.map")
                Globals.camera_x = -86.78
                Globals.camera_y = 131.034
                player.facing = "south"
                terrainValue = 0
            
            if Tiles.enter((round(player_x), math.ceil(player_y))):
                terrain = Map_engine.load_map("C:/Users/thiag/Documents/GitHub/Ilusoes/Mapa/Sala.map")
                Globals.camera_x = -146.26
                Globals.camera_y = -364.81
                player.facing = "north"
                terrainValue = 1
            
            if Tiles.senha((round(player_x), math.ceil(player_y))):
                password()
                player.pressed = False
                Globals.camera_x = -428.869
                Globals.camera_y = -195.393
                Globals.camera_move = 0
                player.facing = "east"

            if Tiles.Descer((round(player_x), math.ceil(player_y))):
                terrain = Map_engine.load_map("C:/Users/thiag/Documents/GitHub/Ilusoes/Mapa/Sala.map")
                Globals.camera_x = -436.3
                Globals.camera_y = -171.42
                player.facing = "south"
                terrainValue = 1

            if Tiles.fugir((round(player_x), math.ceil(player_y))):
                RunPuzzle()
                player.vida(perda())
                Globals.camera_x = 493
                Globals.camera_move = 0
                player.pressed = False

            if Tiles.destrancar((round(player_x), math.ceil(player_y))):
                player.pressed = False
                unlock()
                player.vida(perda())
                Globals.camera_y = -142
                Globals.camera_x = 379
                Globals.camera_move = 0

        elif Globals.camera_move == 3:
            if not Tiles.Blocked_At((math.floor(player_x), round(player_y))) and player.pressed == True:
                Globals.camera_x += 300 * deltatime

            if Tiles.Acao_list((math.floor(player_x), round(player_y))):
                terrain = Map_engine.load_map("C:/Users/thiag/Documents/GitHub/Ilusoes/Mapa/QuartoO.map")
                Globals.camera_x = -863.57
                Globals.camera_y = -88.2
                player.facing = "east"
                terrainValue = 0

            if Tiles.left((math.floor(player_x), round(player_y))):
                terrain = Map_engine.load_map("C:/Users/thiag/Documents/GitHub/Ilusoes/Mapa/Rua.map")
                Globals.camera_x = -86.78
                Globals.camera_y = 131.034
                player.facing = "south"
                terrainValue = 0
            
            if Tiles.enter((math.floor(player_x), round(player_y))):
                terrain = Map_engine.load_map("C:/Users/thiag/Documents/GitHub/Ilusoes/Mapa/Sala.map")
                Globals.camera_x = -146.26
                Globals.camera_y = -364.81
                player.facing = "north"
                terrainValue = 1
            
            if Tiles.senha((math.floor(player_x), round(player_y))):
                password()
                player.pressed = False
                Globals.camera_x = -428.869
                Globals.camera_y = -195.393
                Globals.camera_move = 0
                player.facing = "east"
            
            if Tiles.Descer((math.floor(player_x), round(player_y))):
                terrain = Map_engine.load_map("C:/Users/thiag/Documents/GitHub/Ilusoes/Mapa/Sala.map")
                Globals.camera_x = -436.3
                Globals.camera_y = -171.42
                player.facing = "south"
                terrainValue = 1

            if Tiles.fugir((math.floor(player_x), round(player_y))):
                RunPuzzle()
                player.vida(perda())
                Globals.camera_x = 493
                Globals.camera_move = 0
                player.pressed = False

            if Tiles.destrancar((math.floor(player_x), round(player_y))):
                Globals.camera_y = -142
                Globals.camera_x = 379
                Globals.camera_move = 0
                player.pressed = False
                unlock()
                player.vida(perda())
            

        elif Globals.camera_move == 4:
            if not Tiles.Blocked_At((math.ceil(player_x), round(player_y))) and player.pressed == True:
                Globals.camera_x -= 300 * deltatime

            if Tiles.Acao_list((math.ceil(player_x), round(player_y))):
                terrain = Map_engine.load_map("C:/Users/thiag/Documents/GitHub/Ilusoes/Mapa/QuartoO.map")
                Globals.camera_x = -863.57
                Globals.camera_y = -88.2
                player.facing = "east"
                terrainValue = 0
            
            if Tiles.left((math.ceil(player_x), round(player_y))):
                terrain = Map_engine.load_map("C:/Users/thiag/Documents/GitHub/Ilusoes/Mapa/Rua.map")
                Globals.camera_x = -86.78
                Globals.camera_y = 131.034
                player.facing = "south"
                terrainValue = 0
            
            if Tiles.enter((math.ceil(player_x), round(player_y))):
                terrain = Map_engine.load_map("C:/Users/thiag/Documents/GitHub/Ilusoes/Mapa/Sala.map")
                Globals.camera_x = -146.26
                Globals.camera_y = -364.81
                player.facing = "north"
                terrainValue = 1
            
            if Tiles.senha((math.ceil(player_x), round(player_y))):
                password()
                Globals.camera_x = -428.869
                Globals.camera_y = -195.393
                Globals.camera_move = 0
                player.pressed = False
                player.facing = "east"
            
            if Tiles.Descer((math.ceil(player_x), round(player_y))):
                terrain = Map_engine.load_map("C:/Users/thiag/Documents/GitHub/Ilusoes/Mapa/Sala.map")
                Globals.camera_x = -436.3
                Globals.camera_y = -171.42
                player.facing = "south"
                terrainValue = 1

            if Tiles.fugir((math.ceil(player_x), round(player_y))):
                RunPuzzle()
                player.vida(perda())
                Globals.camera_x = 493
                Globals.camera_move = 0
                player.pressed = False

            if Tiles.destrancar((math.ceil(player_x), round(player_y))):
                Globals.camera_y = -142
                Globals.camera_x = 379
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

    #RENDER NPC
        for npc in NPC.AllNPCs:
            if terrainValue == 1 :
                npc.Render(window)
        #for t in Tiles.Blocked:
          #pygame.draw.rect(window, Color.Red, (t[0] * Tiles.Size + Globals.camera_x, t[1] * Tiles.Size + Globals.camera_y, Tiles.Size, Tiles.Size), 2)

     #DIALOG
        if Globals.dialog_open:
            window.blit(Dialog_Background, (window_width / 2 - Dialog_Background_Width / 2, window_height - Dialog_Background_Height - 2))

            #Draw Dialogs Texts
        
            if Globals.active_dialog != None:
                lines = Globals.active_dialog.Text[Globals.active_dialog.Page]

                for line in lines:
                    #Draw Text to Screen
                    window.blit(Font.Default.render(line, True, Color.Black), (400, (window_height - Dialog_Background_Height) + 30 + (lines.index(line)) * 30))

        #/DIALOG

    
    #Render Menu Scene
    elif Globals.scene == "menu":
        window.fill(Color.Fog)
        logo.Render(window)
        message_display("Ilusões",blue)
        Globals.camera_x = 244.37
        Globals.camera_y = 126.23
        player.facing = "east"
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