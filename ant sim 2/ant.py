from random import randint as r
from time import sleep as s
from variables import *

vals = [
    [size, 0],
    [0, size],
    [-size, 0],
    [0, -size],
    [size, size],
    [size, -size],
    [-size, size],
    [-size, -size]
    ]

home = [int(len(grid[0])/2), int(len(grid)/2)]

class Ant():
    
    def __init__(self, antId, pos):
        self.id = antId
        self.pos = pos
        
        self.holding = False
        self.tail = []
    
    def forage(self):
        choice = r(0, 7)
        self.pos[0] += int(vals[choice][0])
        self.pos[1] += int(vals[choice][1])
        if self.pos[0] > w or self.pos[0] < 0 or self.pos[1] > h or self.pos[1] < 0: return True
        return False
        
    def retreat(self, grid):
        c = r(0, 1)
        self.tail.append(self.pos)
        if self.pos[0] <= w/2 and self.pos[1] <= h/2:
            self.pos[0], self.pos[1] = self.pos[0] + size*c, self.pos[1] + size*(0 if c == 1 else 1)
        elif self.pos[0] < w/2 and self.pos[1] > h/2:
            self.pos[0], self.pos[1] = self.pos[0] + size*c, self.pos[1] - size*(0 if c == 1 else 1)
        elif self.pos[0] >= w/2 and self.pos[1] <= h/2:
            self.pos[0], self.pos[1] = self.pos[0] - size*c, self.pos[1] + size*(0 if c == 1 else 1)
        elif self.pos[0] > w/2 and self.pos[1] > h/2:
            self.pos[0], self.pos[1] = self.pos[0] - size*c, self.pos[1] - size*(0 if c == 1 else 1)
        if self.pos == home: self.holding = False
        
    def move(self, grid):
        if self.holding:
            self.retreat(grid)
            if len(self.tail) == 20:
                self.tail.pop(0)
            for i in range(0, len(self.tail)):
                grid[self.tail[i][0]][self.tail[i][1]] = grid[self.tail[i][0]][self.tail[i][1]]-(1 if grid[self.tail[i][0]][self.tail[i][1]] != 0 else 0)
        else:
            a = self.forage()
            while a: a = self.forage()
            if grid[int(self.pos[0]/size)][int(self.pos[1]/size)] == -1:
                self.holding = True

ant1 = Ant('ant1', [900, 660])
ant1.holding = True

grid[home[0]][home[1]] = 'A'
            

for i in range(1, 40):
    grid[int(ant1.pos[0]/size)-1][int(ant1.pos[1]/size)-1] = ['-']
    ant1.move(grid)
    grid[int(ant1.pos[0]/size)-1][int(ant1.pos[1]/size)-1] = ['A']
    '''for i in grid:
        print(i)
    print(ant1.pos)'''
    #s(0.3)
    

    