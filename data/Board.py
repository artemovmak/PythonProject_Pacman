import pygame
from Constants import RESOLUTION

pygame.init()

screen = pygame.display.set_mode(RESOLUTION)

pygame.display.set_caption("Pacman")
clock = pygame.time.Clock()
name = []
font_to_print = 'Emulogic-zrEw.ttf'
point = 10000

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
        fontObj = pygame.font.Font(font, size)
        self.textSurfaceObj = fontObj.render(prt, True, color, fill_color)
        self.textRectObj = self.textSurfaceObj.get_rect()
        self.textRectObj.center = (cordinate_x, cordinate_y)

    def draw(self):
        screen.blit(self.textSurfaceObj, self.textRectObj)


# Установить заголовок окна
bl = True
# Основной цикл программы
with open('board.txt', 'r') as board:
    name.append(board.readline())
    name.append(board.readline())
    name.append(board.readline())

with open('board.txt', 'w') as board:
    board.write(name[0])
    board.write(name[1])
    board.write(name[2])
while bl:
    # Пользователь что-то сделал
    for event in pygame.event.get():
        # Реагируем на действия пользователя
        if event.type == pygame.QUIT:
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == ord('\r'):
                import Menu
    # Тут можно рисовать
    screen.fill(black)

    text(font_to_print, 80, 'Olymp:', RESOLUTION[0] // 2, 80, blue).draw()
    text(font_to_print, 80, str(name[0][0:-1]),
         RESOLUTION[0] // 2, 250, yellow).draw()
    text(font_to_print, 80, str(name[1][0:-1]),
         RESOLUTION[0] // 2, 400, yellow).draw()
    text(font_to_print, 80, str(name[2][0:-1]),
         RESOLUTION[0] // 2, 550, yellow).draw()
    text(font_to_print, 80, 'Back', RESOLUTION[0] // 2, 700, blue).draw()
    pygame.display.flip()
    clock.tick(30)
screen.fill(black)
pygame.quit()
