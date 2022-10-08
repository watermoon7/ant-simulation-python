import pygame, copy, random
from copy import deepcopy
pygame.init()

class Ant():
        
    def __init__(self, serial, pos, width, height, size):
        self.id = serial
        self.pos = [int(pos[0]), int(pos[1])]
        self.size = size
        self.w = width
        self.h = height
        self.holding = False
        self.base = [int((self.w/2)//self.size*self.size), int((self.h/2)//self.size*self.size)]
        self.trail = 0
        self.trailPositions = []
        self.trailColors = [
            (0, 90, 0),
            (0, 120, 0),
            (0, 150, 0),
            (0, 180, 0),
            (0, 210, 0),
            (0, 240, 0),
            (10, 255, 10),
            (65, 255, 65),
            (120, 255, 120),
            ]
       
    def drawAnt(self, screen):
        if not self.holding:
            antBody = pygame.draw.rect(screen, (0, 0, 0), (self.pos[0], self.pos[1], self.size, self.size))
        else:
            antWithFood = pygame.draw.rect(screen, (235, 0, 0), (self.pos[0], self.pos[1], self.size, self.size))
        for i in range(0, self.trail):
            a = pygame.draw.rect(screen, self.trailColors[int((self.trail-1)/3)-int(i/3)], (self.trailPositions[i][0], self.trailPositions[i][1], self.size, self.size))
    
    def executeTrail(self):
        self.trailPositions.append(deepcopy(self.pos))
        if len(self.trailPositions) > 27:
            self.trailPositions.pop(0)
        self.trail += (1 if self.trail < 27 else 0)
        
        
    def backToBase(self):
        c = random.randint(0, 1)

        #print(f'poses = {self.trailPositions}')
        if self.pos[0] <= self.base[0] and self.pos[1] <= self.base[1]:
            self.executeTrail()
            self.pos[0], self.pos[1] = self.pos[0] + self.size*c, self.pos[1] + self.size*(0 if c == 1 else 1)
        elif self.pos[0] >= self.base[0] and self.pos[1] <= self.base[1]:
            self.executeTrail()
            self.pos[0], self.pos[1] = self.pos[0] - self.size*c, self.pos[1] + self.size*(0 if c == 1 else 1)
        elif self.pos[0] <= self.base[0] and self.pos[1] >= self.base[1]:
            self.executeTrail()
            self.pos[0], self.pos[1] = self.pos[0] + self.size*c, self.pos[1] - self.size*(0 if c == 1 else 1)
        elif self.pos[0] >= self.base[0] and self.pos[1] >= self.base[1]:
            self.executeTrail()
            self.pos[0], self.pos[1] = self.pos[0] - self.size*c, self.pos[1] - self.size*(0 if c == 1 else 1)
        
        
    def move(self, allTrails):
        from random import randint as r
        
        vals = [
            [self.size, 0],
            [0, self.size],
            [-self.size, 0],
            [0, -self.size],
            [self.size, self.size],
            [self.size, -self.size],
            [-self.size, self.size],
            [-self.size, -self.size]
        ]

        def withinBounds(choice, pos, w, h):
            if (pos[0] + vals[choice][0]) > w or (pos[0] + vals[choice][0]) < 0:
                return False
            if (pos[1] + vals[choice][1]) > h or (pos[1] + vals[choice][1]) < 0:
                return False
            return True
        
        def foraging(self):    
            choice = r(0, 7)
            if withinBounds(choice, self.pos, self.w, self.h):
                self.pos[0] += int(vals[choice][0])
                self.pos[1] += int(vals[choice][1])
            else:
                running = True
                while running:
                    choice = r(0, 7)
                    if withinBounds(choice, self.pos, self.w, self.h):
                        self.pos[0] += int(vals[choice][0])
                        self.pos[1] += int(vals[choice][1])
                        running = False
            
        def followingTrail(i):
            pos = deepcopy(i[0])
            c = random.randint(0, 1)

            if self.pos[0] <= pos[0] and self.pos[1] <= pos[1]:
                self.pos[0], self.pos[1] = self.pos[0] + self.size*c, self.pos[1] + self.size*(0 if c == 1 else 1)
            elif self.pos[0] >= pos[0] and self.pos[1] <= pos[1]:
                self.pos[0], self.pos[1] = self.pos[0] - self.size*c, self.pos[1] + self.size*(0 if c == 1 else 1)
            elif self.pos[0] <= pos[0] and self.pos[1] >= pos[1]:
                self.pos[0], self.pos[1] = self.pos[0] + self.size*c, self.pos[1] - self.size*(0 if c == 1 else 1)
            elif self.pos[0] >= pos[0] and self.pos[1] >= pos[1]:
                self.pos[0], self.pos[1] = self.pos[0] - self.size*c, self.pos[1] - self.size*(0 if c == 1 else 1)
            
        y = False
        for i in allTrails:
            if self.pos in i:
                y = True
                tail = deepcopy(i)
        
        if y:
            followingTrail(tail)
        else:
            foraging(self)
        
        
    def execute(self, screen, allFoodPoses, allTrails, paused = False):
        #print(allFoodPoses, self.pos)
        if self.pos == self.base:
            self.holding = False
            self.trail = 0
            self.trailPositions = []
            
        e = [False]
        a = [x[1] for x in allFoodPoses]
    
        #if the ant is on food, and it doesn't currently have any food
        if self.pos in a and not self.holding:
            self.holding = True
            e = [True, a.index(self.pos)]
        else:
            pass
        
        self.drawAnt(screen)
               
        #if the game isn't paused,      
        if not paused:
            if not self.holding:
                self.move(allTrails)
            else:
                self.backToBase()
        
        return e
