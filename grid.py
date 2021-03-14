import pygame, sys
import numpy as np
class Grid:

    shapes = {
        "block" : [(0,0), (0,1), (1,0), (1,1)],
        "beehive": [(0,1), (1,0), (2,0), (3,1), (1,2), (2,2)],
        "loaf": [(0,1),(1,0),(1,2),(2,0),(2,3),(3,1),(3,2)],
        "boat": [(0,0),(0,1),(1,0),(1,2),(2,1)],
        "blinker": [(0,0),(0,1),(0,2)],
        "toad": [(1,0),(2,0),(3,0),(0,1),(1,1),(2,1)],
        "beacon": [(0,0),(0,1),(1,0),(1,1),(2,2),(2,3),(3,2),(3,3)],
        "pulsar": [(0,2),(0,3),(0,4),(0,8),(0,9),(0,10),
                    (2,0),(2,5),(2,7),(2,12),
                    (3,0),(3,5),(3,7),(3,12),
                    (4,0),(4,5),(4,7),(4,12),
                    (5,2),(5,3),(5,4),(5,8),(5,9),(5,10),
                    (7,2),(7,3),(7,4),(7,8),(7,9),(7,10),
                    (8,0),(8,5),(8,7),(8,12),
                    (9,0),(9,5),(9,7),(9,12),
                    (10,0),(10,5),(10,7),(10,12),
                    (12,2),(12,3),(12,4),(12,8),(12,9),(12,10)],
        "pentadecathlon": [(0,1),(1,1),(2,0),(2,2),(3,1),(4,1),(5,1),(6,1),(7,0),(7,2),(8,1),(9,1)],
        "glider": [(0,1),(1,2),(2,0),(2,1),(2,2)]
        
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
        