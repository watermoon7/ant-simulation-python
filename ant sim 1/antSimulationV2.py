def main():
    import pygame, random, copy, gc
    from antMovement import Ant
    from foodClass import Food
    from functions import loadimage, message
    
    pygame.init()
    clock = pygame.time.Clock()
    
    def listInstances(class1):
        d = []
        for obj in gc.get_objects():
            if isinstance(obj, class1):
                d.append(obj)
        print(d)
        print(f'length of d {len(d)}')
            
    
    allFoodPoses = []
    def summonFood(pos, clicked, sizeBox = 5):
        for i in range(1, sizeBox+1):
            for o in range(1, sizeBox+1):
                globals()[f'food{((i-1)*sizeBox+o)+clicked}'] = Food([(pos[0]//size)*size-(2*size)+o*size, (pos[1]//size)*size-(2*size)+i*size], ((i-1)*sizeBox+o)+clicked)
        for i in range(1+clicked, sizeBox*sizeBox+clicked+1):
            allFoodPoses.append([i, globals()[f'food{i}'].pos])
    
    def deleteFood(clicked):
        global allFoodPoses
        for i in range(0, clicked+1):
            try:
                del globals()[f'food{i}']
            except:
                pass
        allFoodPoses = []
    
    def resetAnt(numAnts):
        for i in range(1, numAnts):
            try:
                del globals()[f'ant{i}']
            except:
                pass
            
    def addVariables(num, name, variableData = None):
        varNames = []
        for i in range(0, num):
            varNames.append(f'{name}{i+1}')
            globals()[f'{name}{i+1}'] = variableData
        return varNames
    
    
    """colours"""
    white = (255, 255, 255)
    black = (0, 0, 0)
    """constants"""
    keys1 = [pygame.K_1 ,pygame.K_2 ,pygame.K_3 ,pygame.K_4 ,pygame.K_5 ,pygame.K_6 ,pygame.K_7 ,pygame.K_8 ,pygame.K_9]
    size = 5
    numAnts =1+ 30
    """resolution"""
    w = 1080
    h = 720
    """variables"""
    pause = False
    e = None
    sizeBox = 5
    clicked = 0
    trails = []
    """creating ant objects"""
    for i in range(1, numAnts):
        globals()[f'ant{i}'] = Ant(i, [(w/2)//size*size, (h/2)//size*size], w, h, size)

    """pygame surfaces"""
    screen = pygame.display.set_mode((w, h))
    resetAntsRect = pygame.rect.Rect(10, 10, 60, 20)
    resetFoodRect = pygame.rect.Rect(75, 10, 60, 20)
    
    
    running = 1
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_SPACE:
                    if pause: pause = False
                    else:pause = True
                
                if event.key in keys1:
                    pos = pygame.mouse.get_pos()
                    sizeBox = 4*(keys1.index(event.key)+1) 
                    
                
            if event.type == pygame.MOUSEBUTTONUP: 
                pos = pygame.mouse.get_pos()
                if resetAntsRect.collidepoint(pos):
                    resetAnt(numAnts)  
                    for i in range(1, numAnts):
                        globals()[f'ant{i}'] = Ant(i, [(w/2)//size*size, (h/2)//size*size], w, h, size)
                elif resetFoodRect.collidepoint(pos):
                    print('food reset')
                    deleteFood(clicked)
                    clicked = 0
                else:
                    summonFood(pos, clicked, sizeBox)
                    clicked += sizeBox*sizeBox
                
                    
        screen.fill(white)
        r = pygame.draw.rect(screen, black, resetAntsRect)
        #message(screen, 'Reset ants', 40, 20, 10, white)
        r2 = pygame.draw.rect(screen, black, resetFoodRect)
        #message(screen, 'Reset food', 105, 20, 10, white)
        #listInstances(Food)
        print(len(globals()))
        for obj in gc.get_objects():
            if isinstance(obj, Ant):
                e = obj.execute(screen, allFoodPoses, trails, pause)
                trails.append(obj.trailPositions)
                try:
                    if e != None and e[0]:
                        del globals()[f'food{allFoodPoses[e[1]][0]}']
                        del allFoodPoses[e[1]]
                except:
                    pass
        
        for obj in gc.get_objects():
            if isinstance(obj, Food):
                obj.drawFood(screen, size)
        
        pygame.display.update()
        clock.tick(20)

if __name__ == '__main__':
    main()