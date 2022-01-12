import pygame as pg
from os import path
import sys
from settings import *
from helper import Pointer, text_to_screen
from data import load_data


class Game:
    def __init__(self):
        # initialize all things
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(APP_NAME)
        self.running = True
        self.clock = pg.time.Clock()
        #pg.key.set_repeat(500,100)

    def load_data(self):
        #loading data from map
        self.map_data = load_data(self)
        #print(self.map_data)

    def update_data(self,piece):
        #update data locations
        data = self.map_data[self.pointer.row][self.pointer.col]
        prev_data = self.map_data[self.pointer.prev_row][self.pointer.prev_col]
        prev_data['occupied'] = False
        prev_data['occupied_by'] = None
        prev_data['army'] = 'None'
        if data['occupied']:
            data['occupied_by'].kill()
        data['occupied'] = True
        data['occupied_by'] = piece
        data['army'] = piece.army

    def new(self):
        # start new game
        self.movable_list = []
        self.turn = 'WHITE'
        self.pointer = Pointer(self,4,4)
        self.all_sprites = pg.sprite.Group()
        self.load_data()
        self.playing = True

    def draw_grid(self):
        #draw grid on the screen
        for r in range(0,GRID_WIDTH):
            for c in range(0,GRID_HEIGHT):
                col = WHITE if (r+c)%2 == 0 else GREY
                pg.draw.rect(self.screen,col,[r*TILESIZE,c*TILESIZE,TILESIZE-1,TILESIZE-1])

    def run(self):
        # run loop
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def events(self):
        # game loop - events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

            if event.type == pg.MOUSEBUTTONDOWN:
                self.update_pointer(event.pos)

    def update(self):
        # game loop - update
        self.all_sprites.update()

    def draw(self):
        # game loop - draw
        self.screen.fill(BLACK)
        self.draw_grid()
        self.draw_movable()
        self.all_sprites.draw(self.screen)
        self.pointer.draw_selected()
        text_to_screen(self.screen,"Credits : umrao-ak47",RED,25,WIDTH/2,HEIGHT-20)
        text_to_screen(self.screen,"Turn : "+self.turn,YELLOW,20,WIDTH/2,HEIGHT-40)
        pg.display.flip()

    def game_start_screen(self):
        # game splash screen
        pass

    def game_go_screen(self):
        # game over screen
        pass

    def update_pointer(self,pos):
        col,row = pos[0]//TILESIZE,pos[1]//TILESIZE
        #print("Col =",col+1,"Row =",row+1)
        if col<8 and row<8:
            self.pointer.update(row,col)
            self.activate_piece()

    def activate_piece(self):
        # only store copy not address
        data = self.map_data[self.pointer.row][self.pointer.col].copy()
        prev_data_holder = self.map_data[self.pointer.prev_row][self.pointer.prev_col]['occupied_by']
        if (self.pointer.row,self.pointer.col) in self.movable_list:
            prev_data_holder.move(self.pointer.row,self.pointer.col)
            self.update_data(prev_data_holder)
            self.turn = 'BLACK' if self.turn == 'WHITE' else 'WHITE'
        try:
            self.movable_list = []
            prev_data_holder.active = False
        except:
            pass
        if data['occupied']:
            if self.turn == data['army']:
                data['occupied_by'].active = True

    def set_movable(self,movable_list):
        self.movable_list = movable_list

    def draw_movable(self):
        for pos in self.movable_list:
            pg.draw.rect(self.screen,LIGHTGREEN,[pos[1]*TILESIZE+2,pos[0]*TILESIZE+2,TILESIZE-4,TILESIZE-4])


    def quit(self):
        if self.playing:
            self.playing = False
        self.running = False
        self.game_go_screen()
        pg.quit()
        sys.exit()


if __name__ == "__main__":
    g = Game()
    g.game_start_screen()
    while g.running:
        g.new()
        g.run()
