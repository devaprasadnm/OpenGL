from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math


r = 5


def clearscreen():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-100, 100.0, -100.0, 100.0)
    glPointSize(1.0)


def setpixel(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()


def update(value):
    global r
    glutPostRedisplay()
    glutTimerFunc(int(1000/60), update, int(1))
    r = r+5


def circle(xc, yc, r):
    x, y = 0, r

    while(x < y):
        x = x+0.1
        y = math.sqrt(r*r-x*x)

        setpixel(x+xc, y+yc)
        setpixel(-x+xc, y+yc)
        setpixel(-x+xc, -y+yc)
        setpixel(x+xc, -y+yc)
        setpixel(y+xc, x+yc)
        setpixel(-y+xc, x+yc)
        setpixel(-y+xc, -x+yc)
        setpixel(y+xc, -x+yc)


def display():
    global r

    circle(0, 0, r)
    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutCreateWindow("RIPPLE")
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(200, 200)
    glutDisplayFunc(display)
    glutTimerFunc(0, update, 0)
    clearscreen()
    glutMainLoop()


main()
