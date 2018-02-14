#  File: Train.py
#  Description: use Turtle graphics to draw train

import math, turtle

def drawRect(t, x1, y1, x2, y2, color='blue', fill=False): # UL to LR
    if fill:
        t.fillcolor("#A9A9A9")
        t.begin_fill()
    drawLine(t, x1, y1, x2, y1, color=color)
    drawLine(t, x2, y1, x2, y2, color=color)
    drawLine(t, x2, y2, x1, y2, color=color)
    drawLine(t, x1, y2, x1, y1, color=color)
    if fill:
        t.end_fill()


def drawLine(t, x1, y1, x2, y2, color='blue'):
    t.pencolor(color)
    t.penup()
    t.goto (x1, y1)
    t.pendown()
    t.goto (x2, y2)
    t.penup()

def drawCircle(t, x, y, r, color='red'):
    t.color(color)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(r, steps=500)
    t.penup()

def drawSemiC(t, x, y, r, color='blue'):
    t.color(color)
    t.left(90)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(r, 180, steps=500)
    t.penup()
    t.seth(0)

def drawShape(t, x_list=[], y_list=[], color='blue'):
    t.color(color)
    for i in range(len(x_list)-1):
        drawLine(t, x_list[i], y_list[i], x_list[i+1], y_list[i+1])

def drawDots(t, x, y, color='black'):
    t.color(color)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.dot(6)
    t.penup()

def drawSpokes(t, x, y, r1, r2, color='red'):
        t.seth(0)
        t.penup()
        t.goto(x, y)
        t.right(5)
        for i in range(16):
            t.forward(r1)
            t.pendown()
            t.forward(r2-r1)
            t.penup()
            t.goto(x, y)
            if i%2==0:
                t.right(35)
            else:
                t.right(10)
        t.seth(0)

def drawBody(t, color='blue'):
    y = -105
    drawRect(t, -390, 154, -144, 142, color=color) # top roof
    drawLine(t, -366, 142, -366, y, color=color) # left
    drawLine(t, -166, 142, -166, y, color=color) # right
    drawRect(t, -340, 119, -280, 47, color=color, fill=True) # left window
    drawRect(t, -257, 119, -197, 47, color=color, fill=True) # right window
    # nose
    drawRect(t, -166, 92, 259, 5)
    drawRect(t, -52, 92, -40, 5)
    drawRect(t, 140, 92, 151, 5)
    drawLine(t, -166, -8, 259, -8)
    # top of nose
    drawRect(t, -30, 119, 41, 92)
    drawRect(t, -13, 130, 24, 119)
    drawShape(t, [125, 101, 114, 174, 187, 164], [92, 167, 190, 190, 167, 92])
    drawLine(t, 101, 167, 187, 167)
    # front of nose
    drawShape(t, [259, 259, 342, 307, 259], [-8, -133, -133, -73, -73])
    drawRect(t, 259, 68, 282, -62)
    drawRect(t, 282, 34, 294, -32)
    # bottom
    drawLine(t, -366, y, -340, y)
    drawSemiC(t, -340, y, -70)
    drawLine(t, -200, y, -110, y)
    drawSemiC(t, -110, y, -70)
    drawLine(t, 30, y, 82, y)
    drawSemiC(t, 82, y, -70)
    drawLine(t, 222, y, 259, y)
    # dots
    inc = 422/60
    for i in range(60):
        drawDots(t, -162+i*inc, -1)
    inc = 84/12
    for i in range(12):
        drawDots(t, -47, 11+i*inc)
    for i in range(12):
        drawDots(t, 145, 11+i*inc)

def drawWheels(t):
    x_coords = [-270, -40, 152]
    y0 = -160
    large_r = [50, 45, 45]
    small_r = [12, 10, 10]
    for num in range(3):
        for i in range(2):
            drawCircle(t, x_coords[num], y0-10*i, large_r[num]+10*i)
        drawCircle(t, x_coords[num], y0+large_r[num]-small_r[num], small_r[num])
        drawSpokes(t, x_coords[num], y0+large_r[num], small_r[num], large_r[num])

def drawRails(t, color='black'):
    drawLine(t, -390, -170, 391, -170, color=color)
    drawLine(t, -390, -182, 391, -182, color=color)
    for x in range(-378, 350, 60):
        drawRect(t, x, -182, x+24, -189, color=color)

def main():
    turtle.title ('Train')
    turtle.setup (800, 800, 0, 0)
    t = turtle.Turtle()
    t.pensize(2)
    t.speed(0)
    drawBody(t)
    drawWheels(t)
    drawRails(t)
    t.hideturtle()
    turtle.done()

main()
