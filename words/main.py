import os
from tree import WordTree
import pygame
from pygame.locals import *


def loadImage(name, colorkey=None):
    fullname = os.path.join('bin', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
    image = image.subsurface((173,9,45,51))
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


def main():
    with open("/usr/share/dict/words", 'r') as f:
        l = []
        for line in f:
            l.append(line.strip())

    wt = WordTree()
    for line in l:
        wt.addWord(line)
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    pygame.display.set_caption('Words')

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    pygame.display.flip()
    sprite = pygame.sprite.Sprite()
    sprite.image, sprite.rect = loadImage('scrabble.jpg', -1)
    allsprites = pygame.sprite.RenderPlain(sprite)
    clock = pygame.time.Clock()

    while 1:
        clock.tick(60)

    #Handle Input Events
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            elif event.type == MOUSEBUTTONDOWN:
                if fist.punch(chimp):
                    punch_sound.play() #punch
                    chimp.punched()
                else:
                    whiff_sound.play() #miss
            elif event.type is MOUSEBUTTONUP:
                fist.unpunch()

        sprite.update()

    #Draw Everything
        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
