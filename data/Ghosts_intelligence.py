from data.Ghost import Ghost
from data.Pacman import Pacman
from data.VecFunctions import *


class RedGhost(Ghost):
    def __init__(self, width, height, x, y, screen, entity, speed):
        super().__init__(width, height, x, y, screen, entity, speed)
        self.std_dot = (224, 0)
        self.target_dot = (224, 0)

    def get_target_dot(self, pacman, red_ghost):
        pacman_pos = (pacman.tileX, pacman.tileY)
        self.target_dot = pacman_pos


class PinkGhost(Ghost):
    def __init__(self, width, height, x, y, screen, entity, speed):
        super().__init__(width, height, x, y, screen, entity, speed)
        self.std_dot = (0, 0)
        self.target_dot = (0, 0)

    def get_target_dot(self, pacman, red_ghost):
        pacman_pos = (pacman.tileX, pacman.tileY)
        pacman_vec = to_vec(pacman.direction)
        self.target_dot = plus(pacman_pos, multiply(pacman_vec, 4))


class BlueGhost(Ghost):
    def __init__(self, width, height, x, y, screen, entity, speed):
        super().__init__(width, height, x, y, screen, entity, speed)
        self.std_dot = (224, 224)
        self.target_dot = (224, 224)

    def get_target_dot(self, pacman, red_ghost):
        pacman_pos = (pacman.tileX, pacman.tileY)
        pacman_vec = to_vec(pacman.direction)
        self.target_dot = plus(
            red_ghost.pos,
            multiply(
                minus(
                    plus(
                        pacman_pos,
                        multiply(
                            pacman_vec,
                            2)),
                    red_ghost.pos),
                2))


class OrangeGhost(Ghost):
    def __init__(self, width, height, x, y, screen, entity, speed):
        super().__init__(width, height, x, y, screen, entity, speed)
        self.std_dot = (0, 224)
        self.target_dot = (0, 224)

    def get_target_dot(self, pacman, red_ghost):
        pacman_pos = (pacman.tileX, pacman.tileY)
        if dist(self.pos, pacman_pos) > 64:
            self.target_dot = pacman_pos
        else:
            self.target_dot = self.std_dot
