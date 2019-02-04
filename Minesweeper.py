# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 11:26:57 2019

@author: steven.melville
"""

import pygame, sys, random

colors = [(0,0,0),(200,200,200),(0,0,255), (255,0,0), (255,255,255)]

class cell:
    def __init__(self, x, y):
        self.isClicked = False
        self.rect = pygame.Rect(20*x, 20*y, 20, 20)
        self.type = 1
        self.isMine = False
        self.text
        self.testrect
        
    def click(self, pos, button):
        if self.isClicked == False:
            if self.rect.collidepoint(pos):
                self.isClicked = True
                if button == 1:
                    self.type = self.sweep()
                elif button == 3:
                    self.type = 3
                elif button == 2:
                    self.isClicked = False
                
    def sweep(self, basicfont):
        if self.isMine:
            return 0
        else:
            text = basicfont.render(str(num), True, colors[3], colors[0])
            return 4
        
    def draw(self, screen):
        pygame.draw.rect(screen, colors[self.type], self.rect)
        screen.blit(self.text, self.textrect)
        pygame.draw.rect(screen, (128,128,128), self.rect, 2)
        
def isWinner(board):
    return 0


def generateBoard(board, width, height, numSquares, mines):
    for x in range(0,width):
        for y in range(0,height):
            num = random.randint(1, numSquares)
            if num <= mines:
                board[x][y].isMine = True
                mines = mines - 1
                numSquares = numSquares - 1
            else:
                board[x][y].isMine = False
                numSquares = numSquares - 1
    
    return board

def main(xwidth, yheight, mines):

    numSquares = xwidth * yheight
    pygame.init()
    size = width, height = xwidth * 20, yheight * 20
    screen = pygame.display.set_mode(size)
    
    basicfont = pygame.font.SysFont(None, 48)
    
    squares = [[cell(x,y) for y in range(0,yheight)] for x in range(0,xwidth)]
    
    squares = generateBoard(squares, xwidth, yheight, numSquares, mines)
    
    while True:
        ev = pygame.event.get()
    
        for event in ev:
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for x in range(0,xwidth):
                    for y in range(0,yheight):
                        squares[x][y].click(event.pos, event.button)
            
                
        screen.fill((0,0,0))
        
        #text = basicfont.render('Player: ' + str(turn), True, colors[3], colors[0])
        #textrect = text.get_rect()
        #textrect.centerx = screen.get_rect().centerx
        #textrect.centery = screen.get_rect().centery
        
        for x in range(0,xwidth):
            for y in range(0,yheight):
                squares[x][y].draw(screen)
                
        
        
        pygame.display.flip()
            
    

        
main(5, 5, 10)