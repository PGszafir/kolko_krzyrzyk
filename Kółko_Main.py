import funkcja
#import pygame
import sys
import random
from pygame.locals import *
print('kolko-krzyzyk')

pl0 = [' ' for i in range(9)]
pl1 = [' ' for i in range(9)]

print('wersja z komp')

funkcja.pierwszy_etap(pl1)
#'''
pygame.init()
OKNOGRY = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption('Kółko i krzyżyk')


RUCH = 1
WYGRANY = 0  # wynik gry: 0 - nikt, 1 - gracz, 2 - komputer, 3 - remis
WYGRANA = False
#'''
