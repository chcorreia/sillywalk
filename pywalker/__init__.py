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
_IMAGES_DIR = os.path.join(_MAIN_DIR, "images")
_FIXED_FONT = os.path.join(_FONTS_DIR, "DejaVuSansMono.ttf")

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
		
        elif event.type == pygame.MOUSEBUTTONUP:
			pronto = True
			
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

    def __init__(self, largura=8, altura=8, lado=48):
        """ Inicializa o Mundo """

        # transfere parâmetros para os atributos
        self.tam_x = largura
        self.tam_y = altura
        self.lado = lado

        # define o tamanho das margens
        self.margem_x = 4
        self.margem_y = 4
        self.margem_msgbox = 32

        # prepara o tabuleiro
        self.calcula_tamanhos(self.tam_x, self.tam_y)
        self.desenha_tabuleiro()

    def calcula_tamanhos(self, tam_x, tam_y):
        """ calcula o tamanho em pixels do mundo """

        # calcula os tamanhos em pixels do tabuleiro
        self.pixels_x = self.tam_x * self.lado
        self.pixels_y = self.tam_y * self.lado

        # calcula os rects externo e interno
        self.rect_tudo = self.get_rect_tudo()
        self.rect_dentro = self.get_rect_dentro()
        self.rect_msgbox = self.get_rect_msgbox()

    def get_rect_tudo(self):
        """ retorna um Rect com os limites da tela """
        largura = self.margem_x + self.pixels_x + self.margem_x # eu sei que é redundante
        altura = self.margem_y + self.pixels_y + self.margem_y + self.margem_msgbox + self.margem_y
        return pygame.Rect(0,0, largura, altura)

    def get_rect_dentro(self):
        """ retorna um Rect com os limites do tabuleiro dentro da tela """
        return pygame.Rect(self.margem_x, self.margem_y, self.pixels_x-1, self.pixels_y-1)

    def get_rect_msgbox(self):
        """ retorna o Rect com os limites da caixa de mensagens abaixo do tabuleiro """
        altura = self.margem_y + self.pixels_y + self.margem_y
        return pygame.Rect(self.margem_x, altura, self.pixels_x, self.margem_msgbox)

    def desenha_tabuleiro(self):
        """ desenha o tabuleiro usando os parâmetros """

        # cria as screens (telas de atualização)
        self.screen_tudo = pygame.display.set_mode(self.rect_tudo.size, 0, 32)
        self.screen_tudo.convert_alpha()
        pygame.init()

        # define as cores
        self.cor_linha = pygame.color.Color("DarkSlateGray")
        self.cor_borda = pygame.color.Color("WhiteSmoke")
        self.cor_casas = (pygame.color.Color("Khaki1"), pygame.color.Color("Khaki3"))
        self.cor_msgbox = pygame.color.Color("LightGoldenrod1")

        # pinta o fundo
        self.screen_tudo.fill(self.cor_borda)

        # caixa de mensagens (provavelmente merece estar em um método)
        pygame.draw.rect(self.screen_tudo, self.cor_msgbox, self.rect_msgbox, 0)
        pygame.draw.rect(self.screen_tudo, self.cor_linha, self.rect_msgbox, 1)

        # desenha o grid
        self.desenha_grid()

        # atualiza a tela
        pygame.display.flip()

    def desenha_grid(self):
        """ desenha as casas do tabuleiro e retorna a tela criada """

        # cria uma subsurface focada na área do grid
        self.screen_dentro = self.screen_tudo.subsurface(self.rect_dentro)

        # pinta as casas
        pos_x = 0
        cor = 0
        for x in range(self.tam_x): # em cada coluna

            pos_y = 0
            for y in range(self.tam_y): # em cada linha

                # calcula o rect da casa
                box = pygame.Rect(pos_x, pos_y, self.lado, self.lado)

                # pinta a casa
                pygame.draw.rect(self.screen_dentro, self.cor_casas[cor%2], box)

                # incrementa Y
                pos_y += self.lado
                cor += 1

            # incrementa X
            pos_x += self.lado
            cor += 1

        # risca o grid horizontal
        for x in range(1,self.tam_x):
            pygame.draw.line(self.screen_dentro, self.cor_linha, (x*self.lado, 0), (x*self.lado, self.pixels_y))

        # risca o grid vertical
        for y in range(1,self.tam_y):
            pygame.draw.line(self.screen_dentro, self.cor_linha, (0, y*self.lado), (self.pixels_x, y*self.lado))

        pygame.draw.rect(self.screen_dentro, self.cor_linha, (0,0,self.pixels_x-1,self.pixels_y-1), 1)

        # salva a imagem original do grid para simplificar as atualizações
        self.screen_grid = self.screen_dentro.copy()

    def mensagem(self):
        pass
		

#-------------------------------------------------------------------------------
# FINALIZAÇÃO
#-------------------------------------------------------------------------------		
@atexit.register
def sair():
	espera()
	pygame.quit()

#-------------------------------------------------------------------------------
# INICIALIZAÇÃO
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
# MAIN
#-------------------------------------------------------------------------------
def _main():
    Mundo()

if __name__ == '__main__':
    _main()
