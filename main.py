import sys,time
import pygame
import numpy as np
from grid import *
pygame.init()


class Start:
    def __init__(self, size):
        self.surface = pygame.Surface(size)
        self.start_b_pos = [(250,250), (500,100)]  
        self.draw_button(self.start_b_pos[0], self.start_b_pos[1], 'Start Grid', 48, (410, 280))
        self.create_b_pos = [(250,500), (500,100)] 
        self.draw_button(self.create_b_pos[0],self.create_b_pos[1], 'Create', 48,(430, 530))
        self.bounds_array={"start":self.start_b_pos,"create":self.create_b_pos}
        
        
        

    def draw_button(self, pos, size,  text, font_size, t_pos, pad =10):
        font = pygame.font.SysFont('chalkduster.ttf', font_size)
        pygame.draw.rect(self.surface, (255,255,255), (pos[0], pos[1], size[0], size[1]))
        pygame.draw.rect(self.surface, (0,0,0), (pos[0]+pad, pos[1]+pad, size[0]-(2*pad), size[1]-(2*pad)))
        self.surface.blit(font.render(text, True, (255,255,255)), t_pos)

    def check_bounds(self, pos):
        for item in self.bounds_array:
            bounds = self.bounds_array[item]
            if pos[0] > bounds[0][0] and pos[0] < bounds[0][0] + bounds[1][0]:
                if pos[1] > bounds[0][1] and pos[1] < bounds[0][1] + bounds[1][1]:
                    return item



size = w_WIDTH, w_HEIGHT = 1000, 1000
screen = pygame.display.set_mode(size)

p_size = 5

m_grid = Grid(size, p_size)
start = Start(size)
mouse_b = 0
anim =False
fps = 60

s_active = True
g_active = False

def ON_START():
    m_grid.draw_object("glider", 10, 10)
    m_grid.draw_object("pulsar",35, 35)
    m_grid.draw_object("pentadecathlon",80, 70)
    m_grid.draw_object("pulsar",60, 60)
    m_grid.draw_object("pulsar",120, 23)


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
            if event.key == pygame.K_SPACE and g_active:
                anim = not anim
            if event.key == pygame.K_BACKSPACE and g_active:
                anim = False
                m_grid.p_grid.fill(0)
                g_active = False
                s_active = True
    if mouse_b != 0:
        m_pos = pygame.mouse.get_pos()
        if g_active:
            g_pos = tuple([i // p_size for i in m_pos])
            print(g_pos)
            m_grid.set_pixel(g_pos[0], g_pos[1], mouse_b - 1)
        if s_active:
            clicked = start.check_bounds(m_pos)
            if clicked == "start":
                ON_START()
                s_active = False
                g_active = True
    if anim:
        fps = 200
        m_grid.update()

    m_grid.draw_grid()

    if g_active:
        screen.blit(m_grid.surface, (0,0))
    elif s_active:
        screen.blit(start.surface, (0,0))
    pygame.display.flip()
    

