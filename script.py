import pygame
import random
import sys

pygame.init()

clock = pygame.time.Clock()

cells = 20
cell_size = 40

screen = pygame.display.set_mode((cells * cell_size, cells * cell_size))
pygame.display.set_caption("traffic-dodger")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
    
    clock.tick(60)
    pygame.display.update()

pygame.quit()