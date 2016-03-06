#Take that smo
import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 700

black = (0, 0, 0)
white = (255, 255, 255)
grey = (195, 195, 195)

red = (200, 0, 0)
green = (34, 177, 76)
blue = (0, 50, 200)

light_red = (255, 0, 0)
light_blue = (0, 76, 230)
orange = (255, 128, 64)
yellow = (255,255,0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Rubik's Cube")
clock = pygame.time.Clock()

startImg = pygame.image.load('Rubiks.jpg')

def startpic(x,y):
    gameDisplay.blit(startImg, (x,y))
def turns_made(count):
    font = pygame.font.SysFont(None, 50)
    text = font.render("Turns: "+str(count), True, white)
    gameDisplay.blit(text, (0, 0))
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 95)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    cube_intro()
def textBox(msg,x,y,w,h,ic):
    pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf",15)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), y+(h/2) )
    gameDisplay.blit(textSurf, textRect)
def quit_game():
    pygame.quit()
    quit()
def button(msg,x,y,w,h,ic,ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
            
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), y+(h/2) )
    gameDisplay.blit(textSurf, textRect)
def unpause():
    global pause
    pause = False

def paused():

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(black)
        startpic(display_width//4, display_height//6)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("Paused", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Resume",150,550,100,50,blue,light_blue,unpause)
        button("Exit",550, 550, 100, 50,red,light_red,quit_game)
        
        pygame.display.update()
        clock.tick(15)
def cube_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(black)
        startpic(display_width//4, display_height//6)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("Rubik's Cube", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Solve",150,550,100,50,blue,light_blue,solve_loop)
        button("Exit",550, 550, 100, 50,red,light_red,quit_game)
                    
        pygame.display.update()
        clock.tick(15)
def makeSquare(color,x,y):
    pygame.draw.rect(gameDisplay, color, (x, y, 45, 45))
def displaySide(sideList):
    for i in range(9):
        if i == 0:
            x = 50
            y = 50
        elif i == 1:
            x = 100
            y = 50
        elif i == 2:
            x = 150
            y = 50
        elif i == 3:
            x = 50
            y = 100
        elif i == 4:
            x = 100
            y = 100
        elif i == 5:
            x = 150
            y = 100
        elif i == 6:
            x = 50
            y = 150
        elif i == 7:
            x = 100
            y = 150
        else:
            x = 150
            y = 150
        print(i, "sideList", sideList)
        if sideList[i] == 1:
            makeSquare(white,x,y)
        elif sideList[i] == 2:
            makeSquare(red,x,y)
        elif sideList[i] == 3:
            makeSquare(blue,x,y)
        elif sideList[i] == 4:
            makeSquare(orange,x,y)
        elif sideList[i] == 5:
            makeSquare(green,x,y)
        else:
            makeSquare(yellow,x,y)
def cycleSide():
    global side
    if side == whiteSide:
        side = redSide
    elif side == redSide:
        side = blueSide
    elif side == blueSide:
        side = yellowSide
    elif side == yellowSide:
        side = greenSide
    elif side == greenSide:
        side = orangeSide
    else:
        side = whiteSide
    
def solve_loop():
    global pause
    global side
    global whiteSide
    global redSide
    global blueSide
    global orangeSide
    global greenSide
    global yellowSide
    
    x = (display_width/2)
    y = (display_height * .8)

    x_change = 0
    y_change = 0

    turns = 0

    gameExit = False
##    whiteSide = [1,1,1,1,1,1,1,1,1]
##    redSide = [2,2,2,2,2,2,2,2,2]
##    blueSide = [3,3,3,3,3,3,3,3,3]
##    orangeSide = [4,4,4,4,4,4,4,4,4]
##    greenSide = [5,5,5,5,5,5,5,5,5]
##    yellowSide = [6,6,6,6,6,6,6,6,6]
    for i in range(48):

        whiteSide = [random.randrange(1,7) for x in range(4),1,x,x,x,x]
        redSide = [x,x,x,x,2,x,x,x,x]
        blueSide = [x,x,x,x,3,x,x,x,x]
        orangeSide = [x,x,x,x,4,x,x,x,x]
        greenSide = [x,x,x,x,5,x,x,x,x]
        yellowSide = [x,x,x,x,6,x,x,x,x]

    side = whiteSide

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change = -8
                elif event.key == pygame.K_d:
                    x_change = 8
                if event.key == pygame.K_ESCAPE:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    y_change = -8
                elif event.key == pygame.K_s:
                    y_change = 8
                elif event.key == pygame.K_x:
                    cycleSide()
                if event.key == pygame.K_b:
                    cube_intro()


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    y_change = 0

        x += x_change
        y += y_change

        gameDisplay.fill(black)
        textBox("Hit esc to pause",650,0,110,25,grey)
        turns_made(turns)
        displaySide(side)
        pygame.display.update()
        clock.tick(60)

cube_intro()
