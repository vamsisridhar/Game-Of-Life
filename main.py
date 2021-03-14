import sys,time
import pygame
import numpy as np
from grid import *
pygame.init()



size = w_WIDTH, w_HEIGHT = 1000, 1000
screen = pygame.display.set_mode(size)
p_size = 5

m_grid = Grid(size, screen, p_size)
mouse_b = 0
anim =False
fps = 60

m_grid.draw_object("block",35, 35)


while True:
    time.sleep(1/fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if anim == False:
            fps = 60
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    mouse_b = 2
                elif pygame.mouse.get_pressed()[2]:
                    mouse_b = 1
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_b = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                anim = not anim
    if mouse_b != 0:
        m_pos = pygame.mouse.get_pos()
        g_pos = tuple([i // p_size for i in m_pos])
        print(g_pos)
        m_grid.set_pixel(g_pos[0], g_pos[1], mouse_b - 1)

    if anim:
        fps = 2
        m_grid.update()

    m_grid.draw_grid()

    pygame.display.flip()
    

