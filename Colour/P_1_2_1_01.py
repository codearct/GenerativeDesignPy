if False:
    from Processing3 import *

tileCountX = 2
tileCountY = 10

colorLeft = []
colorRight = []

interpolateShortest = True


def setup():
    size(720, 720)
    noStroke()
    colorMode(HSB, 360, 100, 100, 100)
    shakeColors()


def draw():
    tileCountX = int(map(mouseX, 0, width, 2, 100))
    tileCountY = int(map(mouseY, 0, height, 2, 10))

    tileWidth = width/float(tileCountX)
    tileHeight = height/float(tileCountY)

    for gridY in range(tileCountY):
        col1 = colorLeft[gridY]
        col2 = colorRight[gridY]
        for gridX in range(tileCountX):
            amount = map(gridX, 0, tileCountX-1, 0, 1)
            if interpolateShortest:
                colorMode(RGB, 255, 255, 255, 255)
                interCol = lerpColor(col1, col2, amount)
                colorMode(HSB, 360, 100, 100, 100)
            else:
                interCol = lerpColor(col1, col2, amount)
            posX = tileWidth*gridX
            posY = tileHeight*gridY
            fill(interCol)
            rect(posX, posY, tileWidth, tileHeight)


def shakeColors():
    for i in range(tileCountY):
        colorLeft.append(color(random(0, 60), random(0, 100), 100))
        colorRight.append(color(random(160, 190), 100, random(0, 100)))
        colorLeft[i] = color(random(0, 60), random(0, 100), 100)
        colorRight[i] = color(random(160, 190), 100, random(0, 100))


def mouseReleased():
    shakeColors()


def keyPressed():
    global interpolateShortest
    if key == "1":
        interpolateShortest = True
    if key == "2":
        interpolateShortest = False
