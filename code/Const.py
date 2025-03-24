#C
import pygame

#from code.Player import Player

C_GOLD = (212, 160, 28)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 0)
C_ORANGE = (217, 119, 6)
C_BLUE = (173, 216, 230)

#E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
    'Level1Bg0' : 0,
    'Level1Bg1' : 2,
    'Level1Bg2' : 1,
    'Level1Bg3' : 2,
    'Level1Bg4' : 1.5,
    'Level1Bg5' : 1.8,
    'Level2Bg0' : 0,
    'Level2Bg1' : 2,
    'Level2Bg2' : 1,
    'Level2Bg3' : 2,
    'Level2Bg4' : 1.5,
    'Level2Bg5' : 2,
    'Player1' : 2 ,
    'Player1Shot': 1,
    'Player2' : 2,
    'Player2Shot': 2,
    'Enemy1' : 1,
    'Enemy1Shot': 5,
    'Enemy2' : 1 ,
    'Enemy2Shot': 2,
    'Enemy3': 1.5,
    'Enemy3Shot': 3
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
    'Level2Bg5' : 999,
    'Player1'   : 300,
    'Player1Shot' : 1,
    'Player2'   : 300,
    'Player2Shot' : 1,
    'Enemy1'    : 50,
    'Enemy1Shot': 1,
    'Enemy2'    : 60,
    'Enemy2Shot' : 1,
    'Enemy3': 80,
    'Enemy3Shot': 2
}

ENTITY_SHOT_DELAY = {
    'Player1'   : 20,
    'Player2'   : 15,
    'Enemy1': 100,
    'Enemy2': 150,
    'Enemy3': 170
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
    'Level2Bg5': 0,
    'Player1': 1,
    'Player1Shot': 25,
    'Player2': 1,
    'Player2Shot': 20,
    'Enemy1': 1,
    'Enemy1Shot': 20,
    'Enemy2': 1,
    'Enemy2Shot': 15,
    'Enemy3': 1,
    'Enemy3Shot': 25
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
    'Level2Bg5': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 125,
    'Enemy2Shot': 0,
    'Enemy3': 150,
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
SPAW_TIME = 1200 #2500

#T
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 25000 #25s

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
