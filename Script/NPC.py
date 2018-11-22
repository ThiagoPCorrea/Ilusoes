import pygame
pygame.init()
anicounter = 0

def get_faces(sprite,animation,facing = None):
    global anicounter
    if anicounter//10 == 3:
        anicounter = 0
    faces = {}
    size = sprite.get_size()
    #tile_size = (int(size[0] / 2), int(size[1] / 2))
    tile_size = (int(size[0] / 3), int(size[1] / 4))
    south = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    #south.blit(sprite, (0, 0), (0, 0, tile_size[0], tile_size[1]))
    if not animation:
        south.blit(sprite, (0, 0), (tile_size[0], 0, tile_size[0], tile_size[1]))
    elif facing == 'south':
        south.blit(sprite, (0, 0), (tile_size[0]*(anicounter//10), 0, tile_size[0], tile_size[1]))
        anicounter += 1
    faces["south"] = south

    north = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    #north.blit(sprite, (0, 0), (tile_size[0], tile_size[1], tile_size[0], tile_size[1]))
    if not animation:
        north.blit(sprite, (0, 0), (tile_size[0], tile_size[1]*3, tile_size[0], tile_size[1]))
    elif facing == 'north':
        north.blit(sprite, (0, 0), (tile_size[0]*(anicounter//10), tile_size[1]*3, tile_size[0], tile_size[1]))
        anicounter += 1
    faces["north"] = north

    east = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    #east.blit(sprite, (0, 0), (tile_size[0], 0, tile_size[0], tile_size[1]))
    if not animation:
        east.blit(sprite, (0, 0), (tile_size[0],tile_size[1] , tile_size[1], tile_size[1]))
    elif facing == 'east':
        east.blit(sprite, (0, 0), (tile_size[0]*(anicounter//10),tile_size[1] , tile_size[1], tile_size[1]))
        anicounter += 1
    faces["east"] = east

    west = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    #west.blit(sprite, (0, 0), (0, tile_size[1], tile_size[0], tile_size[1]))
    if not animation:
        west.blit(sprite, (0, 0), (tile_size[0], tile_size[1]*2, tile_size[0], tile_size[1]))
    elif facing == 'west':
        west.blit(sprite, (0, 0), (tile_size[0]*(anicounter//10), tile_size[1]*2, tile_size[0], tile_size[1]))
        anicounter += 1
    faces["west"] = west

    return faces


