import pygame as pg

from data.Constants import RESOLUTION, BLOCK_SIZE
from data.MovingEntity import MovingEntity
from time import sleep
from pygame.transform import scale


class Pacman(MovingEntity):
    def __init__(self, width, height, x, y, screen, speed):
        super().__init__(width, height, x, y, screen)
        self.speed = speed
        self.collidable = True

        self.imgs_arr = [
            pg.image.load('../PythonProject_Pacman/sprites/open.png'),
            pg.image.load('../PythonProject_Pacman/sprites/half.png'),
            pg.image.load('../PythonProject_Pacman/sprites/little.png'),
            pg.image.load('../PythonProject_Pacman/sprites/closed.png')]
        for i in range(0, len(self.imgs_arr)):
            self.imgs_arr[i] = pg.transform.scale(
                self.imgs_arr[i], (width, height))
        self.img_original_arr = self.imgs_arr
        self.rect = self.imgs_arr[0].get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.direction = 0
        self.mouth_state = 0
        self.img = self.imgs_arr[self.mouth_state]

    def change_mouth(self):
        if self.mouth_state != 3:
            self.mouth_state += 1
        else:
            self.mouth_state = 0
        self.img = self.imgs_arr[self.mouth_state]

    def draw(self):
        self.screen.blit(self.img, self.rect)

    def move(self, TICK, collide):
        if not collide:
            if self.direction == 0:
                if self.rect.x + \
                        self.rect[2] < RESOLUTION[0] or self.portal_check:
                    self.rect.x += self.speed
            elif self.direction == 1:
                if self.rect.y > 0 or self.portal_check:
                    self.rect.y -= self.speed
            elif self.direction == 2:
                if self.rect.x > 0 or self.portal_check:
                    self.rect.x -= self.speed
            elif self.direction == 3:
                if self.rect.y + \
                        self.rect[3] < RESOLUTION[1] or self.portal_check:
                    self.rect.y += self.speed
            if TICK % 4 == 0:
                self.change_mouth()
        else:
            self.mouth_state = 3
        self.img = pg.transform.rotate(
            self.img_original_arr[self.mouth_state], self.direction * 90)

    def collideGhost(self, ghost_pos):
        if ghost_pos[0] == self.tileX:
            if ghost_pos[1] == self.tileY:
                return True
        else:
            return False

    def change_direction(self, direction):
        if direction != self.direction:
            self.direction = direction
            self.img = pg.transform.rotate(
                self.img_original_arr[self.mouth_state], self.direction * 90)

    def eat(self, arr):
        pos = [(self.rect.x + self.width // 2) // BLOCK_SIZE[0],
               (self.rect.y + self.height // 2) // BLOCK_SIZE[1]]
        if arr[pos[1]][pos[0]].has_seed:
            arr[pos[1]][pos[0]].has_seed = False
            return True
        else:
            return False

    def death(self, n, arr, ghosts, screen, size):
        for i in arr:
            for j in i:
                j.draw()
        for ghost in ghosts:
            ghost.draw()
        img = pg.image.load("sprites/dead/death" + str(n) + ".png")
        img = scale(img, size)
        screen.blit(img, self.rect)
        pg.display.flip()
        sleep(0.1)
