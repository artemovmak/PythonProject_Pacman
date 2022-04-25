import pygame as pg

from Constants import BLOCK_SIZE, SEED_SIZE, SEED_COLOR, WHITE, PILL_RADIUS
from GameObject import GameObject


class Grid(GameObject):
    def __init__(self, width, height, x, y, screen, color):
        super().__init__(width, height, x, y, screen)
        self.color = color
        self.has_seed = False
        self.has_pill = False
        self.seed_rect = [0, 0, 0, 0]
        self.seed_rect[0] = self.rect[0] + \
            BLOCK_SIZE[0] // 2 - SEED_SIZE[0] // 2
        self.seed_rect[1] = self.rect[1] + \
            BLOCK_SIZE[1] // 2 - SEED_SIZE[1] // 2
        self.seed_rect[2] = SEED_SIZE[0]
        self.seed_rect[3] = SEED_SIZE[1]
        self.pill_center = [
            self.rect[0] + BLOCK_SIZE[0] // 2,
            self.rect[1] + BLOCK_SIZE[0] // 2]

    def draw(self):
        pg.draw.rect(self.screen, self.color, self.rect)
        if self.has_seed:
            pg.draw.rect(self.screen, SEED_COLOR, self.seed_rect)
        elif self.has_pill:
            pg.draw.circle(self.screen, WHITE, self.pill_center, PILL_RADIUS)
