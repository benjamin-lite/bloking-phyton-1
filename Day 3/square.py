import turtle
def drawsquare ( ttl , x , y , length ):
    ttl.penup () # raise the pen
    ttl.goto (x , y) # move startying position
    ttl.setheading (0) # point turtle east
    ttl.pendown () # lower the pen 
    for count in range (4) : # draw 4 sides :
        ttl.forward ( length ) # move forward length ;
        ttl.right (90) # turn right 90 degrees
    ttl.penup () # raise the pen  

bob = turtle . Turtle () # our turtle is named bob 
bob.speed (10) # make bob crawl fast
bob.pensize (3) # line width  of pixels
drawsquare ( bob , 0, 0, 100) # draw a square at (0 ,0)
# with side length 100
turtle .  done () # keep drawing showing

