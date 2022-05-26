from data.Grid import Grid


class Wall(Grid):
    def __init__(self, width, height, x, y, screen, color):
        super().__init__(width, height, x, y, screen, color)
        self.collidable = True
