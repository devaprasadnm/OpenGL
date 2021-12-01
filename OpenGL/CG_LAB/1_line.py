from OpenGL.GL import *
from OpenGL.GLU import *     
from OpenGL.GLUT import *    
import sys
import math



def clearScreen():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-1.0, 1.0,-1.0,1.0)


def horizontal():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,1.0,0.0)
    glPointSize(10.0)
    glBegin(GL_LINES)       
    glVertex2f(x1, y)
    glVertex2f(x2, y) 
    glEnd()
    glFlush()
 
def vertical():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,1.0,0.0)
    glPointSize(10.0)
    glBegin(GL_LINES)       
    glVertex2f(x, y1)
    glVertex2f(x, y2) 
    glEnd()
    glFlush()


def diagonal():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,1.0,0.0)
    glPointSize(10.0)
    glBegin(GL_LINES)       
    glVertex2f(a, a)
    glVertex2f(b, b) 
    glEnd()
    glFlush()



s=int(input("Enter\n 1 for horizontal line \n 2 for vertical line\n 3 for diagonal line\n"))
if s==1:
    x1 = float(input('Enter x1 value : '))/100
    x2 = float(input('Enter x2 value : '))/100
    y = float(input('Enter y value : '))/100

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("Horizontal Line")
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutDisplayFunc(horizontal)
    clearScreen()
    glutMainLoop()
elif s==2:
    x = float(input('Enter x value : '))/100
    y2 = float(input('Enter y2 value : '))/100
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("Vertical Line")
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutDisplayFunc(vertical)
    clearScreen()
    glutMainLoop()
elif s==3:
    a = float(input('Enter a value : '))/100
    b = float(input('Enter b value : '))/100
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("Diagonal")
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutDisplayFunc(diagonal)
    clearScreen()
    glutMainLoop()

        

    
    