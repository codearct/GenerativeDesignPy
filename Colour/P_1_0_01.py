if False:
    from Processing3 import *


def setup():
    size(720, 720)


def draw():
    colorMode(HSB, 360, 100, 100)
    background(mouseY/2, 100, 100)

    rectMode(CENTER)
    noStroke()

    fill(360-mouseY/2, 100, 100)
    rect(360, 360, mouseX+1, mouseX+1)
