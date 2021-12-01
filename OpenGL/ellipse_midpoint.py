from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

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

def MidpointEllipse(a,b,xc,yc):
    x,y = 0 , b
    SetPixel(xc+x,yc+y)
    SetPixel(xc-x,yc+y)
    SetPixel(xc-x,yc-y)
    SetPixel(xc+x,yc-y)

    p1=(b*b)-(a*a*b)+(0.25*a*a)

    v=2*a*a*y
    u=2*b*b*x

    while(u<v):
        if p1<0 :
            x+=1
            u=u+2*b*b
            p1=p1+u+b*b
        else:
            x+=1
            y-=1
            v=v-2*a*a
            u=u+2*b*b
            p1=p1+u-v+b*b
            

        SetPixel(xc+x,yc+y)
        SetPixel(xc-x,yc+y)
        SetPixel(xc-x,yc-y)
        SetPixel(xc+x,yc-y)

    p2=(b*b*(x+0.5)*(x+0.5)) + (a*a*(y-1)*(y-1))-(a*a*b*b)

    while(y>0):
        if p2>0:
            y-=1
            v=v-2*a*a
            p2=p2-v+a*a
        else:
            x+=1
            y-=1
            u=u+2*b*b
            v=v-2*a*a
            p2=p2+u-v+a*a

        SetPixel(xc+x,yc+y)
        SetPixel(xc-x,yc+y)
        SetPixel(xc-x,yc-y)
        SetPixel(xc+x,yc-y)





def Main():
    a= int(input("Rx = "))
    b= int(input("Ry = "))
    xc= int(input("Xc = "))
    yc= int(input("Yc = "))
    print("starting window....")
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(200, 200)
    glutCreateWindow("Ellipse_Midpoint")
    glutDisplayFunc(lambda: MidpointEllipse(a,b,xc,yc))
    glutIdleFunc(lambda: MidpointEllipse(a,b,xc,yc ))
    ClearScreen()
    glutMainLoop()


Main()

