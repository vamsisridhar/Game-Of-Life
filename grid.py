import pygame, sys
import numpy as np
class Grid:

    shapes = {
        "block" : [(0,0), (0,1), (1,0), (1,1)]
    }

    def __init__(self, size: tuple, surface: pygame.Surface, p_size: int):
        self.resolution = tuple([i // p_size for i in size])
        self.p_grid = np.zeros(self.resolution) #Primary
        self.s_grid = np.zeros(self.resolution)#Secondary
        self.surface = surface
        self.p_size = p_size


    def draw_grid(self):
        for i in range(self.resolution[0]):
            for j in range(self.resolution[1]):
                color = (0,0,0)
                if self.p_grid[j][i] == 1:
                    color = (255, 255, 255)
                pygame.draw.rect(self.surface, color, tuple([i * self.p_size for i in [i, j, 1, 1]]))
    
    def set_pixel(self, x, y, val:int):
        self.p_grid[y, x] = val

    def draw_object(self, name, x, y):
        for pt in self.shapes[name]:
            if pt[0] + x < self.resolution[0] and pt[1] + y < self.resolution[1]:
                self.set_pixel(pt[0] + x, pt[1] + y, 1)
                
                

    def update(self):
        for i in range(self.resolution[0]):
            for j in range(self.resolution[1]):
                n_count = 0
                
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):

                        if x > 0 and y > 0 and x < self.resolution[0] and y < self.resolution[1]:
                            
                            if (x, y) != (i,j):
                                if self.p_grid[y][x]:
                                    n_count += 1

                if self.p_grid[j][i] == 0:
                    if n_count == 3:
                        self.s_grid[j][i] = 1
                    else:
                        self.s_grid[j][i] = 0

                elif self.p_grid[j][i] == 1:
                    
                    if n_count < 2 or n_count > 3:
                        self.s_grid[j][i] = 0
                    else:
                        self.s_grid[j][i] = 1
        
        self.p_grid = np.copy(self.s_grid)
        self.s_grid.fill(0)
        