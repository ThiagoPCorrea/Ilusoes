import pygame

#display_width = 1366
#display_height = 768

display_width = 1280
display_height = 720

#display_width = 800
#display_height = 600

pause = False
gameExit = False
loop = True
crashed = True
ruwin = True
loss = 0
buttonDelay = 0
unlockcount = 0

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

display_size = display_height * display_width
gameDisplay = pygame.display.set_mode((display_width,display_height)) 
clock = pygame.time.Clock() 

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