import pygame as pg
from Constants import *
from Wall import Wall
from Grid import Grid
from sys import exit
from Pacman import Pacman
import copy
from Ghosts_intelligence import *
from time import sleep
from Portals import Portal

pg.init()
screen = pg.display.set_mode(RESOLUTION)
pg.font.init()
clock = pg.time.Clock()
font = pg.font.Font('Emulogic-zrEw.ttf', 50)


def GetMatrixFromFile(file_name):
    arr = []
    with open(file_name, 'r', encoding="utf-8") as file:
        lines = file.readlines()
        lines = [i.replace('\n', '') for i in lines]
        for i in range(0, len(lines)):
            arr.append([])
            for j in lines[i]:
                if j == "0":
                    arr[i].append(0)
                elif j == "1":
                    arr[i].append(1)
    return arr


def FillMatrix(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            if arr[i][j] == 1:
                arr[i][j] = Wall(
                    BLOCK_SIZE[0],
                    BLOCK_SIZE[1],
                    BLOCK_SIZE[0] * j,
                    BLOCK_SIZE[1] * i,
                    screen,
                    WHITE)
            elif arr[i][j] == 0:
                arr[i][j] = Grid(
                    BLOCK_SIZE[0],
                    BLOCK_SIZE[1],
                    BLOCK_SIZE[0] * j,
                    BLOCK_SIZE[1] * i,
                    screen,
                    BLACK)
                arr[i][j].has_seed = True
            else:
                exit("FATAL ERROR AT READING FILE")
    return arr


START_MUSIC = pg.mixer.Sound(START_SOUND)
END_MUSIC = pg.mixer.Sound(END_SOUND)


##########################################################################


where_kursor = 0
MENU_RUNNING = True

aqua = (0, 255, 255)   # морская волна
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
                 cordinate_y, color, fill_color=BLACK):
        fontObj = pg.font.Font(font, size)
        self.textSurfaceObj = fontObj.render(prt, True, color, fill_color)
        self.textRectObj = self.textSurfaceObj.get_rect()
        self.textRectObj.center = (cordinate_x, cordinate_y)

    def draw(self):
        screen.blit(self.textSurfaceObj, self.textRectObj)


# Установить заголовок окна
pg.display.set_caption("Pacman the best game")


##########################################################################
name = []


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

##########################################################################

waka_sound = pg.mixer.Sound(WAKA_SOUND)
Lives = PACMAN_MAX_LIVES
while MAIN_RUNNING:
    while GAME_RUNNING:

        if TICK == 0:
            if Lives == PACMAN_MAX_LIVES:
                map = GetMatrixFromFile("map.txt")
                arr = copy.deepcopy(map)
                arr = FillMatrix(arr)

            portals = [
                Portal(
                    BLOCK_SIZE[0],
                    BLOCK_SIZE[1],
                    0,
                    BLOCK_SIZE[1] * 15,
                    screen,
                    1,
                    2),
                Portal(
                    BLOCK_SIZE[0],
                    BLOCK_SIZE[1],
                    BLOCK_SIZE[0] * 31,
                    BLOCK_SIZE[1] * 15,
                    screen,
                    2,
                    1)]  # порталы
            pacman = Pacman(
                PACMAN_SIZE[0],
                PACMAN_SIZE[0],
                PACMAN_START_POSITION[0] *
                BLOCK_SIZE[0],
                PACMAN_START_POSITION[1] *
                BLOCK_SIZE[1],
                screen,
                PACMAN_SPEED)
            ghosts = []
            Score = SCORE
            DIRECTIONS = {pg.K_d: 0, pg.K_w: 1, pg.K_a: 2, pg.K_s: 3}
            command = None
            pause = False
            ghosts.append(
                RedGhost(
                    GHOST_SIZE[0],
                    GHOST_SIZE[0],
                    RED_GHOST_START_POS[0] *
                    BLOCK_SIZE[0],
                    RED_GHOST_START_POS[1] *
                    BLOCK_SIZE[1],
                    screen,
                    1,
                    GHOST_SPEED))
            ghosts.append(
                PinkGhost(
                    GHOST_SIZE[0],
                    GHOST_SIZE[0],
                    PINK_GHOST_START_POS[0] *
                    BLOCK_SIZE[0],
                    PINK_GHOST_START_POS[1] *
                    BLOCK_SIZE[1],
                    screen,
                    0,
                    GHOST_SPEED))
            ghosts.append(
                BlueGhost(
                    GHOST_SIZE[0],
                    GHOST_SIZE[0],
                    BLUE_GHOST_START_POS[0] *
                    BLOCK_SIZE[0],
                    BLUE_GHOST_START_POS[1] *
                    BLOCK_SIZE[1],
                    screen,
                    3,
                    GHOST_SPEED))
            ghosts.append(
                OrangeGhost(
                    GHOST_SIZE[0],
                    GHOST_SIZE[0],
                    ORANGE_GHOST_START_POS[0] *
                    BLOCK_SIZE[0],
                    ORANGE_GHOST_START_POS[1] *
                    BLOCK_SIZE[1],
                    screen,
                    2,
                    GHOST_SPEED))
            red_ghost = ghosts[0]

        pg.display.set_caption("Pacman - Game")
        clock.tick(60)

        for i in range(0, len(ghosts)):
            if pacman.collideGhost(ghosts[i].CountTile()):
                END_MUSIC.play()
                for i in range(1, 18):
                    pacman.death(i, arr, ghosts, screen, PACMAN_SIZE)
                sleep(0.5)
                print(Lives)
                Lives -= 1
                TICK = -1
                continue

        if Lives < 1:
            GAME_RUNNING = False
            MENU_RUNNING = True

        key = pg.key.get_pressed()

        if key[pg.K_a] or key[pg.K_d] or key[pg.K_w] or key[pg.K_s]:
            command = key
        if key[pg.K_p]:
            pause = True
            while pause:
                for e in pg.event.get():
                    if e.type == pg.QUIT:
                        GAME_RUNNING = False
                        MENU_RUNNING = True
                    if e.type == pg.KEYDOWN:
                        pause = False
        if command is not None:
            for direction_key in DIRECTIONS:
                direction_value = DIRECTIONS[direction_key]

                if command[direction_key]:
                    if not pacman.collideWall(
                            direction_value, arr) and pacman.rect.x % 24 == 0 and pacman.rect.y % 24 == 0:
                        pacman.change_direction(direction_value)
                        command = None
                        break
        for ghost in ghosts:
            if ghost.rect.x % 24 == 0 and ghost.rect.y % 24 == 0:
                ghost.CountTile()
                ghost.pos = (ghost.tileX, ghost.tileY)
                ghost.get_target_dot(pacman, ghosts[0])  # Red ghost
                ghost.change_direction(ghost.get_direction(map))
                ghost.move(TICK, 0)
            else:
                ghost.CountTile()
                ghost.pos = (ghost.tileX, ghost.tileY)
                ghost.move(TICK, 0)
        pacman.CountTile()
        pacman.move(TICK, pacman.collideWall(pacman.direction, arr))

        [i.colideTeleport([pacman] + ghosts, portals)
         for i in portals]  # порталы

        screen.fill(BLACK)

        if pacman.eat(arr):
            waka_sound.play()
            Score += 100
            print(Score)

        for i in arr:
            for j in i:
                j.draw()

        pacman.draw()
        for ghost in ghosts:
            ghost.draw()
        pg.display.flip()

        if TICK == 0:
            START_MUSIC.play()
            sleep(5)

        TICK += 1

        if Score == TARGET_SCORE:
            TICK = 0
            sleep(2)
            GAME_RUNNING = False
            MENU_RUNNING = True

        for e in pg.event.get():
            if e.type == pg.QUIT:
                GAME_RUNNING = False
                MENU_RUNNING = True
            elif e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE:
                GAME_RUNNING = False
                MENU_RUNNING = True
                TICK = 0

    # Основной цикл программы
    while MENU_RUNNING:
        pg.display.set_caption("Pacman - Menu")
        # Пользователь что-то сделал
        for event in pg.event.get():
            # Реагируем на действия пользователя
            if event.type == pg.QUIT:
                MAIN_RUNNING = False
                MENU_RUNNING = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    where_kursor = (where_kursor - 1) % 3
                elif event.key == pg.K_DOWN:
                    where_kursor = (where_kursor + 1) % 3
                elif event.key == pg.K_ESCAPE:
                    MAIN_RUNNING = False
                    MENU_RUNNING = False
                elif event.key == ord('\r'):
                    if where_kursor == 0:
                        GAME_RUNNING = True
                        MENU_RUNNING = False
                    elif where_kursor == 1:
                        BOARD_RUNNING = True
                        MENU_RUNNING = False
                    elif where_kursor == 2:
                        MAIN_RUNNING = False
                        MENU_RUNNING = False

        # Тут можно рисовать
        screen.fill(black)
        text(MENU_FONT, 80, 'Pacman', RESOLUTION[0] // 2, 70, blue).draw()
        text(
            MENU_FONT,
            80,
            'Play',
            RESOLUTION[0] //
            2,
            280,
            yellow if abs(where_kursor) != 0 else aqua).draw()
        text(
            MENU_FONT,
            65,
            'Score Board',
            RESOLUTION[0] // 2,
            460,
            yellow if abs(where_kursor) != 1 else aqua).draw()
        text(
            MENU_FONT,
            80,
            'Exit',
            RESOLUTION[0] // 2,
            700,
            blue if abs(where_kursor) != 2 else red).draw()

        # Рисунок появится после обновления экрана
        pg.display.flip()

        # Экран будет перерисовываться 30 раз в секунду
        clock.tick(30)

    while BOARD_RUNNING:
        pg.display.set_caption("Pacman - Board")
        # Пользователь что-то сделал
        for event in pg.event.get():
            # Реагируем на действия пользователя
            if event.type == pg.QUIT:
                BOARD_RUNNING = False
                MENU_RUNNING = True
            elif event.type == pg.KEYDOWN:
                if event.key == ord('\r'):
                    MENU_RUNNING = True
                    BOARD_RUNNING = False
        # Тут можно рисовать
        screen.fill(black)

        text(MENU_FONT, 80, 'Olymp:', RESOLUTION[0] // 2, 80, blue).draw()
        text(MENU_FONT, 80, str(name[0][0:-1]),
             RESOLUTION[0] // 2, 250, yellow).draw()
        text(MENU_FONT, 80, str(name[1][0:-1]),
             RESOLUTION[0] // 2, 400, yellow).draw()
        text(MENU_FONT, 80, str(name[2][0:-1]),
             RESOLUTION[0] // 2, 550, yellow).draw()
        text(MENU_FONT, 80, 'Back', RESOLUTION[0] // 2, 700, blue).draw()
        pg.display.flip()
        clock.tick(30)

pg.quit()
