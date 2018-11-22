import pygame
from Script.Texturas import *

class Map_engine:

    def add_tile(tile, pos, addTo):
        addTo.blit(tile, (pos[0] * Tiles.Size, pos[1] * Tiles.Size))

    def load_map(file):
        with open(file, "r") as mapfile:
            map_data = mapfile.read()

        #Read Tile Data
        map_data = map_data.split("-")     #Split into list of tiles
        map_size = map_data[len(map_data) - 1]  #Get map dimensions
        map_data.remove(map_size)
        map_size = map_size.split(",")
        map_size[0] = int(map_size[0]) * Tiles.Size
        map_size[1] = int(map_size[1]) * Tiles.Size

        tiles = []
        Tiles.Blocked[:] = []
        Tiles.Acao[:] = []
        Tiles.Descida[:] = []
        Tiles.chest[:] = []
        Tiles.run[:] = []

        for tile in range(len(map_data)):
            map_data[tile] = map_data[tile].replace("\n", "")
            tiles.append(map_data[tile].split(":"))  #Split pos from textures
        
        for tile in tiles:
            tile[0] = tile[0].split(",") #Split pos into list
            pos = tile[0]

            for p in pos:
                pos[pos.index(p)] = int(p) #Convert to integer

            tiles[tiles.index(tile)] = (pos, tile[1]) #Save to tile list

        #Create Terrain
        terrain = pygame.Surface(map_size, pygame.HWSURFACE)

        for tile in tiles:
            if tile[1] in Tiles.Texture_Tags:
                Map_engine.add_tile(Tiles.Texture_Tags[tile[1]], tile[0], terrain)
            if tile[1] in Tiles.Blocked_Types:
                Tiles.Blocked.append(tile[0])
            if tile[1] in Tiles.Acao_list2:
                Tiles.Acao.append(tile[0])
            if tile[1] in Tiles.Descida2:
                Tiles.Descida.append(tile[0])
            if tile[1] in Tiles.runevent:
                Tiles.run.append(tile[0])
            if tile[1] in Tiles.chestevet:
                Tiles.chest.append(tile[0])
        return terrain

