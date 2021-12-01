
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math



X1,Y1,X2,Y2,X3,Y3=0,0,30,60,-30,60
angle=0


def clearscreen():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-100.0,100.0,-100.0,100.0)
    

def setpixel(edges,points,rgb):
    glColor3f(rgb[0],rgb[1],rgb[2])
    glBegin(GL_POLYGON)

    for e in edges:
        for v in e:
            glVertex2fv([points[v]])

    glEnd()
    glFlush()


def update(value):
    global  X1,Y1,X2,Y2,X3,Y3,angle 
    glutPostRedisplay()
    glutTimerFunc(int(1000/60),update,int(0))
    angle=angle+2
    X1,Y1,X2,Y2,X3,Y3=rotation(X1,Y1,X2,Y2,X3,Y3,0,0,angle)     
    




def triangle(x1,y1,x2,y2,x3,y3,rgb):
    edges=[
     [0,1],
     [1,2],
     [2,0]
    ]

    points=[

     [x1,y1],
     [x2,y2],
     [x3,y3]
     
    ]

    setpixel(edges,points,rgb)
def rotation(x1,y1,x2,y2,x3,y3,xr,yr,angle):

    rad_angle=(angle*math.pi)/180
    X1=(x1-xr)*math.cos(rad_angle)-(y1-yr)*math.sin(rad_angle)+xr
    Y1=(x1-xr)*math.sin(rad_angle)+(y1-yr)*math.cos(rad_angle)+yr

    X2=(x2-xr)*math.cos(rad_angle)-(y2-yr)*math.sin(rad_angle)+xr
    Y2=(x2-xr)*math.sin(rad_angle)+(y2-yr)*math.cos(rad_angle)+yr

    X3=(x3-xr)*math.cos(rad_angle)-(y3-yr)*math.sin(rad_angle)+xr
    Y3=(x3-xr)*math.sin(rad_angle)+(y3-yr)*math.cos(rad_angle)+yr

    return X1,Y1,X2,Y2,X3,Y3
    
    

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    global X1,Y1,X2,Y2,X3,Y3
    green=(0.0,0.0,1.0)
    triangle(X1,Y1,X2,Y2,X3,Y3,green)
    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutCreateWindow("Fan")
    glutInitWindowSize(500,500)
    glutInitWindowPosition(200,200)
    glutDisplayFunc(display)
    glutTimerFunc(0,update,0)
    clearscreen()
    glutMainLoop()
main()