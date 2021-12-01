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

# MidPointCircle_Method

def MidPointCircle(r, xc, yc):
    x, y = 0, r
    SetPixel(x+xc, y+yc)
    SetPixel(x+xc, -y+yc)
    SetPixel(y+xc, x+yc)
    SetPixel(-y+xc, x+yc)
    p = 5/4-r
    while x < y:
        x = x+1
        if p < 0:
            p = p+2*x+1
        else:
            y = y - 1
            p = p+2*x-2*y+1
        SetPixel(x+xc, y+yc)
        SetPixel(-x+xc, y+yc)
        SetPixel(-x+xc, -y+yc)
        SetPixel(x+xc, -y+yc)
        SetPixel(y+xc, x+yc)
        SetPixel(-y+xc, x+yc)
        SetPixel(-y+xc, -x+yc)
        SetPixel(y+xc, -x+yc)

#PolarCircle_Method

def PolarCircle(r,xc,yc):
    x,y=0,r
    angle = 0
    end_angle = (22/7)/4 

    while angle <= end_angle:
        angle += 0.001
        x =  r*math.cos(angle)
        y =  r*math.sin(angle)

        SetPixel(x+xc, y+yc)
        SetPixel(-x+xc, y+yc)
        SetPixel(-x+xc, -y+yc)
        SetPixel(x+xc, -y+yc)
        SetPixel(y+xc, x+yc)
        SetPixel(-y+xc, x+yc)
        SetPixel(-y+xc, -x+yc)
        SetPixel(y+xc, -x+yc)

#NonPolarCircle_Method

def NonPolarCircle(r,xc,yc):
    x,y=0,r

    while x <= y:
        y -= 0.01
        x =  math.sqrt(r*r-y*y)

        SetPixel(x+xc, y+yc)
        SetPixel(-x+xc, y+yc)
        SetPixel(-x+xc, -y+yc)
        SetPixel(x+xc, -y+yc)
        SetPixel(y+xc, x+yc)
        SetPixel(-y+xc, x+yc)
        SetPixel(-y+xc, -x+yc)
        SetPixel(y+xc, -x+yc)
  


def Main():
    choice = 0
    while choice != 4:
        choice=int(input("Choose the Algorithm \n 1)Mid_Point Algorithm \n 2)Polar Algorithm \n 3)NonPolar Algorithm\n 4)exit \n"))
        if choice==1 or choice==2 or choice==3:
            r = float(input("Enter the Radius"))
            print("Enter the Center of the Circle")
            c1 = float(input("xc = "))
            c2 = float(input("yc = ")) 
            print("starting window....") 
    
            glutInit()
            glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
            glutInitWindowSize(500, 500)
            glutInitWindowPosition(200, 200)
            glutCreateWindow("Circle")
            if choice ==1:
                glutDisplayFunc(lambda :MidPointCircle(r, c1, c2))
            if choice ==2:
                glutDisplayFunc(lambda :PolarCircle(r, c1, c2))
            if choice ==3:
                glutDisplayFunc(lambda :NonPolarCircle(r, c1, c2))
            ClearScreen()
            glutMainLoop()
        else :
            print("Invalid Choice")



Main()
