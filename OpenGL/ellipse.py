from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import math

def clearscreen():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-100, 100, -100, 100)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 1.0)
    glPointSize(5.0)    
    


def setpixel(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()


def ellipse_midpoint( rx, ry , xc, yc):
    x, y = 0, ry
    p1 = ((ry * ry) - (rx * rx * ry) +(0.25 * rx * rx))
    dx = 2*ry*ry*x
    dy = 2*rx*rx*y


    while (dx < dy):
        setpixel(x+xc, y+yc)
        setpixel(-x+xc, y+yc)
        setpixel(x+ xc,-y+yc)
        setpixel(-x+xc,-y + yc)

        if (p1 < 0):
            x += 1
            dx = dx + (2 * ry * ry)
            p1 = p1 + dx + (ry * ry)
        else:
            x += 1
            y -= 1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            p1 = p1 + dx - dy + (ry * ry)    
    
    p2 = (((ry*ry) * ((x+0.5) * (x+0.5))) +((rx*rx) * ((y-1) * (y-1))) -(rx*rx * ry * ry))
    while (y >= 0):
        setpixel(x+xc, y+yc)
        setpixel(-x+xc, y+yc)
        setpixel(x+ xc, -y + yc)
        setpixel(-x + xc, -y + yc)

       
        if (p2 > 0):
            y -= 1
            dy = dy - (2 * rx * rx)
            p2 = p2 + (rx * rx) - dy
        else:
            y -= 1
            x += 1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            p2 = p2 + dx - dy + (rx * rx)


def main():
    rx = float(input("Radius along x axis:"))
    ry = float(input("Radius along y axis:"))
    xc = float(input("xcoordinate:"))
    yc = float(input("ycoordinate:")) 
    print("starting window....")
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500) 
    glutInitWindowPosition(200, 200)
    glutCreateWindow("Ellipse midpoint algorithm")
    glutDisplayFunc(lambda: ellipse_midpoint( rx, ry, xc, yc))
    glutIdleFunc(lambda: ellipse_midpoint(rx, ry, xc, yc))
    clearscreen()
    glutMainLoop()    
        
main()