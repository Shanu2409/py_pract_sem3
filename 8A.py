
import math


def circleArea(r):
    return math.pi*r*r


def squareArea(x):
    return x**2


def pointyShapeVolume(x, h, square):
    if square:
        base = squareArea(x)
    else:
        base = circleArea(x)
    return h*base/3.0


print(pointyShapeVolume(2, 3, True))
print(pointyShapeVolume(2, 4, False))
