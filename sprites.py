from settings import *
import pygame as pg


class Piece(pg.sprite.Sprite):
    def __init__(self,game,row,col,img,army):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.image = img#pg.transform.scale(img,(TILESIZE,TILESIZE))
        #self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.game = game
        self.pos = (row,col)
        self.active = False
        self.army = army

    def update(self):
        self.rect.center = ((self.pos[1]+0.5)*TILESIZE,(self.pos[0]+0.5)*TILESIZE)
        if self.active:
            self.game.set_movable(self.get_movable_pos())


    def get_movable_pos(self):
        return []

    def move(self,row,col):
        self.pos = (row,col)

class King(Piece):
    def get_movable_pos(self):
        self.movable_pos = []
        # optimized for king
        for i in range(self.pos[0]-1,self.pos[0]+2):
            for j in range(self.pos[1]-1,self.pos[1]+2):
                if ((i>=0)&(i<=7))&((j>=0)&(j<=7)):
                    data = self.game.map_data[i][j]['occupied']
                    if data:
                        if self.army != self.game.map_data[i][j]['army']:
                            self.movable_pos.append((i,j))
                    else:
                        self.movable_pos.append((i,j))
        #print(movable_pos)
        return self.movable_pos


class Rook(Piece):
    def get_movable_pos(self):
        self.movable_pos = []
        # optimized for rook
        for j in range(self.pos[1]+1,8):
            # for right side of rook
            if self.data_feed(self.pos[0],j):
                break
        for j in range(self.pos[1]-1,-1,-1):
            # for left side of rook
            if self.data_feed(self.pos[0],j):
                break
        for j in range(self.pos[0]+1,8):
            # for lower side of rook
            if self.data_feed(j,self.pos[1]):
                break
        for j in range(self.pos[0]-1,-1,-1):
            # for upper side of rook
            if self.data_feed(j,self.pos[1]):
                break
        #print(movable_pos)
        return self.movable_pos

    def data_feed(self,row,col):
        data = self.game.map_data[row][col]['occupied']
        if data:
            if self.army != self.game.map_data[row][col]['army']:
                self.movable_pos.append((row,col))
            return True
        else:
            self.movable_pos.append((row,col))
            return False

class Bishop(Piece):
    def get_movable_pos(self):
        self.movable_pos = []
        # optimized for rook
        x,y = self.pos[0],self.pos[1]
        while(x>0 and y>0):
            # for upper-left side of bishop
            if self.data_feed(x-1,y-1):
                break
            x,y = x-1,y-1
        x,y = self.pos[0],self.pos[1]
        while(x>0 and y<7):
            # for upper-right side of bishop
            if self.data_feed(x-1,y+1):
                break
            x,y = x-1,y+1
        x,y = self.pos[0],self.pos[1]
        while(x<7 and y>0):
            # for lower-left side of bishop
            if self.data_feed(x+1,y-1):
                break
            x,y = x+1,y-1
        x,y = self.pos[0],self.pos[1]
        while(x<7 and y<7):
            # for lower-right side of bishop
            if self.data_feed(x+1,y+1):
                break
            x,y = x+1,y+1
        #print(movable_pos)
        return self.movable_pos

    def data_feed(self,row,col):
        data = self.game.map_data[row][col]['occupied']
        if data:
            if self.army != self.game.map_data[row][col]['army']:
                self.movable_pos.append((row,col))
            return True
        else:
            self.movable_pos.append((row,col))
            return False

class Queen(Piece):
    def get_movable_pos(self):
        self.movable_pos = []
        x,y = self.pos[0],self.pos[1]
        while(x>0 and y>0):
            # for upper-left side of bishop
            if self.data_feed(x-1,y-1):
                break
            x,y = x-1,y-1
        x,y = self.pos[0],self.pos[1]
        while(x>0 and y<7):
            # for upper-right side of bishop
            if self.data_feed(x-1,y+1):
                break
            x,y = x-1,y+1
        x,y = self.pos[0],self.pos[1]
        while(x<7 and y>0):
            # for lower-left side of bishop
            if self.data_feed(x+1,y-1):
                break
            x,y = x+1,y-1
        x,y = self.pos[0],self.pos[1]
        while(x<7 and y<7):
            # for lower-right side of bishop
            if self.data_feed(x+1,y+1):
                break
            x,y = x+1,y+1
        for j in range(self.pos[1]+1,8):
            # for right side of rook
            if self.data_feed(self.pos[0],j):
                break
        for j in range(self.pos[1]-1,-1,-1):
            # for left side of rook
            if self.data_feed(self.pos[0],j):
                break
        for j in range(self.pos[0]+1,8):
            # for lower side of rook
            if self.data_feed(j,self.pos[1]):
                break
        for j in range(self.pos[0]-1,-1,-1):
            # for upper side of rook
            if self.data_feed(j,self.pos[1]):
                break
        #print(movable_pos)
        return self.movable_pos

    def data_feed(self,row,col):
        data = self.game.map_data[row][col]['occupied']
        if data:
            if self.army != self.game.map_data[row][col]['army']:
                self.movable_pos.append((row,col))
            return True
        else:
            self.movable_pos.append((row,col))
            return False

class Knight(Piece):
    def get_movable_pos(self):
        self.movable_pos = []
        # optimized for knight
        for i in [self.pos[0]-2,self.pos[0]+2]:
            for j in [self.pos[1]-1,self.pos[1]+1]:
                self.data_feed(i,j)
        for i in [self.pos[0]-1,self.pos[0]+1]:
            for j in [self.pos[1]-2,self.pos[1]+2]:
                self.data_feed(i,j)
        #print(movable_pos)
        return self.movable_pos

    def data_feed(self,row,col):
        if ((row>=0)&(row<=7)) and ((col>=0)&(col<=7)):
            data = self.game.map_data[row][col]['occupied']
            if data:
                if self.army != self.game.map_data[row][col]['army']:
                    self.movable_pos.append((row,col))
            else:
                self.movable_pos.append((row,col))

class Pawn(Piece):
    def get_movable_pos(self):
        self.movable_pos = []
        # optimized for pawn
        if self.army == 'WHITE':
            if self.pos[0] > 0:
                self.data_feed(-1)
        if self.army == 'BLACK':
            if self.pos[0] < 7:
                self.data_feed(1)
        #print(movable_pos)
        return self.movable_pos

    def data_feed(self,bias):
        data =  self.game.map_data[self.pos[0]+bias][self.pos[1]]['occupied']
        if not data:
            self.movable_pos.append((self.pos[0]+bias,self.pos[1]))
        if self.pos[1] != 7:
            data = self.game.map_data[self.pos[0]+bias][self.pos[1]+1]['occupied']
            if data:
                if self.army != self.game.map_data[self.pos[0]+bias][self.pos[1]+1]['army']:
                    self.movable_pos.append((self.pos[0]+bias,self.pos[1]+1))
        if self.pos[1] != 0:
            data = self.game.map_data[self.pos[0]+bias][self.pos[1]-1]['occupied']
            if data:
                if self.army != self.game.map_data[self.pos[0]+bias][self.pos[1]-1]['army']:
                    self.movable_pos.append((self.pos[0]+bias,self.pos[1]-1))
