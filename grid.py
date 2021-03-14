import pygame
import numpy as np
class Grid:
    def __init__(self, size: tuple, surface: pygame.Surface, p_size: int):
        self.resolution = tuple([i // p_size for i in size])
        grids = [np.empty(self.resolution)]*2
        self.p_grid = grids[0] #Primary
        self.p_grid.fill(0)
        self.s_grid = grids[1] #Secondary
        self.surface = surface
        self.p_size = p_size
        


    def draw_grid(self):
        for i in range(self.resolution[0]):
            for j in range(self.resolution[1]):
                color = (0,0,0)
                if self.p_grid[i][j] == 1:
                    color = (255, 255, 255)
                pygame.draw.rect(self.surface, color, tuple([i * self.p_size for i in [i, j, 1, 1]]))
    
    def set_pixel(self, g_pos:tuple, val:int):
        self.p_grid[g_pos] = val