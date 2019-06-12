#!coding: utf-8
from __future__ import print_function, division

import pygame
pygame.init()

taille = [820, 820]
ecran = pygame.display.set_mode(taille)
a = 100
sens = 1

NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]
ORANGE = [255, 128, 0]
ROSE = [255, 128, 192]

# DÉBUT

clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK
    
    
    # DESSIN
    ecran.fill(ORANGE)
    
    k = 10
    m = 10
    
    for i in range(5):

        pygame.draw.rect(ecran, NOIR, [k,m, 80,80])
        k = k + 80
    
        pygame.draw.rect(ecran, BLANC, [k,m, 80,80])
        k = k + 80
        
    for i in range(5):
        
        pygame.draw.rect(ecran, NOIR, [k,m, 80,80])
        k = k + 80
        
        pygame.draw.rect(ecran, BLANC, [k,m, 80,80])
        k = k + 80
        m = m + 80
            
            
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()