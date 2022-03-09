import turtle as tl
from random import randint
from time import sleep
from point import *
from bezier_curve import *

k = 200
    
tl.hideturtle()
tl.speed(0)

div = 100
def replay():

    b = Bezier()
    
    p0 = Point(randint(-k, k),randint(-k, k))
    p1 = Point(randint(-k, k),randint(-k, k))
    p2 = Point(randint(-k, k),randint(-k, k))
    p3 = Point(randint(-k, k),randint(-k, k))
    
    tl.penup()
    tl.goto(p0.x,p0.y)
    tl.pendown()
    tl.dot(10, 'blue')

    tl.penup()
    tl.goto(p1.x,p1.y)
    tl.pendown()
    tl.dot(10, 'red')

    tl.penup()
    tl.goto(p2.x,p2.y)
    tl.pendown()
    tl.dot(10, 'red')

    tl.penup()
    tl.goto(p3.x,p3.y)
    tl.pendown()
    tl.dot(10, 'blue')

    l1 = b.fromPoints(p0, p1)
    l2 = b.fromPoints(p1, p2)
    l3 = b.fromPoints(p2, p3,)

    m1 = b.fromBezier(l1, l2)
    m2 = b.fromBezier(l2, l3)

    n = b.fromBezier(m1, m2)

    tl.penup()
    tl.goto(p0.x,p0.y)
    tl.pendown()

    for d in range(div):
        p = n[d]
        tl.goto(p.x, p.y)


c = 220

for i in range(50):
    tl.clear()
    tl.penup()
    tl.goto(-c, c)
    tl.pendown()
    tl.goto(-c, -c)
    tl.goto(c, -c)
    tl.goto(c, c)
    tl.goto(-c, c)
    replay()
    sleep(1)