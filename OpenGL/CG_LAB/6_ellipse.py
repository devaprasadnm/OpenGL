from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math

def ClearScreen():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-100.0, 100.0, -100.0, 100.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 0.0)
    glPointSize(5.0)

def SetPixel(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()

#polar ellipse algo
def PolarEllipse(a,b,xc,yc):
    x,y=0,b
    angle = 0
    end_angle = (22/7)/2 

    while angle <= end_angle:
        angle += 0.001
        x =  a*math.cos(angle)
        y =  b*math.sin(angle)

  
        SetPixel(x+xc,y+yc)
        SetPixel(-x+xc,y+yc)
        SetPixel(-x+xc,-y+yc)
        SetPixel(x+xc,-y+yc)    

#non polar ellipse algorithm

def NonPolarEllipse(a,b,xc,yc):
    x,y=0,b
    xend=a

    while x<=xend:
        x += 0.01
        y= (math.sqrt(abs(1-((x*x)/(a*a)))))*b

        SetPixel(x+xc,y+yc)
        SetPixel(-x+xc,y+yc)
        SetPixel(-x+xc,-y+yc) 
        SetPixel(x+xc,-y+yc)    

def Main():
    print("Ellipse Drawing")
    a= float(input("Rx = "))
    b= float(input("Ry = "))
    xc= float(input("Xc = "))
    yc= float(input("Yc = "))
    choice = int(input("1) Polar Algorithm \n2) Non Polar Algorithm \n"))
    print("starting window....")

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(200, 200)
    glutCreateWindow("Ellipse")
    if choice == 1:
         glutDisplayFunc(lambda: PolarEllipse(a,b,xc,yc))

    elif choice== 2 :
         glutDisplayFunc(lambda: NonPolarEllipse(a,b,xc,yc))
    else:
        print("Invalid input")  
        exit()  

   
    ClearScreen()
    glutMainLoop()

Main()




