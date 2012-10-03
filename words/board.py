import os
import pygame
import itertools
from pygame.locals import *


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
    piece_coord = (index, (tile_w, tile_h))
    piece = Piece()
    piece.image = tilesheet.subsurface(piece_coord)
    piece.rect  = piece.image.get_rect()
    return piece


class Board:
    def __init__(self):
        self.tilesheet = loadImage('scrabble.jpg',-1)[0]
        self.letters = {
                    'a': createPiece('a', self.tilesheet, (5,9)),
                    'b': createPiece('b', self.tilesheet, (173,9)),
                    'c': createPiece('c', self.tilesheet, (283,9)),
                    'd': createPiece('d', self.tilesheet, (338,9)),
                    'e': createPiece('e', self.tilesheet, (500,9)),
                    'f': createPiece('f', self.tilesheet, (116,70)),
                    'g': createPiece('g', self.tilesheet, (228,69)),
                    'h': createPiece('h', self.tilesheet, (444,68)),
                    'i': createPiece('i', self.tilesheet, (3,130)),
                    'j': createPiece('j', self.tilesheet, (114,130)),
                    'k': createPiece('k', self.tilesheet, (170,130)),
                    'l': createPiece('l', self.tilesheet, (226,128)),
                    'm': createPiece('m', self.tilesheet, (444,127)),
                    'n': createPiece('n', self.tilesheet, (3,190)),
                    'o': createPiece('o', self.tilesheet, (114,191)),
                    'p': createPiece('p', self.tilesheet, (282,189)),
                    'q': createPiece('q', self.tilesheet, (392,188)),
                    'r': createPiece('r', self.tilesheet, (448,188)),
                    's': createPiece('s', self.tilesheet, (115,250)),
                    't': createPiece('t', self.tilesheet, (225,249)),
                    'u': createPiece('u', self.tilesheet, (391,247)),
                    'v': createPiece('v', self.tilesheet, (4,310)),
                    'w': createPiece('w', self.tilesheet, (113,309)),
                    'x': createPiece('x', self.tilesheet, (224,309)),
                    'y': createPiece('y', self.tilesheet, (280,308)),
                    'z': createPiece('z', self.tilesheet, (390,306))
                }
        self.cur_iter  = itertools.cycle(range(ord('a'),ord('z')+1))
        self.cur_letter = chr(self.cur_iter.next())

    def nextLetter(self):
        self.cur_letter = chr(self.cur_iter.next())

    def draw(self, screen):
        cur_piece = self.letters[self.cur_letter]
        screen.blit(cur_piece.image,cur_piece.rect)


