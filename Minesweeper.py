# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 11:26:57 2019

@author: steven.melville
"""

import sys, pygame

pygame.init()

size = width, height = 640, 480
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

while 1:
    ev = pygame.event.get()
    
    for event in ev:
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            speed[0] = 2 * speed[0]
            speed[1] = 2 * speed[1]

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
        

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()