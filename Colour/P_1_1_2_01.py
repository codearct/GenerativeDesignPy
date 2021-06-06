if False:
    from Processing3 import *

segmentCount = 6


def setup():
    size(720, 720)
    noStroke()
    colorMode(HSB, 360, width, height)


def draw():
    translate(width/2, height/2)
    with beginShape(TRIANGLE_FAN):

        vertex(0, 0)

        radius = width/2
        angleStep = 360/segmentCount

        for angle in range(0, 361, angleStep):
            px = radius*cos(radians(angle))
            py = radius*sin(radians(angle))
            fill(angle, mouseX, mouseY)
            vertex(px, py)
    # endShape()


def keyPressed():
    global segmentCount
    if key == "1":
        segmentCount = 6
    elif key == "2":
        segmentCount = 12
    elif key == "3":
        segmentCount = 24
    elif key == "4":
        segmentCount = 45
    elif key == "5":
        segmentCount = 360
