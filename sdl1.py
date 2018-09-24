import pygame, sys, os

from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((868, 600))
pygame.display.set_caption('monkey')
screen = pygame.display.get_surface()

# monkey_head_file = os.path.join("data", "chimp.bmp")
monkey_head_file = '/home/hdc/Downloads/MARBLES.BMP'

monkey_surface = pygame.image.load(monkey_head_file)

screen.blit(monkey_surface, (0, 0))
pygame.display.flip()

def input(events):
    for event in events:
        if event.type ==QUIT:
            sys.exit(0)
        else:
            print(event)

while True:
    input(pygame.event.get())