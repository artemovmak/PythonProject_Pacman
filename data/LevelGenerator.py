import random
size = 32
a = [['0' for j in range(size)] for i in range(size)]
prev = [-1]


def draw_road_ver(gen_false, what_draw='0'):
    for i in range(size - 1):
        a[i][gen_false] = what_draw


def draw_road_gor(gen_false, what_draw='0'):
    for i in range(size - 1):
        a[gen_false][i] = what_draw

def do_true_num(num):
    for i in prev:
        if i == num + 1:
            num += 1
        elif i == num:
            num += 2
        elif i == num - 1:
            num -= 1
    if num >= size:
        num = size - 1
    return num


def shape_draw(gen_map):
    if gen_map == 0:
        built = 1
        built2 = size - 2
        for i in a[built:built2 + 1]:
            i[built] = 1
            i[built2] = 1
        for i in range(built, built2):
            a[built][i] = 1
        for i in range(built, built2):
            a[built2][i] = 1
    elif gen_map == 1:
        built = 3
        built2 = size - 4
        for i in a[built:built2 + 1]:
            i[built] = 1
            i[built2] = 1
        for i in range(built, built2):
            a[built][i] = 1
        for i in range(built, built2):
            a[built2][i] = 1
    elif gen_map == 2:
        built = 5
        built2 = size - 6
        for i in a[built:built2 + 1]:
            i[built] = 1
            i[built2] = 1
        for i in range(built, built2):
            a[built][i] = 1
        for i in range(built, built2):
            a[built2][i] = 1
    elif gen_map == 3:
        built = 7
        built2 = size - 8
        for i in a[built:built2 + 1]:
            i[built] = 1
            i[built2] = 1
        for i in range(built, built2):
            a[built][i] = 1
        for i in range(built, built2):
            a[built2][i] = 1
    elif gen_map == 4:
        for i in range(0, 5):
            rand = do_true_num(random.randint(0, size - 1))
            draw_road_gor(rand, '1')
            prev.append(rand)
    elif gen_map == 5:
        for i in range(0, 5):
            rand = do_true_num(random.randint(0, size - 1))
            draw_road_ver(rand, '1')
            prev.append(rand)


def draw_true_wall():
    for i in range(size - 1):
        for j in range(size - 1):
            if a[i][j] == 1 and a[i - 1][j] == 1 and a[i][j - 1] == 1:
                a[i][j] = 4  # 4 #'-|'
            elif a[i][j] == 1 and a[i + 1][j] == 1 and a[i][j - 1] == 1:
                a[i][j] = 3  # 3 '_|'
            elif a[i][j] == 1 and a[i - 1][j] == 1 and a[i][j + 1] == 1:
                a[i][j] = 5  # 5 '|-'
            elif a[i][j] == 1 and a[i + 1][j] == 1 and a[i][j + 1] == 1:
                a[i][j] = 2  # 2 '|_'


generate = set()
while(len(generate) < 4):
    generate.add(random.randint(0, 5))
for i in generate:
    shape_draw(i)
draw_true_wall()
prev = [-1]
for i in range(4):
    rand_num = do_true_num(random.randint(0, size - 1))
    draw_road_ver(rand_num)
    prev.append(rand_num)
for i in range(4):
    rand_num = do_true_num(random.randint(0, size - 1))
    draw_road_gor(rand_num)
    prev.append(rand_num)
with open('map.txt', 'w+') as out:
    for j in a:
        for k in j:
            out.write(str(k))
            print(k, end=" ")
        out.write("\n")
        print()
