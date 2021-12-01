from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *



def ClearScreen():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-100.0, 100.0, -100.0, 100.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 0.0)
    glPointSize(2.0)


def SetPixel(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()


def BresenhamLine(x1, y1, x2, y2):

    if x2 > x1:
        x, y, xend = x1, y1, x2
        dx, dy = x2-x1, y2-y1
    else:
        x, y, xend = x2, y2, x1
        dx, dy = x1-x2, y1-y2

    SetPixel(x, y)
    P = 2*dy-dx

    while x < xend:
        x = x+1
        if P < 0:
            P += 2*dy
        else:
            y = y+1
            P += 2*dy-2*dx
        SetPixel(x, y)


def Main():

    choice = 0
    while choice != 2:
        choice = int(input("Enter \n1) Plot a Line \n2) exit \n"))
        if choice ==1:
             x1 = float(input("X1 Co-ordinate:"))
             y1 = float(input("Y1 Co-ordinate:"))
             x2 = float(input("X2 Co-ordinate:"))
             y2 = float(input("Y2 Co-ordinate:"))
             print("starting window....")
            
             glutInit(sys.argv)
             glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
             glutInitWindowSize(500, 500)
             glutInitWindowPosition(200, 200)
             glutCreateWindow("Bresenham_Algorithm")
             glutDisplayFunc(lambda: BresenhamLine(x1, y1, x2, y2))
             glutIdleFunc(lambda: BresenhamLine(x1, y1, x2, y2))
             ClearScreen()
             glutMainLoop()
        else :
            print("Invalid Choice")
        

Main()
