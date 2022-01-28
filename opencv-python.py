import cv2
import numpy as np

#IMEREAD retorna os dados da imagem, ou seja os pixes para um NUMPY array
#essa função tem dois parametros, o diretorio da imagem e o modo de como vc quer carregar a imagem,
#  colorido, preto e branco.
img = cv2.imread('pessoa4.8.jpg', 1)

#exibe a janela, o parametro é o nome da janela.
cv2.namedWindow('hello word')
#primeiro parametro é o nome da janela e o segundo é o array onde esta carregado os pixes da imagem
cv2.imshow('hello word', img)
#deixa a janela em aberto para exibir a imagem.
cv2.waitKey()

print('teste git')
