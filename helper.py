from settings import *
import pygame as pg


def text_to_screen(screen,text,col,size,x,y):
    font = pg.font.SysFont('arial',size)
    text_surface = font.render(text,True,col)
    text_rect = text_surface.get_rect()
    text_rect.center = (x,y)
    screen.blit(text_surface,text_rect)

class Pointer:
    def __init__(self,game,row,col):
        self.row = row
        self.col = col
        self.prev_row = None
        self.prev_col = None
        self.game = game

    def update(self,row,col):
        self.prev_col = self.col
        self.prev_row = self.row
        self.row = row
        self.col = col

    def draw_selected(self):
        pg.draw.rect(self.game.screen,BLUE,
                    [self.col*TILESIZE,self.row*TILESIZE,TILESIZE-1,TILESIZE-1],2)
