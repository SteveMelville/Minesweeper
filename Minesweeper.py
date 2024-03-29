# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 11:26:57 2019

@author: steven.melville
"""

import pygame, sys, random

colors = [(0,0,0),(200,200,200),(0,0,255), (255,0,0), (255,255,255)]
    
numRows = 8
numCollumns = 8
numMines = 10

class cell:
    def __init__(self, x, y):
        self.isClicked = False
        self.rect = pygame.Rect(20*x, 20*y, 20, 20)
        self.type = 1
        self.isMine = False
        self.isFlag = False
        self.numMines = 0
        self.x = x
        self.y = y
        
    def click(self, pos, button):
        if self.isClicked == False:
            if self.rect.collidepoint(pos):
                self.isClicked = True
                if button == 1:
                    self.type = self.sweep()
                    if self.isMine:
                        return True, False, self.isClicked
                    else:
                        return False, False, self.isClicked
                elif button == 3:
                    self.type = 3
                    self.isFlag = True
                    return False, True, self.isClicked
                elif button == 2:
                    self.isClicked = False
        return False, False, False
    
    def initClick(self, pos):
        if self.rect.collidepoint(pos):
            return True
        else:
            return False
    
    def sweep(self):
        if self.isMine:
            return 0
        else:
            return 4
        
    def draw(self, screen, text, textrect):
        textrect.centerx = self.x * 20 + 10
        textrect.centery = self.y * 20 + 10
        
        pygame.draw.rect(screen, colors[self.type], self.rect)
        pygame.draw.rect(screen, (128,128,128), self.rect, 2)
        if self.type == 4 and not self.isMine and not self.isFlag:
            screen.blit(text, textrect)
            
            
        
def isWinner(board, width, height, numMines):
    isWon = True
    numFlags = 0
    flagError = False
    for x in range(0,width):
        for y in range(0,height):
            if not board[x][y].isClicked:
                isWon = False
            if board[x][y].isFlag:
                numFlags += 1
     
    if isWon:
        if numFlags > numMines:
            loseGame(board, width, height)
            flagError = True
            isWon = False
        
    return isWon, flagError
            


def loseGame(board, width, height):
    for x in range(0,width):
        for y in range(0,height):
            board[x][y].isClicked = True
            if board[x][y].isMine and not board[x][y].isFlag:
                board[x][y].type = 0
            elif board[x][y].isMine and board[x][y].isFlag:
                board[x][y].type = 2
                
                
    

def generateBoard(board, width, height, numSquares, mines, initX, initY):
    numMines = 0
    minesLeft = mines
    success = True
    for x in range(0,width):
        for y in range(0,height):
            num = random.randint(0, numSquares)
            if not x == initX and not y == initY:
                if num <= mines and numMines < mines:
                    board[x][y].isMine = True
                    minesLeft -= 1
                    numMines += 1
                    numSquares = numSquares - 1
                else:
                    board[x][y].isMine = False
                    numSquares = numSquares - 1
            else:
                board[x][y].isMine = False
                numSquares = numSquares - 1
    
    while numMines < mines:
        success = False
        for x in range(0,width):
            for y in range(0,height):
                spot = board[x][y]
                if not success:
                    if not spot.isMine and not x == initX and not y == initY:
                        spot.isMine = True
                        numMines += 1
                        success = True
                
                
    for x in range(0,width):
        for y in range(0, height):
            count = 0
            if not board[x][y].isMine:
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i + x < width and j + y < height and i + x >= 0 and j + y >= 0:
                            if board[x + i][y + j].isMine:
                                count = count + 1
    
                board[x][y].numMines = count
    return board



def main(xwidth, yheight, mines):

    numSquares = xwidth * yheight
    pygame.init()
    
    width, height = xwidth * 20, yheight * 20 + 50
    if width < 200:
        width = 200
    
    size = width, height
    screen = pygame.display.set_mode(size)
    numMines = mines 
    firstClick = True
    isWon = False
    isLost = False
    flagError = False
    
    basicfont = pygame.font.SysFont(None, 24)
    
    squares = [[cell(x,y) for y in range(0,yheight)] for x in range(0,xwidth)]
    
    
    while True:
        ev = pygame.event.get()
    
        for event in ev:
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if firstClick:
                    initX = -1
                    initY = -1
                    
                    for x in range(0,xwidth):
                        for y in range(0,yheight):
                            isStart = squares[x][y].initClick(event.pos)
                            if isStart:
                                initX = x
                                initY = y
                                
                    if initX > -1 and initY > -1:
                        squares = generateBoard(squares, xwidth, yheight, numSquares, mines, initX, initY)
                        squares[initX][initY].click(event.pos, event.button)
                        numSquares = numSquares - 1
                        firstClick = False
        
                        
                else:
                    for x in range(0,xwidth):
                        for y in range(0,yheight):
                            isMine, isFlag, isClicked = squares[x][y].click(event.pos, event.button)
                            if isClicked:
                                isWon, flagError = isWinner(squares, xwidth, yheight, mines)
                            if isMine:
                                loseGame(squares, xwidth, yheight)
                                isLost = True
                                numSquares = 0
                            if isFlag:
                                numMines = numMines - 1
                                
        
                                
        
            
                
        screen.fill((0,0,0))
        
        for x in range(0,xwidth):
            for y in range(0,yheight):
                text = basicfont.render(str(squares[x][y].numMines), True, colors[3], colors[4])
                textrect = text.get_rect()
                squares[x][y].draw(screen, text, textrect)        
            
        if isWon:
            barText = "You have won :("
        else:
            barText = "Number of Mines Left: " + str(numMines)
            
        if isLost or flagError:
            barText = "You Lose >:D"
            
        minesLeft = basicfont.render(barText, True, colors[4], colors[0])
        minerect = minesLeft.get_rect()
        minerect.centerx = width / 2
        minerect.centery = yheight * 20 + 30
        screen.blit(minesLeft,minerect)
        
        pygame.display.flip()

main(numRows, numCollumns, numMines)