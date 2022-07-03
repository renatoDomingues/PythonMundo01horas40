#Faça um programa em Python que abra e reproduza o áudio de arquivo MP3.

'''
python -m pip install pygame
'''

import pygame
pygame.init()
pygame.mixer.music.load('desafio021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
