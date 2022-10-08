import pygame, gc
pygame.init()

def message(screen, text, centerx, centery, size = 30, colour = (0, 0, 0)):
    font = 'optima'
    myfont = pygame.font.SysFont(font, size)

    ts = myfont.render(text, True, colour)
    tsR = ts.get_rect(center=(centerx, centery))
    screen.blit(ts, tsR)

def loadimage(screen, img, x, y, transform = 0):
    white = (255, 255, 255)
    image = pygame.image.load(img)
    if transform != 0:
        image = pygame.transform.scale(image, (transform[0], transform[1]))
    image_rect = image.get_rect()
    image_rect.center = (x, y)
    screen.blit(image, image_rect)
   
def varGrid():
    with open('variables.py', 'r') as f:
        return eval(f.readline())
        
def editGrid(grid):
    with open('variables.py', 'w') as f:
        f.write(str(grid))


'''
variables = addVariables(30, 'apple', 11)
for i in variables:
    print(globals()[i])
'''

