# Make a Python program that opens and plays audio from an MP3 file.

import pygame
from time import sleep

pygame.init()

pygame.mixer.music.load('assets/morada.mp3')
pygame.mixer.music.play()

sleep(250)

pygame.event.wait()
