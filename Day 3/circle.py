import turtle 

def tangentcircles(ttl):
    """print 10 tanghent circles."""
    r = 10 # initial radius
    n = 10 # count of crcles 

    for i in range(1, n + 1):
        ttl.circle(r * i)


def concentriccirrcle(ttl):
    """print 10 concentric circles."""
    r = 10 # initial radius 

    for i in range (1, 11):
        ttl.circle(r * i)
        ttl. up()
        ttl.sety(-(r * i))
        ttl.down()

ben = turtle.Turtle()

#tangentcircles (biru)

ben.up()
ben.goto(0, -150)
ben.down()
ben.pencolor("red")
concentriccirrcle (ben)

turtle.done