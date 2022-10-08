'''
Created on 16 Sept 2022

@author: coding
'''

size = 40
w = 1080
h = 720

white = (255,255,255)
black = (0,0,0)
green1 = (0, 90, 0)
green2 = (0, 150, 0)
green3 = (0, 210, 0)
green4 = (10, 255, 10)
green5 = (120, 255, 120)

grid = []
for i in range(0, int(w/size)):
    a = []
    for o in range(0, int(h/size)):
        a.append(0)
    grid.append(a)

