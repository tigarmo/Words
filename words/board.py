import os
import pygame
from pygame.locals import *

letter_coords = {
            'a': (5,9),
            'b': (173,9),
            'c': (283,9),
            'd': (338,9),
            'e': (500,9),
            'f': (116,70),
            'g': (228,69),
            'h': (444,68),
            'i': (3,130),
            'j': (114,130),
            'k': (170,130),
            'l': (226,128),
            'm': (444,127),
            'n': (3,190),
            'o': (114,191),
            'p': (282,189),
            'q': (392,187),
            'r': (448,188),
            's': (115,250),
            't': (225,249),
            'u': (391,247),
            'v': (4,310),
            'w': (113,309),
            'x': (224,309),
            'y': (280,308),
            'z': (390,306)
        }

class Piece(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

def loadImage(name, colorkey=None):
    fullname = os.path.join('bin', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


def createPiece(letter, tilesheet, index):
    tile_w, tile_h = 46, 51
    space_w, space_h = tile_w + 11, tile_h + 7
    piece_coord = (letter_coords[letter], (tile_w, tile_h))
    piece = Piece()
    piece.image = tilesheet.subsurface(piece_coord)
    piece.rect  = piece.image.get_rect()
    return piece


class Board:
    def __init__(self):
        self.tilesheet = loadImage('scrabble.jpg',-1)[0]
        self.piece_a   = createPiece('z', self.tilesheet, (3,0))
        self.allsprites = pygame.sprite.RenderPlain(self.piece_a)

    def draw(self, screen):
        self.allsprites.draw(screen)


