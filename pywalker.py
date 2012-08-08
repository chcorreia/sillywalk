# coding=UTF-8
#-------------------------------------------------------------------------------
# Name:        silly walk
# Purpose:
#
# Author:      Carlos H Correia
#
# Created:     07/08/2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
""" biblioteca para ensino de programação

    Para utilizar crie o Mundo(largura, altura) e em seguida crie instâncias de Objeto()
    O primeiro objeto criado irá obedecer ao comando andar()
    Os objetos subsequentes podem ser comandados via objeto.andar()
"""

import atexit
import pygame
import sys

#-------------------------------------------------------------------------------
# VARIÁVEIS E CONSTANTES
#-------------------------------------------------------------------------------
_ENCERRADO = False # evitar realizar certas rotinas após o término

#-------------------------------------------------------------------------------
# ROTINAS
#-------------------------------------------------------------------------------
def espera():
    """ aguarda pressionar uma tecla"""
    global _ENCERRADO

    pronto = False
    tick_old = pygame.time.get_ticks()
    print "espera"
    while not (pronto or _ENCERRADO):

        event = pygame.event.wait()

        if event.type == pygame.QUIT:
            print "quit"
            _ENCERRADO = True
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print "ESC"
                _ENCERRADO = True
            else:
                print"key"
                pronto = True


#-------------------------------------------------------------------------------
# CLASSES
#-------------------------------------------------------------------------------

class Mundo():
    """ Classe que contém o tabuleiro e o mostra na tela """

    def __init__(self, largura=8, altura=8, lado=64):
        """ Inicializa o Mundo """

        # transfere parâmetros para os atributos
        self._tam_x = largura
        self._tam_y = altura
        self._lado = lado

        # calcula os tamanhos em pixels do mundo
        self._pixels_x = self._tam_x * self._lado
        self._pixels_y = self._tam_y * self._lado

        # calcula os rects
        self._rect_tudo = pygame.Rect(0,0,self._pixels_x, self._pixels_x)

        # cria as screens (telas de atualização)
        self._screen_tudo = pygame.display.set_mode(self._rect_tudo.size, 0, 32)
        self._screen_tudo.convert_alpha()
        pygame.init()

        # desenha a moldura
        self._cor_borda = (255,0,0)
        pygame.draw.rect(self._screen_tudo, self._cor_borda, self._rect_tudo, 0)

        # atualiza a tela
        pygame.display.flip()






#-------------------------------------------------------------------------------
# INICIALIZAÇÃO
#-------------------------------------------------------------------------------
atexit.register(espera)

#-------------------------------------------------------------------------------
# MAIN
#-------------------------------------------------------------------------------
def _main():
    pass
    Mundo()
    espera()
    print "done."

if __name__ == '__main__':
    _main()
