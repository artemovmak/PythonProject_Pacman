import pygame as pg

from Constants import RESOLUTION
from MovingEntity import MovingEntity
from VecFunctions import *


class Ghost(MovingEntity):
    def __init__(self, width, height, x, y, screen, entity, speed):
        super().__init__(width, height, x, y, screen)
        self.collidable = True
        self.size = (width + height) // 2
        self.pos = (x // 24, y // 24)
        self.vec = (0, 1)
        self.std_dot = (0, 0)
        self.target_dot = (0, 0)
        if entity == 0:
            self.imgs_arr = [
                pg.image.load('sprites/pink.png'),
                pg.image.load('sprites/pink1.png')]
        elif entity == 1:
            self.imgs_arr = [
                pg.image.load('sprites/red.png'),
                pg.image.load('sprites/red1.png')]
        elif entity == 2:
            self.imgs_arr = [
                pg.image.load('sprites/yellow.png'),
                pg.image.load('sprites/yellow1.png')]
        else:
            self.imgs_arr = [
                pg.image.load('sprites/tur.png'),
                pg.image.load('sprites/tur1.png')]

        for i in range(0, len(self.imgs_arr)):
            self.imgs_arr[i] = pg.transform.scale(
                self.imgs_arr[i], (width, height))
        self.img_original_arr = self.imgs_arr

        self.eyes_arr = [
            pg.image.load("sprites/eyesLR.png"),
            pg.image.load("sprites/eyesUD.png"),
            pg.image.load("sprites/eyesLR.png"),
            pg.image.load("sprites/eyesUD.png")]
        self.eyes_arr[1] = pg.transform.flip(self.eyes_arr[1], False, True)
        self.eyes_arr[2] = pg.transform.flip(self.eyes_arr[2], True, False)
        for i in range(0, len(self.eyes_arr)):
            self.eyes_arr[i] = pg.transform.scale(
                self.eyes_arr[i], (width + width // 4, height + width // 4))

        self.rect = self.imgs_arr[0].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.eyes_rect_original = self.eyes_arr[0].get_rect()
        self.eyes_rect = self.eyes_rect_original
        self.eyes_rect.x = x
        self.eyes_rect.y = y
        self.direction = 0  # 1, 2, 3, 4 => 0, 90, 180, 270
        self.mouth_state = 0
        self.speed = speed

    def change_mouth(self):
        self.mouth_state = 0 if self.mouth_state == 1 else 1

    def draw(self):
        self.screen.blit(self.imgs_arr[self.mouth_state], self.rect)
        self.screen.blit(self.eyes_arr[self.direction], self.eyes_rect)

    def get_target_dot(self):
        pass

    def move(self, TICK, collide):
        if not collide:
            if self.direction == 0:
                if self.rect.x + \
                        self.rect[2] < RESOLUTION[0] or self.portal_check:
                    self.rect.x += self.speed
                    self.eyes_rect.x += self.speed
            elif self.direction == 1:
                if self.rect.y > 0 or self.portal_check:
                    self.rect.y -= self.speed
                    self.eyes_rect.y -= self.speed
            elif self.direction == 2:
                if self.rect.x > 0 or self.portal_check:
                    self.rect.x -= self.speed
                    self.eyes_rect.x -= self.speed
            elif self.direction == 3:
                if self.rect.y + \
                        self.rect[3] < RESOLUTION[1] or self.portal_check:
                    self.rect.y += self.speed
                    self.eyes_rect.y += self.speed
        if TICK % 7 == 0:
            self.change_mouth()

    def get_direction(self, map):
        self.pos = (self.tileX, self.tileY)
        next_dots = [plus(self.pos, (0, 1)), plus(self.pos, (1, 0)), plus(
            self.pos, (0, -1)), plus(self.pos, (-1, 0))]
        correct_dots = []
        previous_dot = minus(self.pos, self.vec)
        for dot in next_dots:
            if (not map[dot[1]][dot[0]]) and (dot != previous_dot):
                correct_dots.append(dot)
        min_dot = correct_dots[0]
        for dot in correct_dots:
            if dist(dot, self.target_dot) < dist(min_dot, self.target_dot):
                min_dot = dot
        if min_dot == plus(self.pos, (0, 1)):
            self.vec = (0, 1)
            return 3
        elif min_dot == plus(self.pos, (1, 0)):
            self.vec = (1, 0)
            return 0
        elif min_dot == plus(self.pos, (0, -1)):
            self.vec = (0, -1)
            return 1
        elif min_dot == plus(self.pos, (-1, 0)):
            self.vec = (-1, 0)
            return 2
        else:
            pass

    def change_direction(self, direction):
        if direction != self.direction:
            self.direction = direction
            if self.direction == 0:
                self.eyes_rect.x = self.rect.x - self.size // 3
                self.eyes_rect.y = self.rect.y
            elif self.direction == 1:
                self.eyes_rect.x = self.rect.x - self.size // 6
                self.eyes_rect.y = self.rect.y - self.size // 3
            elif self.direction == 2:
                self.eyes_rect.x = self.rect.x
                self.eyes_rect.y = self.rect.y
            elif self.direction == 3:
                self.eyes_rect.x = self.rect.x - self.size // 6
                self.eyes_rect.y = self.rect.y - self.size // 12
