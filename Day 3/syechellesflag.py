import turtle
from PIL import image 
def save_as_jpg ( canvas , fileName ):
    # same as before 
    ...
def drawRectangle (ttl , x , y , width , height):
    """draw a rectangle of dimensions width and height ,  with upper """
    ttl . up ()
    ttl . goto (x , y)
    ttl . setheading (0)
    ttl . down ()
    for i in range (2):
        ttl . forward ( width )
        ttl . right (90)
        ttl . forward ( height )
        ttl . right (90)
    ttl . up ()
def drawTriangle (ttlo , x1 , y1 , x2 , y2 , x3 , y3):
    ttl . penup()
    ttl . goto ( x1 , y1 )
    ttl . pendown ()
    ttl . goto ( x2 , y2 )
    ttl . goto ( x3 , y3 )
    ttl . goto ( x1 , y1 )
    ttl . penup ()
def fillTriangel (ttl , x1 , y1 , x2 , y2 , x3 , y3 , color) :
    # this assumes color is given as a hex string value . 
    ttl . fillcolor ( color )
    ttl . begin_fill ()
    drawTriangle ( ttl , x1 , y1 , x2 , y2 , x3 , y3)
    ttl . end_fill ()
# set up the screen size (in pixels - 1000 x 1000)
# set the starting point the turtle (0 , 0)
turtle . setup (1500 , 1000 , 0 , 0)
Myblue = "#003882"
Myyellow = "#FCD647"
Myred = "#D12421"
mygreen = "#007336"
mywhite = "#FFFFFF"
joe = turtle . Turtle ()
joe . screen . colormode (225)
drawRectangle ( joe , 0 , 300 , 600 , 300)
joe = . goto (0 , 0)
#draw blue triangle
fillTriangel ( joe , 0, 0, 0 , 300 , 200 , 300 , Myblue)
#draw yellow triangle
fillTriangel ( joe , 0, 0, 200 , 300 , 400 , 300 , Myyellow)
#draw red triangle
fillTriangel ( joe , 0, 0, 400 , 300 , 600 , 300 , Myred)
#draw white triangle
fillTriangel ( joe , 0, 0, 600 , 300 , 600 , 150 , mywhite)
#draw green triangle
fillTriangel ( joe , 0, 0, 600 , 150 , 600 , 0 , mygreen)
joe . hideturtle ()
ts = turtle . getscreen ()
tc = ts . getcanvas ()
# creates a postscript image file
# substitute your own filename
tc . postscriptc( file = " SeychellesFlag . eps ")
# converts to JPEG 
save_as_jpg (tc ," SeychellesFlag ")
turtle . done ()



