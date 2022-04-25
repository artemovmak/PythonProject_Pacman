from math import floor

import pygame as pg

from Constants import BLOCK_SIZE, RESOLUTION
from GameObject import GameObject
from Wall import Wall


class MovingEntity(GameObject):
    def __init__(self, width, height, x, y, screen):
        super().__init__(width, height, x, y, screen)
        self.rect = pg.Rect(x, y, width, height)
        self.tileX = floor((self.rect.x + self.width / 2) / BLOCK_SIZE[0])
        self.tileY = floor((self.rect.y + self.height / 2) / BLOCK_SIZE[1]) 
        self.portal_check = False

    def collideWall(self, direction, arr):
        for i in arr:
            for j in i:
                if type(j) == Wall:
                    if self.cMove(direction).colliderect(j.rect) == 1:
                        return True
        return False

    def cMove(self, direction):
        rect_ = pg.Rect(self.rect.x, self.rect.y, self.width, self.height)
        if direction == 0:
            if rect_.x + rect_[2] < RESOLUTION[0]:
                rect_.x += self.speed 
        elif direction == 1:
            if rect_.y > 0:
                rect_.y -= self.speed
        elif direction == 2:
            if rect_.x > 0:
                rect_.x -= self.speed
        elif direction == 3:
            if rect_.y + rect_[3] < RESOLUTION[1]:
                rect_.y += self.speed
        return rect_

    def CountTile(self):
        centerX = self.rect.x + self.width / 2
        centerY = self.rect.y + self.height / 2
        nowTileX = centerX/BLOCK_SIZE[0]
        nowTileY = centerY/BLOCK_SIZE[1]
        self.tileX = floor(nowTileX)
        self.tileY = floor(nowTileY)

        return [self.tileX, self.tileY]
