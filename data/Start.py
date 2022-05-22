import pygame as pg
from data.Constants import RESOLUTION, MENU_FONT

pg.init()

screen = pg.display.set_mode(RESOLUTION)

pg.display.set_caption("Pacman")
clock = pg.time.Clock()
name = []

aqua = (0, 255, 255)   # морскаяволна
black = (0, 0, 0)   # черный
blue = (0, 0, 255)   # синий
fuchsia = (255, 0, 255)   # фуксия
gray = (128, 128, 128)   # серый
green = (0, 128, 0)   # зеленый
lime = (0, 255, 0)   # цвет лайма
maroon = (128, 0, 0)   # темно-бордовый
navy_blue = (0, 0, 128)   # темно-синий
olive = (128, 128, 0)   # оливковый
purple = (128, 0, 128)   # фиолетовый
red = (255, 0, 0)   # красный
silver = (192, 192, 192)   # серебряный
teal = (0, 128, 128)   # зелено-голубой
white = (255, 255, 255)   # белый
yellow = (255, 255, 0)   # желтый


class text:
    def __init__(self, font, size, prt, cordinate_x,
                 cordinate_y, color, fill_color=black):
        fontObj = pg.font.Font(font, size)
        self.textSurfaceObj = fontObj.render(prt, True, color, fill_color)
        self.textRectObj = self.textSurfaceObj.get_rect()
        self.textRectObj.center = (cordinate_x, cordinate_y)

    def draw(self):
        screen.blit(self.textSurfaceObj, self.textRectObj)


# Установить заголовок окна
open_window = True
# Основной цикл программы

while open_window:
    # Тут можно рисовать
    screen.fill(black)
    text(MENU_FONT, 80, 'SwiftTeam', RESOLUTION[0] // 2, 80, yellow).draw()
    text(MENU_FONT, 80, 'PACMAN', RESOLUTION[0] // 2, 400, yellow).draw()
    text(
        MENU_FONT,
        40,
        'PRESS       TO PLAY',
        RESOLUTION[0] // 2,
        700,
        yellow).draw()
    text(MENU_FONT, 40, 'ENTER', RESOLUTION[0] // 2 - 30, 700, blue).draw()
    pg.display.flip()

    # Пользователь что-то сделал
    for event in pg.event.get():
        # Реагируем на действия пользователя
        if event.type == pg.QUIT:
            open_window = False
        elif event.type == pg.KEYDOWN:
            if event.key == ord('\r'):
                open_window = False
            elif event.key == pg.K_ESCAPE:
                open_window = False

    clock.tick(30)

