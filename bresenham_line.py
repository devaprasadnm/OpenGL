from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
print("Packages imported successfully")


def clearscreen():  # clears the windows
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-20.0, 20.0, -20.0, 20.0)


def plot_points(x,y):
    print("in points")
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 0.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()
    glFlush()


def Bresenham_algo(x1, y1, x2, y2):
    print('in algo')
    x = x1
    y = y1
    dx,dy = abs(x2-x1),abs(y2-y1)
    plot_points(x, y)
    p = 2*dy - dx
    if dx > dy:
        while x < x2:
          x = x+1
          if p < 0:
              p = p+2*dy
          else: 
              y=y+1
              p = p+2*dy - 2*dx
        plot_points(x, y)

    else:
        while y<y2:
            y=y+1
            if p<0:
                p=p+2*dx
            else:
                 x=x+1
                 p=p+2*dx-2*dy
        plot_points(x, y)

def Display():
    x1=float(input('Enter Coordinate X1 :'))
    x2=float(input('Enter Coordinate X2 :'))
    y1=float(input('Enter Coordinate Y2 :'))
    y2=float(input('Enter Coordinate Y2 :'))
    Bresenham_algo(x1,y1,x2,y2)
    print('ended')

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutCreateWindow("Bresenham Algorithm")
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    clearscreen()
    glutDisplayFunc(Display)
    glutMainLoop()


main()
