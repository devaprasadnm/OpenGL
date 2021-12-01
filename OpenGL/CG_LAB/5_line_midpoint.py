from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def ClearScreen():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-100.0, 100.0, -100.0, 100.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 1.0)
    glPointSize(5.0)


def SetPixel(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()


def MidPointLine(x1, y1, x2, y2):
    if x2 > x1:
        x, y, xend = x1, y1, x2
        dx, dy = x2-x1, y2-y1
    else:
        x, y, xend = x2, y2, x1
        dx, dy = x1-x2, y1-y2

    SetPixel(x, y)
    P = dy-dx/2

    while x < xend:
        x = x+1
        if P < 0:
            P += dy
        else:
            y = y+1
            P += dy-dx
        SetPixel(x, y)

def Main():
     choice =0 
     while choice != 2:
        choice = int(input("Enter \n1) Plot a Line \n2) exit \n"))
        if choice ==1:
             x1 = float(input("X1 Co-ordinate:"))
             y1 = float(input("Y1 Co-ordinate:"))
             x2 = float(input("X2 Co-ordinate:"))
             y2 = float(input("Y2 Co-ordinate:"))
             print("starting window....")
             glutInit()
             glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
             glutInitWindowSize(500, 500)
             glutInitWindowPosition(200, 200)
             glutCreateWindow("Lin using Midpoint-Algorithm")
             glutDisplayFunc(lambda:MidPointLine(x1, y1, x2, y2))
             ClearScreen()
             glutMainLoop()

        else :
            print("Invalid Choice")


Main()
