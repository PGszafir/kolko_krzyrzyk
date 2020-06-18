import funkcje
import pygame
import sys
import random
from pygame.locals import *
#'''
print('kolko-krzyzyk \nPoczątek Gry')

pl0 = [' ' for i in range(9)]
pl1 = [' ' for i in range(9)]

a=funkcje.pierwszy_etap(pl1)
#print(a[0].rys_plansza())
if a==0:
    print("KONIEC")
else:
    funkcje.drugi_etap(*a)
#'''



'''
pygame.init()
OKNOGRY = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption('Kółko i krzyżyk')


RUCH = 1
WYGRANY = 0  # wynik gry: 0 - nikt, 1 - gracz, 2 - komputer, 3 - remis
WYGRANA = False
'''
