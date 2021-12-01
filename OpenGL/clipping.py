from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*


def clearscreen():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-100, 100, -100, 100)
    glClear(GL_COLOR_BUFFER_BIT)

def setpixel(edges,points,rgb):
    glBegin(GL_LINES)
    glColor3f(rgb[0],rgb[1],rgb[2])
    for e in edges:
        for v in e:
            glVertex2fv(points[v])
    glEnd()
    glFlush()

def rectangle(x1,y1,x2,y2):
    edges = [
        [0,1],
        [1,2],
        [2,3],
        [3,0]
    ]

    points =[
      [x1,y2],
      [x2,y2],
      [x2,y1],
      [x1,y1]
    ]
    
    rgb = (1.0,1.0,1.0)
    setpixel(edges,points,rgb)

def line(x1,y1,x2,y2):

    edges = [
        [0,1],
       ]

    points=[
      [x1,y1],
      [x2,y2]  
    ]   
    rgb = (0.0,1.0,0.0)
    setpixel(edges,points,rgb) 



# ENCODE FUNCTION

INSIDE=0
LEFT=1
RIGHT=2
BOTTOM=4
TOP=8


def encode(x,y,xl,xr,yb,yt):
    region_code=INSIDE
    if x<xl:
        region_code = region_code|LEFT
    if x>xr:
        region_code=region_code|RIGHT
    if y<yb:
        region_code=region_code|BOTTOM
    if y>yt:
        region_code=region_code|TOP

    return region_code

   

# Cohen Sutherland 
def cohensutherland(x1,y1,x2,y2,xl,xr,yb,yt):
    rectangle(xl,yb,xr,yt)
    m = float()
    line(x1,y1,x2,y2)
    accept = False

      #step1
    r_code1=encode(x1,y1,xl,xr,yb,yt)
    r_code2=encode(x2,y2,xl,xr,yb,yt)

    while True:

      
        #step2 
        if r_code1==0 and r_code2  ==0:
            #to complete accceptance
            accept = True
            break
           

        #step3
        elif  r_code1 & r_code2 !=0:
            #to complete rejection
            break
        #step4
        else:
            if r_code1!=0:
                r_codeout=r_code1
            else:
                r_codeout=r_code2

            #intersection point in xl

            if r_codeout & TOP:
                x=(yt-y1)*(x2-x1)/(y2-y1)+x1
                y=yt      # x1,y1 are the intersecting point of y=yt line

            elif r_codeout &  BOTTOM:
                x=(yb-y1)*(x2-x1)/(y2-y1)+x1
                y=yb     # x1,y1 are the intersecting point of y=yb line 
 

            elif  r_codeout & LEFT:
                y=(xl-x1)*(y2-y1)/(x2-x1)+y1
                x=xl    # x1,y1 are the intersecting point of x=xl line 

            elif  r_codeout & RIGHT:
                y=(xr-x1)*(y2-y1)/(x2-x1)+y1
                x=xr    # x1,y1 are the intersecting point of x=xr line 

            

            if r_codeout == r_code1:
                x1, y1 = x, y
                r_code1 = encode(x,y,xl,xr,yb,yt)

            else:
                x2, y2 = x, y
                r_code2 = encode(x,y,xl,xr,yb,yt)

    #Here x1,y1 and x2,y2 are the clipped lines and we need to draw this line
    if accept:
        edges = [
          [0,1]
        ]
        points=[
            [x1,y1],
            [x2,y2]  
        ]   
        rgb = (0.0,0.0,1.0)
        setpixel(edges,points,rgb) 

    else:
        print("The given line cannot be clipped!")

def main():
    choice=0
   
    while(choice!=2):
        choice=int(input("Enter\n\t1.Plot a line \n\t2.exit\n"))
        if choice==1:
            x1=float(input('x1 Coordinate:'))
            y1=float(input("y1 Coordinate:"))
            x2=float(input('x2 Coordinate:'))    
            y2=float(input("y2 Coordinate:"))
            print("Window Boundary conditions")
            xl=float(input("Minimum value of x="))
            xr=float(input("Maximum value of x="))
            yb=float(input("Minimum value of y="))
            yt=float(input("Maximum value of y="))

            print("Starting window.....")
        
            glutInit()
            glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
            glutInitWindowSize(700,700)
            glutInitWindowPosition(0,0)
            glutCreateWindow("Line Clipping")
            glutDisplayFunc(lambda: cohensutherland(x1,y1,x2,y2,xl,xr,yb,yt))
            clearscreen()
            glutMainLoop()
        else:
            print("Invalid Choice")    
main()   



    




























