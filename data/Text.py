class text:
    def __init__(self, font, size, prt, cordinate_x,
                 cordinate_y, color, fill_color=black):
        fontObj = pg.font.Font(font, size)
        self.textSurfaceObj = fontObj.render(prt, True, color, fill_color)
        self.textRectObj = self.textSurfaceObj.get_rect()
        self.textRectObj.center = (cordinate_x, cordinate_y)

    def draw(self, screen):
        screen.blit(self.textSurfaceObj, self.textRectObj)
