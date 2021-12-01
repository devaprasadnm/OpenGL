from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import math


def clearscreen():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-50, 50, -50, 50)
    glClear(GL_COLOR_BUFFER_BIT)
    
    glPointSize(5.0)

def setpixel(edges,points,rgb):

    glColor3f(rgb[0],rgb[1],rgb[2])
    glBegin(GL_LINES)
    
    for e in edges:
        for v in e:
            glVertex2fv(points[v])
    glEnd()
    glFlush()

def triangle(x1,y1,x2,y2,x3,y3,rgb):
    edges = [
        [0,1],
        [1,2],
        [2,0]
    ]

    points =[
      [x1,y1],
      [x2,y2],
      [x3,y3]
    ]

    setpixel(edges,points,rgb)

def line(x1,y1,x2,y2,rgb):
    edges = [
        [0,1]
    ]

    points =[
      [x1,y1],
      [x2,y2]
    ]


    setpixel(edges,points,rgb)

def translation(x1,y1,x2,y2,x3,y3,tx,ty):
    rgb=(1.0,0,0)
    triangle(x1, y1, x2, y2,x3,y3,rgb)

    x1,y1,x2,y2,x3,y3=x1+tx,y1+ty,x2+tx,y2+ty,x3+tx,y3+ty
    rgb =(0,1,0)
    triangle(x1, y1, x2, y2,x3,y3,rgb)

def scaling(x1,y1,x2,y2,x3,y3,tx,ty,xr=0,yr=0):
    rgb=(1.0,0,0)
    triangle(x1, y1, x2, y2,x3,y3,rgb)

    x1= (x1-xr)*tx+xr
    y1=(y1-yr)*ty+yr
    x2=(x2-xr)*tx+xr
    y2=(y2-yr)*ty+yr
    x3=(x3-xr)*tx+xr
    y3=(y3-yr)*ty+yr
    rgb =(0,1,0)
    triangle(x1, y1, x2, y2,x3,y3,rgb)


def rotation(x1,y1,x2,y2,x3,y3,angle,xr=0,yr=0):
    rgb=(1.0,0,0)
    triangle(x1, y1, x2, y2,x3,y3,rgb)
    cosT=  math.cos(angle)
    sinT=  math.sin(angle)
    X1 = (x1-xr)*cosT - (y1-yr)*sinT + xr
    Y1 = (x1-xr)*sinT + (y1-yr)*cosT + yr
    X2 = (x2-xr)*cosT - (y2-yr)*sinT + xr
    Y2 = (x2-xr)*sinT + (y2-yr)*cosT + yr
    X3 = (x3-xr)*cosT - (y3-yr)*sinT + xr
    Y3 = (x3-xr)*sinT + (y3-yr)*cosT + yr
    rgb =(0,1,0)
    triangle(X1, Y1, X2, Y2,X3,Y3,rgb)

def reflection(x1, y1,x2,y2,x3,y3,type,a1=0,b1=0,a2=0,b2=0):
    rgb=(1.0,0,0)
    triangle(x1, y1, x2, y2,x3,y3,rgb)
    rgb= (1,1,1)
    line(-50,0,50,0,rgb)
    line(0,50,0,-50,rgb)
    if type == 1: # About X axis
        rgb= (0,1,1)
        line(-50,0,50,0,rgb)
        y1,y2,y3 = -y1,-y2,-y3

    if type == 2: # About Y axis
        rgb= (0,1,1)
        line(0,-50,0,50,rgb)
        x1,x2,x3 = -x1,-x2,-x3
    if type == 3: # About Origin axis
        x1,y1,x2,y2,x3,y3 = -x1,-y1,-x2,-y2,-x3,-y3
    if type == 4: # About Y=X 
        rgb= (0,1,1)
        line(-50,-50,50,50,rgb)
        x1,y1,x2,y2,x3,y3 =y1,x1,y2,x2,y3,x3
    if type == 5: # About Y= -X 
        rgb= (0,1,1)
        line(-50,50,50,-50,rgb)
        x1,y1,x2,y2,x3,y3 =-y1,-x1,-y2,-x2,-y3,-x3

    if type == 6: # About arbitary line
        if a2-a1 == 0:
           reflection(x1, y1,x2,y2,x3,y3,2)
        else:
            m=(b2-b1)/(a2-a1)
            c=b1-m*a1  
            rgb= (0,1,1)
            line(-50,(m*-50)+c,50,(m*50)+c,rgb)  
            x1,y1=eqn(x1,y1,m,c)
            x2,y2=eqn(x2,y2,m,c)
            x3,y3=eqn(x3,y3,m,c)
    
    rgb =(0,1,0)
    triangle(x1, y1, x2, y2,x3,y3,rgb)



def eqn(x0,y0,m,c):
    
    x = ((1-m*m)*x0 + 2*m*(y0-c))/(1+m*m)
    y = (2*m*x0-(1-m*m)*y0+2*c)/(1+m*m)
    return(x,y)

def main():
    choice=0
   
    while(choice!=2):
        choice=int(input("Enter\n\t1.Plot a Ttiangle \n\t2.exit\n"))
        if choice==1:
            x1=float(input('x1 Coordinate:'))
            y1=float(input("y1 Coordinate:"))
            x2=float(input('x2 Coordinate:'))           
            y2=float(input("y2 Coordinate:"))
            x3=float(input('x3 Coordinate:'))           
            y3=float(input("y3 Coordinate:"))

            print("\nChoose the transformation technique")

            ch = int(input("1.Translation \n2.Scaling \n3.Rotation \n4.Reflection\n"))
                 
            glutInit()
            glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
            glutInitWindowSize(500,500)
            glutInitWindowPosition(400,400)
            glutCreateWindow("2D_TRANSFORMATION")
            if ch==1:
                tx=float(input('x Coordinate:'))
                ty=float(input("y Coordinate:"))
                glutDisplayFunc(lambda: translation(x1, y1, x2, y2,x3,y3,tx,ty))
                glutIdleFunc(lambda: translation(x1, y1, x2, y2,x3,y3,tx,ty))
            if ch == 2:
                sx=float(input('Sx =:'))
                sy=float(input("Sy =:"))
                type = int(input("\n\t1.About Origin  \n\t2.About Reference point \n\t"))
                if type == 1: 
                     glutDisplayFunc(lambda: scaling(x1, y1, x2, y2,x3,y3,sx,sy))
                     glutIdleFunc(lambda: scaling(x1, y1, x2, y2,x3,y3,sx,sy))
                if type == 2:
                    xr= float(input("xr ="))
                    yr= float(input("yr ="))
                    glutDisplayFunc(lambda: scaling(x1, y1, x2, y2,x3,y3,sx,sy,xr,yr))
                    glutIdleFunc(lambda: scaling(x1, y1, x2, y2,x3,y3,sx,sy,xr,yr))



            if ch == 3 :
                angle=float(input('Angle w.r.t origin:'))
                angle= (angle*(22/7))/180
                type = int(input("\n\t1.About Origin  \n\t2.About Reference point \n\t"))
                if type ==1:
                    glutDisplayFunc(lambda: rotation(x1, y1, x2, y2,x3,y3,angle))
                    glutIdleFunc(lambda: rotation(x1, y1, x2, y2,x3,y3,angle))
                if type == 2:
                    xr= float(input("xr ="))
                    yr= float(input("yr ="))
                    glutDisplayFunc(lambda: rotation(x1, y1, x2, y2,x3,y3,angle,xr,yr))
                    glutIdleFunc(lambda: rotation(x1, y1, x2, y2,x3,y3,angle,xr,yr))
                

            if ch == 4 :
                type = int(input("\n\t1.About X axis \n\t2.About Y axis \n\t3.About Origin \n\t4.About Y=X \n\t5.About Y=-X \n\t6.About Arbitrary line\n\t"))
                if type == 6:
                    print("Enetr the 2 points of arbitary line")
                    x0=float(input('x0 Coordinate:'))
                    y0=float(input("y0 Coordinate:"))
                    x=float(input('x Coordinate:'))
                    y=float(input("y Coordinate:"))
                    glutDisplayFunc(lambda: reflection(x1, y1, x2, y2,x3,y3,type,x0,y0,x,y))
                    glutIdleFunc(lambda: reflection(x1, y1, x2, y2,x3,y3,type,x0,y0,x,y))
                else:
                    glutDisplayFunc(lambda: reflection(x1, y1, x2, y2,x3,y3,type))
                    glutIdleFunc(lambda: reflection(x1, y1, x2, y2,x3,y3,type))
                
            clearscreen()
            glutMainLoop()
        else:
            print("Invalid Choice")    

main()   
