"""
021: Faça um programa em python que abra e reproduza o áudio de um arquivo MP3.
"""

import pygame

pygame.mixer.init()
pygame.mixer.music.load("")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    continue

"""
Correção:

import pygame 

pygame.init()
pygame.mixer.music.load("")
pygame.mixer.music.play()
pygame.event.wait()
"""