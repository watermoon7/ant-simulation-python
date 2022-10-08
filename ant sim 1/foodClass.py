from antMovement import Ant
import pygame
pygame.init()

class Food():

    def __init__(self, pos, idnum):
        self.idnum = idnum
        self.pos = pos
        self.color = (0, 147, 0)
    
    def drawFood(self, screen, size):
        food = pygame.draw.rect(screen, self.color, (self.pos[0], self.pos[1], size, size))
'''
a = [2, 3, 4]
a1 = [2, 6, 7]
a2 = []
a3 = ['e']
b = 2
c = []

c.append(a)
c.append(a1)
print(c)
for i in c:
    print(i)
    if b in i:
        print(True)'''