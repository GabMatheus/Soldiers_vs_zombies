import pygame
#from code.Player import Player

#C
C_GOLD = (212, 160, 28)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 0)
C_ORANGE = (217, 119, 6)
C_BLUE = (173, 216, 230)
C_RED = (255, 20, 30)

#E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
    'Level1Bg0' : 2,
    'Level1Bg1' : 0.6,
    'Level1Bg2' : 1.1,
    'Level1Bg3' : 1.6,
    'Level1Bg4' : 1.9,
    'Level1Bg5' : 2.1,
    'Level2Bg0' : 0,
    'Level2Bg1' : 0.7,
    'Level2Bg2' : 0.9,
    'Level2Bg3' : 1.1,
    'Level2Bg4' : 1.3,
    'Player1' : 2 ,
    'Player1Shot': 1,
    'Player2' : 2,
    'Player2Shot': 2,
    'Enemy1' : 1,
    'Enemy1Shot': 5,
    'Enemy2' : 1.5 ,
    'Enemy2Shot': 3,
    'Enemy3': 1,
    'Enemy3Shot': 2
}

ENTITY_HEALTH = {
    'Level1Bg0' : 999,
    'Level1Bg1' : 999,
    'Level1Bg2' : 999,
    'Level1Bg3' : 999,
    'Level1Bg4' : 999,
    'Level1Bg5' : 999,
    'Level2Bg0' : 999,
    'Level2Bg1' : 999,
    'Level2Bg2' : 999,
    'Level2Bg3' : 999,
    'Level2Bg4' : 999,
    'Player1'   : 300,
    'Player1Shot' : 1,
    'Player2'   : 300,
    'Player2Shot' : 1,
    'Enemy1'    : 70,
    'Enemy1Shot': 1,
    'Enemy2'    : 85,
    'Enemy2Shot' : 1,
    'Enemy3': 75,
    'Enemy3Shot': 2
}

ENTITY_SHOT_DELAY = {
    'Player1'   : 18,
    'Player2'   : 14,
    'Enemy1': 80,
    'Enemy2': 150,
    'Enemy3': 120
}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Player1': 1,
    'Player1Shot': 25,
    'Player2': 1,
    'Player2Shot': 20,
    'Enemy1': 1,
    'Enemy1Shot': 15,
    'Enemy2': 1,
    'Enemy2Shot': 25,
    'Enemy3': 1,
    'Enemy3Shot': 20
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 155,
    'Enemy2Shot': 0,
    'Enemy3': 130,
    'Enemy3Shot': 0
}

#M
MENU_OPTION = ('New Game 1P',
               'New Game 2P - Cooperative',
               'New Game 2P - Competitive',
               'Score',
               'Exit')

#P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = { 'Player1': pygame.K_DOWN,
                    'Player2': pygame.K_s}
PLAYER_KEY_LEFT = { 'Player1': pygame.K_LEFT,
                    'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_SHOT = { 'Player1': pygame.K_RCTRL,
                    'Player2': pygame.K_LCTRL}

#S
SPAW_TIME = 1200

#T
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 25000 #25s

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

#S-2
SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Name': (WIN_WIDTH / 2, 110),
             0: (WIN_WIDTH / 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190),
             5: (WIN_WIDTH / 2, 210),
             6: (WIN_WIDTH / 2, 230),
             7: (WIN_WIDTH / 2, 250),
             8: (WIN_WIDTH / 2, 270),
             9: (WIN_WIDTH / 2, 290)
        }