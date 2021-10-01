from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*


def clearscreen():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-100, 100, -100, 100)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 1.0)
    glPointSize(5.0)

def setpixel(edges,points):


    glBegin(GL_LINES)
    
    for e in edges:
        for v in e:
            glVertex2fv(points[v])
    glEnd()
    glFlush()

def rectangle(x1,y1,x2,y2):
    edges = [
        [0,1],
        [1,2],
        [2,3],
        [3,0]
    ]

    points =[
      [x1,y2],
      [x2,y2],
      [x2,y1],
      [x1,y1]
    ]

    hana = (1.0,0.0,0.0)

    setpixel(edges,points)

# -------line--------------------------------

# def line(x1,y1,x2,y2):

#     edges = [
#         [0,1],
#        ]

#     points=[
#       [x1,y1],
#       [x2,y2]  
#     ]   
     

#     setpixel(edges,points) 





def main():
    choice=0
   
    while(choice!=2):
        choice=int(input("Enter\n\t1.Plot a line \n\t2.exit\n"))
        if choice==1:
            x1=float(input('x1 Coordinate:'))
            x2=float(input('x2 Coordinate:'))
            y1=float(input("y1 Coordinate:"))
            y2=float(input("y2 Coordinate:"))
        
            glutInit()
            glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
            glutInitWindowSize(500,500)
            glutInitWindowPosition(200,200)
            glutCreateWindow("Line using Midpoint Algorithm")
            glutDisplayFunc(lambda: rectangle(x1, y1, x2, y2))
            glutIdleFunc(lambda: rectangle(x1, y1, x2, y2))
            clearscreen()
            glutMainLoop()
        else:
            print("Invalid Choice")    
main()   








