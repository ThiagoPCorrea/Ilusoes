import pygame

pygame.init()

class Tiles:
    
    Size = 32

    Acao = []
    Acao_list2 = ["106", "70"]

    Blocked = []
    Blocked_Types = ["2", "3", "4", "5", "6", "10", "11", "14", "15", "16", "17", "18", "22", "23", "24", "32", "33", "34", "35"
    , "36", "37", "38", "39", "41", "44", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "60", "61", "62", "71", "72", "65", "64", "78", "79", "80", "81", "88", "89", "90"
    , "93", "94", "95", "96", "107", "108", "111", "112", "113", "114", "115", "116", "117", "118", "119", "120", "121", "122", "123", "124", "125", "126", "127", "128", "129", "130", "131", "132", "133"]

    Descida = []
    Descida2 = ["77"]

    chest = []
    chestevet = ["106"]

    run = []
    runevent = ["82","83","91","92"]

    entrar = []
    entrou = ["73","74"]

    sair = []
    saiu = ["135"]

    password = []
    passwordEnter = ["134"]

    def left(pos):    
        if list(pos) in Tiles.sair:
            return True
        else:
            return False


    def enter(pos):    
        if list(pos) in Tiles.entrar:
            return True
        else:
            return False


    def senha(pos):    
        if list(pos) in Tiles.password:
            return True
        else:
            return False

    def destrancar(pos):    
        if list(pos) in Tiles.chest:
            return True
        else:
            return False

    def fugir(pos):    
        if list(pos) in Tiles.run:
            return True
        else:
            return False


    def Descer(pos):    
        if list(pos) in Tiles.Descida:
            return True
        else:
            return False

    def Acao_list(pos):
        if list(pos) in Tiles.Acao:
            return True
        else:
            return False

    def Blocked_At(pos):
        if list(pos) in Tiles.Blocked:
            return True
        
        else:
            return False

    def Load_Texture(file, Size):
        bitmap = pygame.image.load(file)
        bitmap = pygame.transform.scale(bitmap, (Size, Size))
        surface = pygame.Surface((Size, Size), pygame.HWSURFACE|pygame.SRCALPHA)
        surface.blit(bitmap, (0, 0))
        return surface
    
    Grass = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Rua/sprites34_017.png", Size)

    

    #PAREDE
    ParedeMad1 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Paredes_Teto/sprites15_222.png", Size)
    ParedeMad2 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Paredes_Teto/sprites15_223.png", Size)
    ParedeMad3 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Paredes_Teto/sprites15_238.png", Size)
    ParedeMad4 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Paredes_Teto/sprites15_239.png", Size)
    ParedeMad5 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Paredes_Teto/sprites15_240.png", Size)

    #CHAO
    ChaoMad = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Chao/sprites16_048.png", Size)
    ChaoCoz = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Acabamentos/sprites18_037.png", Size)

    #MOBILIAS
    #Sala
    Sofa1 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites8_061.png", Size)
    Sofa2 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites8_062.png", Size)
    Sofa3 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites8_044.png", Size)
    Sofa4 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites8_060.png", Size)
    Sofa5 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites8_043.png", Size)
    Sofa6 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites8_059.png", Size)

    Mesa1 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Chao/sprites16_046.png", Size)
    Mesa2 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Chao/sprites16_047.png", Size)
    Mesa3 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Paredes_Teto/sprite15_0001.png", Size)
    Mesa4 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Chao/sprites6_0001.png", Size)
    

    Lareira1 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites19_011.png", Size)
    Lareira2 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites19_027.png", Size)

    Janela1 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites19_064.png", Size)
    Janela2 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites19_080.png", Size)

    Prateleira2 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites19_241.png", Size)

    Estante1 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites8_104.png", Size)
    Estante2 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites8_120.png", Size)

    Relogio1 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites19_071.png", Size)
    Relogio2 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites19_087.png", Size)

    #Cozinha
    Geladeira1 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites8_103.png", Size)
    Geladeira2 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites8_119.png", Size)

    Fogao = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites19_223.png", Size)
    Pia1 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites19_224.png", Size)
    Pia2 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites19_225.png", Size)
    Pia3 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites19_226.png", Size)

    Estante3 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites19_127.png", Size)
    Estante4 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites19_143.png", Size)

    Mesa5 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites19_191.png", Size)
    Banquinho = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites19_207.png", Size)
    Cenoura = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites19_231.png", Size)
    
    Prateleira1 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites19_243.png", Size)
    Prateleira3 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites19_242.png", Size)

    Comida = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites20_096.png", Size)

    #Sala Cultural
    Piano1 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites9_059.png", Size)
    Piano2 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites9_060.png", Size)
    Piano3 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites9_061.png", Size)
    Piano4 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites9_075.png", Size)
    Piano5 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites9_076.png", Size)
    Piano6 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites9_077.png", Size)

    Lareira3 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites9_091.png", Size)
    Lareira4 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites9_092.png", Size)
    Lareira5 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites9_093.png", Size)
    Lareira6 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites9_107.png", Size)
    Lareira7 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites9_108.png", Size)
    Lareira8 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites9_109.png", Size)

    Espelho1 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites9_057.png", Size)
    Espelho2 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites9_073.png", Size)

    Vaso1 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites9_058.png", Size)
    Vaso2 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites9_071.png", Size)
    Vaso3 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites9_087.png", Size)

    Banquinho2 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites9_032.png", Size)

    Estatua1 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites9_170.png", Size)
    Estatua2 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites9_186.png", Size)

    Tapete1 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Chao/sprites16_068.png", Size)
    Tapete2 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Chao/sprites16_069.png", Size)
    Tapete3 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Chao/sprites16_084.png", Size)
    Tapete4 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Chao/sprites16_085.png", Size)

    #Sala da Escada
    Escada = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Acabamentos/sprites18_066.png", Size)
    
    Armario1 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/armario1.png", Size)
    Armario2 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/armario2.png", Size)

    Quadrolongo1 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/quadrolongo1.png", Size)
    Quadrolongo2 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/quadrolongo2.png", Size)

    Vaso4 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites9_070.png", Size)
    Vaso5 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites9_086.png", Size)

    #Segundo Andar
    EscadaD = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites8_019.png", Size)

    Porta1 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Chao/sprites6_0002.png", Size)
    Porta2 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Chao/sprites6_0003.png", Size)

    Janela3 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites8_034.png", Size)
    Janela4 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites8_050.png", Size)

    Estante5 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites19_133.png", Size)
    Estante6 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites19_134.png", Size)
    Estante7 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites19_149.png", Size)
    Estante8 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites19_150.png", Size)

    Cama1 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites19_160.png", Size)
    Cama2 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites19_161.png", Size)
    Cama3 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites19_176.png", Size)
    Cama4 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites19_177.png", Size)

    Cadeira = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites8_056.png", Size)

    Relogio3 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites8_014.png", Size)

    Telefone = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites8_011.png", Size)

    Pc = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites8_009.png", Size)

    Caveira1 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites9_033.png", Size)
    Caveira2 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites9_049.png", Size)

    Ursinho = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites20_227.png", Size)

    Roupa1 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites20_076.png", Size)
    Roupa2 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites20_077.png", Size)
    Roupa3 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites20_078.png", Size)

    Pintar = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites9_083.png", Size)

    Tapete5 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Chao/sprites16_020.png", Size)
    Tapete6 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Chao/sprites16_0004.png", Size)
    Tapete7 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Chao/sprites16_021.png", Size)
    Tapete8 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Chao/sprites16_0007.png", Size)
    Tapete9 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Chao/sprites16_0006.png", Size)
    Tapete10 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Chao/sprites16_0008.png", Size)
    Tapete11 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Chao/sprites16_036.png", Size)
    Tapete12 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Chao/sprites16_0005.png", Size)
    Tapete13 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Chao/sprites16_037.png", Size)

    Bau = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites21_00.png", Size)

    #Rua
    Teto1 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Paredes_Teto/sprites15_082.png", Size)
    Teto2 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Paredes_Teto/sprites15_098.png", Size)

    Piso = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Chao/sprites16_113.png", Size)

    Rua = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Chao/sprites16_083.png", Size)

    Tijolo = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Paredes_Teto/sprites15_050.png", Size)

    TetoPreto = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Acabamentos/sprites18_071.png", Size)
    TetoPreto2 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Acabamentos/sprites18_074.png", Size)
    TetoPreto3 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Acabamentos/sprites18_073.png", Size)

    Cerca = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites20_200.png", Size)
    Cerca2 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites20_201.png", Size)
    Cerca3 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites20_202.png", Size)
    Cerca4 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites20_203.png", Size)

    Cimento = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Paredes_Teto/sprites15_049.png", Size)

    TetoPreto4 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Teto/sprites38_056.png", Size)
    TetoPreto5 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Teto/sprites38_057.png", Size)
    TetoPreto6 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Teto/sprites38_058.png", Size)
    TetoPreto7 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Teto/sprites38_072.png", Size)
    TetoPreto8 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Teto/sprites38_073.png", Size)
    TetoPreto9 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Teto/sprites38_074.png", Size)
    TetoPreto10 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Teto/sprites38_088.png", Size)
    TetoPreto11 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Teto/sprites38_089.png", Size)
    TetoPreto12 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Teto/sprites38_090.png", Size)

    Arvore = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Arvore/sprites39_087.png", Size)
    Arvore1 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Arvore/sprites39_103.png", Size)
    Arvore2 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Arvore/sprites39_109.png", Size)
    Arvore3 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Arvore/sprites39_135.png", Size)
    Arvore4 = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Arvore/sprites39_151.png", Size)

    Livro = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Objetos/sprites20_132.png", Size)

    Saida = Load_Texture("C:/Users/thiag/Documents/GitHub/Ilusoes/graphics/Rua/sprites34_006.png", Size)


    Texture_Tags = {"1": Grass, "2": ParedeMad2, "3": ParedeMad3, "4": ParedeMad4, "5": Armario1, "6": Armario2, "7": Quadrolongo1, "8": Quadrolongo2, "9": ChaoMad, "10": ParedeMad1, "11": ParedeMad5, "12": Sofa1, "13": Sofa2, "14": Mesa1, "15": Mesa2, "16": Mesa3, "17": Lareira1, "18": Lareira2, "19": Janela1, "20": Janela2
    , "21": Prateleira1, "22": Estante1, "23": Estante2, "24": Mesa4, "25": Relogio1, "26": Relogio2, "27": Prateleira2, "28": Sofa3, "29": Sofa4, "30": Sofa5, "31": Sofa6, "32": Geladeira1, "33": Geladeira2, "34": Estante3, "35": Estante4, "36": Fogao, "37": Pia1, "38": Pia2, "39": Mesa5, "40": Banquinho,"41": Cenoura, "42": Prateleira3
    , "43": ChaoCoz, "44": Pia3, "45": Comida, "46": Piano1, "47": Piano2, "48": Piano3, "49": Piano4, "50": Piano5, "51": Piano6, "52": Lareira3, "53": Lareira4, "54": Lareira5, "55": Lareira6, "56": Lareira7, "57": Lareira8, "58": Espelho1, "59": Espelho2, "60": Vaso1, "61": Vaso2, "62": Vaso3,
    "63": Banquinho2, "64": Estatua1, "65": Estatua2, "66": Tapete1, "67": Tapete2, "68": Tapete3, "69": Tapete4, "70": Escada, "71": Vaso4, "72": Vaso5, "73": Porta1, "74": Porta2, "75": Janela3, "76": Janela4, "77": EscadaD, "78": Estante5, "79": Estante6, "80": Estante7, "81": Estante8,
    "82": Cama1, "83": Cama2, "84": Cadeira, "85": Relogio3, "86": Telefone, "87": Pc, "88": Caveira1, "89": Caveira2, "90": Ursinho, "91": Cama3, "92": Cama4, "93": Roupa1, "94": Roupa2, "95": Roupa3, "96": Pintar, "97": Tapete5, "98": Tapete6, "99": Tapete7, "100": Tapete8, "101": Tapete9, "102": Tapete10, "103": Tapete11, "104": Tapete12, "105": Tapete13
    , "106": Bau, "107": Teto1, "108": Teto2, "109": Piso, "110": Rua, "111": Tijolo, "112": TetoPreto, "113": TetoPreto2, "114": TetoPreto3, "115": Cerca, "116": Cerca2, "117": Cerca3,
    "118": Cerca4, "119": Cimento, "120": TetoPreto4, "121": TetoPreto5, "122": TetoPreto6, "123": TetoPreto7, "124": TetoPreto8, "125": TetoPreto9, "126": TetoPreto10,"127": TetoPreto11, "128": TetoPreto12,
    "129": Arvore, "130": Arvore1, "131": Arvore2, "132": Arvore3, "133": Arvore4, "134": Livro, "135": Saida}
