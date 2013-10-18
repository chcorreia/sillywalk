# coding=UTF-8

from pybot import *

# desenha o tabuleiro
mundo = Mundo(altura=8, largura=8)
Robot(2,1)

while True:
    andar(direita)
    andar(direita)
    andar(abaixo)
    andar(esquerda)
    andar(esquerda)
    andar(acima)