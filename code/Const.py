#C
import pygame

#from code.Player import Player

COLOR_GOLD = (212, 160, 28)
COLOR_WHITE = (255,255,255)
COLOR_YELLOW = (255,255,0)

#E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'Level1Bg0' : 0,
    'Level1Bg1' : 1.5,
    'Level1Bg2' : 1.8,
    'Level1Bg3' : 1.5,
    'Level1Bg4' : 2.5,
    'Player1' : 2 ,
    'Player2' : 2,
    'Enemy1' : 2,
    'Enemy2' : 1
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
SPAW_TIME = 2200

# W
WIN_WIDTH = 480
WIN_HEIGHT = 270
