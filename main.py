import pygame
import numpy as np

from pygame.locals import *

QTT = 50
MAX_HEIGHT = 450

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Lista 2')

#Gera as alturas aleatórias
retangules_heights = np.random.randint(0, MAX_HEIGHT, QTT)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    
    pos = 10
    for height in retangules_heights:
        pos = pos + 10 
        retangule_pos = (pos, 600 - height)
        
        retangule = pygame.Surface((2, height))
        retangule.fill((255, 255, 255))

        screen.blit(retangule, retangule_pos)    

    pygame.display.update()