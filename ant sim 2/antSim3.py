import pygame
from ant import *
from variables import *

def main():
    
    screen = pygame.display.set_mode((w, h))
    
    def drawGrid():
        for i in grid:
            for o in range(0, len(grid[0])):
                if grid[i][o] == 0:
                    a = pygame.draw.rect(screen, (white), (i*size, o*size, size, size))
                elif grid[i][o] == -1:
                    a = pygame.draw.rect(screen, (green3), (i*size, o*size, size, size))
                elif grid[i][o] > 0:
                    a = pygame.draw.rect(screen, (black), (i*size, o*size, size, size))
                
    def addFood(num, sizeBox, pos):
        pos = [int(pos[0]/size),int(pos[1]/size)]
        for i in range(0, sizeBox):
            for o in range(0, sizeBox):
                grid[i][o] = -1
    
    def addAnts(num):
        for i in range(1, num+1):
            globals()[f'ant{i}'] = Ant(f'ant{i}', home)
    
    def removeAnts():
        pass
    
    def removeFood():
        pass
    
    
    
    running = 1
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = 0
                
            

if __name__ == '__main__':
    main()