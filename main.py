import sys,time
import pygame
import numpy as np
from grid import *
pygame.init()



size = w_WIDTH, w_HEIGHT = 1000, 1000
screen = pygame.display.set_mode(size)
p_size = 5

m_grid = Grid(size, screen, p_size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_pos = pygame.mouse.get_pos()
            m_grid.set_pixel(tuple([i // p_size for i in m_pos]), 1)
    
    m_grid.draw_grid()

    pygame.display.flip()
    

