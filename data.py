from os import path
import pygame as pg
from sprites import King, Queen , Bishop, Knight, Rook, Pawn


ARMY = [(1,Rook,'rook.png'),(2,Knight,'knight.png'),(3,Bishop,'bishop.png'),(4,Queen,'queen.png'),
        (5,King,'king.png'),(6,Bishop,'bishop.png'),(7,Knight,'knight.png'),(8,Rook,'rook.png')]

# images loading folder setting
game_folder = path.dirname(__file__)
img_folder = path.join(game_folder,'imgs')


def load_data(game):
    a = []
    for i in range(8):
        new_list = []
        for j in range(8):
            new_list.append({'occupied':False,
                            'occupied_by':None,
                            'army':'None'})
        a.append(new_list)


    for pair in ARMY:
        image = 'chess_piece_2_black_'+pair[2]
        img = pg.image.load(path.join(img_folder,image)).convert()
        data = a[0][pair[0]-1]
        data['occupied'] = True
        data['occupied_by'] = pair[1](game,0,pair[0]-1,img,"BLACK")
        data['army'] = 'BLACK'

    image = 'chess_piece_2_black_pawn.png'
    img = pg.image.load(path.join(img_folder,image)).convert()
    for c in range(8):
        data = a[1][c]
        data['occupied'] = True
        data['occupied_by'] = Pawn(game,1,c,img,"BLACK")
        data['army'] = 'BLACK'

    image = 'chess_piece_2_white_pawn.png'
    img = pg.image.load(path.join(img_folder,image)).convert()
    for c in range(8):
        data = a[6][c]
        data['occupied'] = True
        data['occupied_by'] = Pawn(game,6,c,img,"WHITE")
        data['army'] = 'WHITE'


    for pair in ARMY:
        image = 'chess_piece_2_white_'+pair[2]
        img = pg.image.load(path.join(img_folder,image)).convert()
        data = a[7][pair[0]-1]
        data['occupied'] = True
        data['occupied_by'] = pair[1](game,7,pair[0]-1,img,"WHITE")
        data['army'] = 'WHITE'
    return a
