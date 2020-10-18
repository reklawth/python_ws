from math import ceil, pi

def circle_circumference(radius):
    initial = 2 * pi * radius
    return ceil(initial * 100) / 100


def circle_area(radius):
    initial = pi * radius ** 2
    return ceil(initial * 100) / 100
