class GameObject:
    def __init__(self, width, height, x, y, screen):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.rect = (self.x, self.y, self.width, self.height)
        self.screen = screen
        self.collidable = False
