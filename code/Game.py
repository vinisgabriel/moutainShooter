#!/usr/bin/python
# -*- coding: utf-8 -*-

from class2 import Class2
#from class4 import class4
import pygame

from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # checar por todos eventos
            #for evento in pygame.event.get():
            #    if evento.type == pygame.QUIT:
            #        pygame.quit()  # fechar janela
            #        quit()  # encerrar pygame
#        pass