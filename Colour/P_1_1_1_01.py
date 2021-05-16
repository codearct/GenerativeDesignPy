if False:
    from Processing3 import *


def setup():
    size(800, 400)
    noStroke()
    colorMode(HSB, width, height, 100)


def draw():

    stepX = mouseX+2
    stepY = mouseY+2

    for gridX in range(0, width, stepX):
        for gridY in range(0, height, stepY):
            fill(gridX, height-gridY, 100)
            rect(gridX, gridY, stepX, stepY)
