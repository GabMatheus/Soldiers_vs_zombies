#!/usr/bin/python
#-*- coding: utf-8 -*-
from code.Entity import Entity


class Level:
    def __init__(self ,window, name, game_mode):
        self.window = window
        self.entity_list: list[Entity] = []
        self.game_mode = game_mode #modo de jogo
        self.name = name

    def run(self, ):
        pass

