#!/usr/bin/python
#-*- coding: utf-8 -*-
import random
import sys
from random import choice

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAW_TIME, C_ORANGE, C_BLUE, EVENT_TIMEOUT, \
    TIMEOUT_STEP, TIMEOUT_LEVEL
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self ,window: Surface, name: str, game_mode: str , player_score: list[int]):
        self.window = window
        self.timeout = TIMEOUT_LEVEL
        self.entity_list: list[Entity] = []
        self.game_mode = game_mode
        self.name = name
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        player = (EntityFactory.get_entity('Player1'))
        player.score = player_score[0]
        self.entity_list.append(player)
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            player = (EntityFactory.get_entity('Player2'))
            player.score = player_score[1]
            self.entity_list.append(player)
        pygame.time.set_timer(EVENT_ENEMY, SPAW_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)


    def run(self , player_score: list[int]):
        pygame.mixer_music.load(f'./asset/{self.name}.wav')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf , dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name == 'Player1':
                    self.level_text(16, f'Player1 - Health: {ent.health} | Score: {ent.score}', C_ORANGE, (10, 18))
                if ent.name == 'Player2':
                    self.level_text(16, f'Player2 - Health: {ent.health} | Score: {ent.score}', C_BLUE, (10, 31))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice  = random.choice(('Enemy1','Enemy2','Enemy3'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'Player2':
                                player_score[1] = ent.score
                        return  True

                found_player = any(isinstance(e, Player) for e in self.entity_list)

                if not found_player:
                    return False

            # printed text
            self.level_text(15, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', C_WHITE, (10, 5))
            self.level_text(15, f'fps: {clock.get_fps():.0f}', C_WHITE, (10, WIN_HEIGHT - 25))
            self.level_text(15, f'entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 12))
            pygame.display.flip()
            #collisions
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)


    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)


