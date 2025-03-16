#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()  # Inicializa o Pygame
        self.window = pygame.display.set_mode((600, 480))

    def run(self):
        # Loop principal
        while True:
            menu = Menu(self.window)
            menu.run()
            pass
            # for event in pygame.event.get():
            #    if event.type == pygame.QUIT:
            #        running = False
            #        pygame.quit()

            #pygame.display.update()  # Atualiza a tela

        # quit()

if __name__ == "__main__":
    game = Game()
    game.run()
