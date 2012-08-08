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

import sys, os.path, atexit, pygame

#-------------------------------------------------------------------------------
# VARIÁVEIS E CONSTANTES
#-------------------------------------------------------------------------------
_ENCERRADO = False # evitar realizar certas rotinas após o término
_MAIN_DIR = os.path.abspath(os.path.dirname(sys.argv[0]) if __name__ == '__main__' else os.path.dirname(__file__))
_FONTS_DIR = os.path.join(_MAIN_DIR, "fonts")
print _MAIN_DIR

#-------------------------------------------------------------------------------
# ROTINAS
#-------------------------------------------------------------------------------
def espera():
    """ aguarda pressionar uma tecla"""
    global _ENCERRADO

    pronto = False
    tick_old = pygame.time.get_ticks()

    while not (pronto or _ENCERRADO):

        event = pygame.event.wait() # espera um evento

        if event.type == pygame.QUIT: # se fechou a janela sai e evita esperar de novo
            _ENCERRADO = True
            sys.exit()
        elif event.type == pygame.KEYDOWN: # tecla pressionada

            if event.key == pygame.K_ESCAPE: # ESC = encerra (mesmo no meio)
                _ENCERRADO = True
            else:
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
        self._margem_x = 8
        self._margem_y = 8

        # calcula os tamanhos em pixels do mundo
        self._pixels_x = self._tam_x * self._lado
        self._pixels_y = self._tam_y * self._lado

        # calcula os rects
        self._rect_tudo = self._get_rect_tudo()

        # cria as screens (telas de atualização)
        self._screen_tudo = pygame.display.set_mode(self._rect_tudo.size, 0, 32)
        self._screen_tudo.convert_alpha()
        pygame.init()

        # desenha a moldura
        self._cor_borda = (255,0,0)
        pygame.draw.rect(self._screen_tudo, self._cor_borda, self._rect_tudo, 0)

        # atualiza a tela
        pygame.display.flip()

    def _get_rect_tudo(self):
        largura = self._pixels_x + self._margem_x * 2
        altura = self._pixels_y + self._margem_y * 2
        return pygame.Rect(0,0, largura, altura)






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

if __name__ == '__main__':
    _main()
