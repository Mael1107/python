# Desafio 021 em CursoemVideo
import pygame
pygame.init()

pygame.mixer.music.load("ju_arrotando.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)



