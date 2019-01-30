# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 11:34:05 2019

@author: steven.melville
"""

import pygame, sys

class cell:
    def __init__(self, x, y):
        self.isClicked = False
        self.rect = pygame.Rect(200*x, 200*y, 200, 200)
        self.player = 0
        
    def click(self, pos, turn):
        if self.isClicked == False:
            if self.rect.collidepoint(pos):
                self.isClicked = True
                if turn == 1:
                    self.player = 1
                else:
                    self.player = 2
            
        
    def draw(self, screen):
        
        if self.isClicked:
            if self.player == 1:
                pygame.draw.rect(screen, (255,0,0), self.rect)
            elif self.player == 2:
                pygame.draw.rect(screen, (0,255,0), self.rect)
            
        
        pygame.draw.rect(screen, (128,128,128), self.rect, 10)
        

def main():
    pygame.init()
    
    size = width, height = 600, 600
    
    turn = 1
    
    squares = [[cell(x,y) for y in range(0,3)] for x in range(0,3)]
    
    
    screen = pygame.display.set_mode(size)
    
    while True:
        ev = pygame.event.get()
    
        for event in ev:
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(0,3):
                    for j in range(0,3):
                        squares[i][j].click(event.pos, turn)
                if turn == 1: turn = 2
                else: turn = 1
                
        screen.fill((0,0,255))
        
        for i in range(0,3):
            for j in range(0,3):
                squares[i][j].draw(screen)
        
        pygame.display.flip()
            
    

        
main()