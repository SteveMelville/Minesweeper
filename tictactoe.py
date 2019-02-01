# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 11:34:05 2019

@author: steven.melville
"""


import pygame, sys

letters = []
colors = [(0,0,0),(255,0,0),(0,0,255), (255,255,255)]

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
                    return 2
                else:
                    self.player = 2
                    return 1
        return turn
        
    def draw(self, screen):
        pygame.draw.rect(screen, colors[self.player], self.rect)
        pygame.draw.rect(screen, colors[self.player], self.rect)
        screen.blit()
        pygame.draw.rect(screen, (128,128,128), self.rect, 10)
        
def isWinner(board):
    for x in range(0,3):
        if board[x][0].player == board[x][1].player and board[x][2].player == board[x][0].player and not board[x][0].player == 0:
            return board[x][0].player
        if board[0][x].player == board[1][x].player and board[2][x].player == board[0][x].player and not board[0][x].player == 0:
            return board[0][x].player
        
    if board[0][0].player == board[1][1].player and board[2][2].player == board[0][0].player and not board[0][0].player == 0:
            return board[0][0].player
    if board[2][0].player == board[1][1].player and board[0][2].player == board[2][0].player and not board[2][0].player == 0:
            return board[2][0].player
    return 0


def main():
    global letters
    pygame.init()
    size = width, height = 600, 600
    screen = pygame.display.set_mode(size)
    
    turn = 1
    
    basicfont = pygame.font.SysFont(None, 48)
    font1 = pygame.font.SysFont('Papyrus', 200, bold=True)
    textX = font1.render('X', True, colors[1], colors[0])
    textY = font1.render('Y', True, colors[2], colors[0])
    blank = font1.render(" ", True, colors[0], colors[0])
    xrect = textX.get_rect()
    yrect = textY.get_rect()
    
    letters = [blank, textX, textY]
    
    squares = [[cell(x,y) for y in range(0,3)] for x in range(0,3)]
    
    while True:
        ev = pygame.event.get()
    
        for event in ev:
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(0,3):
                    for j in range(0,3):
                        turn = squares[i][j].click(event.pos, turn)
            if isWinner(squares) != 0:
                for x in range(0,3):
                    for y in range(0,3):
                        squares[x][y].player = isWinner(squares)
                        squares[x][y].isClicked = True
                turn = isWinner(squares)
                
        screen.fill((0,0,0))
        
        text = basicfont.render('Player: ' + str(turn), True, colors[3], colors[0])
        textrect = text.get_rect()
        textrect.centerx = screen.get_rect().centerx
        textrect.centery = screen.get_rect().centery
        
        for i in range(0,3):
            for j in range(0,3):
                squares[i][j].draw(screen)
                
        screen.blit(text, textrect)
        
        pygame.display.flip()
            
    

        
main()