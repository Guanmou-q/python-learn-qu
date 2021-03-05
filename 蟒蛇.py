import turtle


def drawSnake(rad, angle, len, neckead):
    for i in range(len):
        turtle.circle(rad, angle)
        turtle.circle(-rad, angle)
    turtle.circle(rad, angle / 2)
    turtle.fd(rad)
    turtle.circle(neckead + 1, 180)
    turtle.fd(rad * 2 / 3)


def main():
    turtle.setup(1300, 800, 0, 0)
    pythonsize = 30
    turtle.pensize = 30
    turtle.pencolor("bule")
    turtle.seth(-40)
    drawSnake(40,80,5,pythonsize/2)
    main()

