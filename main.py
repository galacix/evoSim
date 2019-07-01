#import pygame
#sys module for exiting the window we create
import pygame, sys, random
#importing useful constants
from pygame.locals import *

#constants representing colors
BLACK = (0, 0, 0)
BROWN = (153, 76, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREY = (220, 220, 220)

#constants representing the different resources
DIRT = 0
GRASS = 1
WATER = 2 
COAL = 3
LAVA = 4
ROCK = 5

#a dictionary linking resources to textures
textures = {
    DIRT  : pygame.image.load('DIRT.png'),
    WATER : pygame.image.load('WATER.png'),
    LAVA  : pygame.image.load('LAVA.png'),
    GRASS : pygame.image.load('GRASS.png'),
    COAL  : pygame.image.load('COAL.png'),
    ROCK  : pygame.image.load('STONE.png')
}

inventory = {
    DIRT  : 0,
    GRASS : 0,
    WATER : 0,
    COAL  : 0,
    ROCK  : 0,
    LAVA  : 0
}
#useful game dimensions
TILESIZE = 20
MAPWIDTH = 30
MAPHEIGHT = 20

#the player image
PLAYER = pygame.image.load('PLAYER.png')
#the pos of the player [x, y]
playerPos = [0, 0]

#a list of resources
resources = [DIRT, GRASS, WATER, COAL, LAVA, ROCK]
#a list representing our tilemap
tilemap = [[DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]

pygame.init()
#creates a drawing surface, ((w,h))
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE + 50))

INVFONT = pygame.font.SysFont('FreeSansBold.ttf', 18)

for rw in range(MAPHEIGHT):
    #loop through each column in the row
    #loop through each column in the row
    for cl in range(MAPWIDTH):
        #pick a random number between 0 and 15
        randomNumber = random.randint(0,50)
        #if a zero, then the tile is coal
        if randomNumber == 0:
            tile = LAVA
        elif randomNumber == 1:
            tile = COAL
        elif randomNumber >= 2 and randomNumber <= 4:
            tile = WATER
        elif randomNumber >= 5 and randomNumber <= 15:
            tile = GRASS
        elif randomNumber >=16 and randomNumber <= 17:
            tile = ROCK
        else:
            tile = DIRT
        tilemap[rw][cl] = tile

while True:
    for event in pygame.event.get():
        if event.type == quit:
            pygame.quit()
            sys.exit()
        # draw the resource at that position in the tilemap, using the correct color\
        elif event.type == KEYDOWN:
            #if the right arrow is pressed
            if event.key == K_d and playerPos[0] < MAPWIDTH - 1:
                #change the player's x position
                playerPos[0] += 1
            if event.key == K_a and playerPos[0] > 0:
                playerPos[0] -= 1
            if event.key == K_w and playerPos[1] > 0:
                playerPos[1] -= 1
            if event.key == K_s and playerPos[1] < MAPHEIGHT - 1:
                playerPos[1] += 1
            if event.key == K_SPACE:
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if currentTile == LAVA or currentTile == WATER:
                    continue
                inventory[currentTile] += 1
                tilemap[playerPos[1]][playerPos[0]] = DIRT

            if event.key == K_1:
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if inventory[DIRT] > 0:
                    inventory [DIRT] -= 1
                    tilemap[playerPos[1]][playerPos[0]] = DIRT
                    inventory [currentTile] += 1

    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE, row*TILESIZE))

    #display the player at the correct position
    DISPLAYSURF.blit(PLAYER,(playerPos[0]*TILESIZE,playerPos[1]*TILESIZE))

    #display the inventory
    placePosition = 10
    for item in resources:
        DISPLAYSURF.blit(textures[item], (placePosition,MAPHEIGHT*TILESIZE+20))
        placePosition += 30
        textObj = INVFONT.render(str(inventory[item]), True, (255, 255, 255), (0, 0, 0))
        DISPLAYSURF.blit(textObj, (placePosition, MAPHEIGHT*TILESIZE+20))
        placePosition += 50

    pygame.display.update()
