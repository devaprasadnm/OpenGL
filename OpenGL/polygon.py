from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*


def clearscreen():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-100, 100, -100, 100)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 1.0)
    glPointSize(5.0)



def drawPolygons(edges, points, rgb):
    glColor3f(rgb[0], rgb[1], rgb[2])
    glBegin(GL_LINES)
    for e in edges:
        for v in e:
            glVertex2fv(points[v])
    glEnd()
    glFlush()

def drawGivenPolygon(edges, points):
    rgb = [1.0, 0.0, 0.0]
    drawPolygons(edges, points, rgb)

def getPolygon():
    n = int(input("Enter the number of edges : "))
    edges = list(list())
    points = list(list())
   
    for i in range(n):
        edges += [[i, (i+1) % n]]

    for i in range(n):
        x = float(input("Enter the x-coordinate value of point " + str(i+1) + ": "))
        y = float(input("Enter the y-coordinate value of point " + str(i+1) + ": "))
        points += [[x, y]]

    return edges, points


def main():
    choice=0
   
    while(choice!=2):
        choice=int(input("Enter\n\t1.Plot a Polygon \n\t2.exit\n"))
        if choice==1:
            edges, points = getPolygon()
            glutInit()
            glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
            glutInitWindowSize(1920,1080)
            glutInitWindowPosition(200,200)
            glutCreateWindow("Line using Midpoint Algorithm")
            glutDisplayFunc(lambda: drawGivenPolygon(edges, points))
            glutIdleFunc(lambda: drawGivenPolygon(edges, points))
            clearscreen()
            glutMainLoop()
        else:
            print("Invalid Choice")    
main()   








