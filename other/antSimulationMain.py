import pygame
import random
from pickle import TRUE
from functions import loadimage, message

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

w = 1080
h = 720

numsW = [random.randint(0, w) for x in range(0, 100)]
numsH = [random.randint(0, h) for x in range(0, 100)]

screen = pygame.display.set_mode((w, h), pygame.RESIZABLE)

rectangle = pygame.rect.Rect((w/2, h/2, w/12, w/12))
rectangle_draging = False

running = 1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
        elif event.type == pygame.VIDEORESIZE:
            surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            rectangle.width, rectangle.height = event.w/12, event.w/12
            w, h = event.w, event.h
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:            
                if rectangle.collidepoint(event.pos):
                    rectangle_draging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = rectangle.x - mouse_x
                    offset_y = rectangle.y - mouse_y

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:            
                rectangle_draging = False

        elif event.type == pygame.MOUSEMOTION:
            if rectangle_draging:
                mouse_x, mouse_y = event.pos
                rectangle.x = mouse_x + offset_x
                rectangle.y = mouse_y + offset_y
                
    screen.fill(white)
    box = pygame.draw.rect(screen, black, rectangle)
    for i in range(0, 100):
        loadimage(screen, 'ant2.png', numsW[i], numsH[i])

    pygame.display.update()

    
    
    
    
    
    
    
    
    
    
    