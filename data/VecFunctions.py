def plus(a, b):
    return a[0] + b[0], a[1] + b[1]


def minus(a, b):
    return a[0] - b[0], a[1] - b[1]


def multiply(a, b):
    return a[0] * b, a[1] * b


def dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def to_vec(a):
    if a == 0:
        return 1, 0
    elif a == 1:
        return 0, 1
    elif a == 2:
        return -1, 0
    elif a == 3:
        return 0, -1
