import pygame as pg
from Constants import BLOCK_SIZE
from GameObject import GameObject
from math import floor


class Portal(GameObject):
    def __init__(self, width, height, x, y, screen, id_, id_to):
        super().__init__(width, height, x, y, screen)
        self.tileX = floor((self.x + self.width / 2) / BLOCK_SIZE[0])
        self.tileY = floor((self.y + self.height / 2) / BLOCK_SIZE[1])
        self.id_ = id_
        self.id_to = id_to

    def colideTeleport(self, objectsToColide, portals):
        for i in objectsToColide:
            if i.tileY == self.tileY and i.tileX == self.tileX:
                i.portal_check = True
                self.teleport(i, portals)

    def teleport(self, object_, portals):
        dest = self.id_to
        for i in portals:
            if i.id_ == dest and i.id_ != self.id_:
                if object_.direction == 0:
                    object_.rect.x = i.x + BLOCK_SIZE[0]
                    object_.rect.y = i.y
                elif object_.direction == 2:
                    object_.rect.x = i.x - BLOCK_SIZE[0]
                    object_.rect.y = i.y
                elif object_.direction == 1:
                    object_.rect.x = i.x
                    object_.rect.y = i.y - BLOCK_SIZE[1]
                else:
                    object_.rect.x = i.x
                    object_.rect.y = i.y + BLOCK_SIZE[1]
                if 'Ghost' in str(object_.__class__.__mro__):
                    if object_.direction == 0:
                        object_.eyes_rect.x = i.x + object_.size - object_.size // 3
                        object_.eyes_rect.y = i.y
                    elif object_.direction == 2:
                        object_.eyes_rect.x = i.x - object_.size
                        object_.eyes_rect.y = i.y
                    elif object_.direction == 1:
                        object_.eyes_rect.x = i.x - object_.size // 6
                        object_.eyes_rect.y = i.y - object_.size - object_.size // 3
                    else:
                        object_.eyes_rect.x = i.x - object_.size // 6
                        object_.eyes_rect.y = i.y + object_.size
                i.portal_check = False
