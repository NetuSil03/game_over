import pygame
import pygame as pg
import sys


class Game_over(pg.sprite.Sprite):
    def __init__(self, x, y, filename):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        if self.rect.x != 0:
            self.rect.x += 4


def main():
    W = 600
    H = 300
    Blue = (0, 0, 255)
    my_path = 'C:/Users/Alex/PycharmProjects/untitled_1/'
    # my_path = ''
    clock = pygame.time.Clock()
    sc = pg.display.set_mode((W, H))
    game_over = Game_over(-300, 150, my_path + 'data/gameover.png')
    while 1:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        pygame.display.set_caption('Game over')
        sc.fill(Blue)
        sc.blit(game_over.image, game_over.rect)
        pg.display.update()
        game_over.update()
        clock.tick(200)


if __name__ == '__main__':
    main()
