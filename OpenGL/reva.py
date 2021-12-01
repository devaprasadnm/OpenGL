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

    glColor3f(rgb[0], rgb[1], rgb[2])

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
        [2,0],
        
    ]

    points =[
      [x1,y1],
      [x2,y2],
      [x3,y3],
      
    ]

    

    setpixel(edges,points,rgb)

def translation(x1,y1,x2,y2,x3,y3,tx,ty):

    rgb = (1.0,0.0,0.0)

    triangle(x1,y1,x2,y2,x3,y3,rgb)

    
    X1=x1+tx
    Y1=y1+ty

    X2=x2+tx
    Y2=y2+ty

    X3=x3+tx
    Y3=y3+ty


    rgb =(0.0,1.0,0.0)

    triangle(X1,Y1,X2,Y2,X3,Y3,rgb)
    
    
def Scale(x1,y1,x2,y2,x3,y3,sx,sy):
    rgb = (1.0,0.0,0.0)
    triangle(x1,y1,x2,y2,x3,y3,rgb)

    X1=sx*x1
    Y1=sy*y1

    X2=sx*x2
    Y2=sy*y2

    X3=sx*x3
    Y3=sy*y3

    rgb =(0.0,1.0,0.0)

    triangle(X1,Y1,X2,Y2,X3,Y3,rgb)

def Scaling(x1,y1,x2,y2,x3,y3,sx,sy,xr=0,yr=0):

    rgb = (1.0,0.0,0.0)
    triangle(x1,y1,x2,y2,x3,y3,rgb)
    X1=(x1-xr)*sx+xr
    Y1=(y1-yr)*sy+yr

    X2=(x2-xr)*sx+xr
    Y2=(y2-yr)*sy+yr

    X3=(x3-xr)*sx+xr
    Y3=(y3-yr)*sy+yr

    rgb =(0.0,1.0,0.0)

    triangle(X1,Y1,X2,Y2,X3,Y3,rgb)


def Rotation(x1,y1,x2,y2,x3,y3,angle,xr=0,yr=0):
    print(xr)
    print(yr)
    rgb = (0.0,1.0,0.0)
    triangle(x1,y1,x2,y2,x3,y3,rgb)
    rad_angle= (angle*(22/7))/180
    cosT=math.cos(rad_angle)
    sinT=math.sin(rad_angle)



    X1= cosT*(x1-xr)-sinT*(y1-yr)+xr
    Y1= sinT*(x1-xr)+cosT*(y1-yr)+yr
    

    X2=cosT*(x2-xr)-sinT*(y2-yr)+xr
    Y2=sinT*(x2-xr)+cosT*(y2-yr)+yr

    X3=cosT*(x3-xr)-sinT*(y3-yr)+xr
    Y3= sinT*(x3-xr)+cosT*(y3-yr)+yr

    rgb =(1.0,0.0,0.0)

    triangle(X1,Y1,X2,Y2,X3,Y3,rgb)

  

def reflection(x1,y1,x2,y2,x3,y3,choice,x0=0,y0=0,x=0,y=0):
    print(x0)
    print(y0)
    print(x)
    print(y)

    
    if choice == 1:
        
        rgb = (1.0,0.0,0.0)
        triangle(x1,y1,x2,y2,x3,y3,rgb)         
        X1= x1
        Y1= -(y1)         
        X2= x2
        Y2= -(y2)         
        X3= x3
        Y3= -(y3)

        rgb =(0.0,1.0,0.0)

        triangle(X1,Y1,X2,Y2,X3,Y3,rgb)

    if choice ==2:
        rgb = (1.0,0.0,0.0)
        triangle(x1,y1,x2,y2,x3,y3,rgb)         
        X1= -(x1)
        Y1= y1         
        X2= -(x2)
        Y2= y2         
        X3= -(x3)
        Y3= y3

        rgb =(0.0,1.0,0.0)

        triangle(X1,Y1,X2,Y2,X3,Y3,rgb)    



    if choice==3:

        rgb = (1.0,0.0,0.0)
        triangle(x1,y1,x2,y2,x3,y3,rgb)         
        X1= -(x1)
        Y1= -(y1)         
        X2= -(x2)
        Y2= -(y2)         
        X3= -(x3)
        Y3= -(y3)

        rgb =(0.0,1.0,0.0)

        triangle(X1,Y1,X2,Y2,X3,Y3,rgb)

    if choice==4:
        rgb = (1.0,0.0,0.0)
        triangle(x1,y1,x2,y2,x3,y3,rgb)         
        X1= y1
        Y1= x1         
        X2= y2
        Y2= x2         
        X3= y3
        Y3= x3

        rgb =(0.0,1.0,0.0)

        triangle(X1,Y1,X2,Y2,X3,Y3,rgb)
        
    if choice==5:
        rgb = (1.0,0.0,0.0)
        triangle(x1,y1,x2,y2,x3,y3,rgb)         
        X1= -(y1)
        Y1= -(x1)         
        X2= -(y2)
        Y2= -(x2)         
        X3= -(y3)
        Y3= -(x3)

        rgb =(0.0,1.0,0.0)

        triangle(X1,Y1,X2,Y2,X3,Y3,rgb) 
    

    if choice ==6:
        rgb = (1.0,0.0,0.0)
        triangle(x1,y1,x2,y2,x3,y3,rgb)
        print("choice")
        if (x-x0)==0:
            print("haii slope =0")
        else:
            print("haii")
            m=(y-y0)/(x-x0)

            c=y-(m*x)
    
            X1=(1-(m*m)*x1+2*m*(y1-c))/(1+(m*m))
            Y1=(2*m*x1-(1-(m*m))*y1+2*c)/(1+(m*m))
    
            X2=(1-(m*m)*x2+2*m*(y2-c))/(1+(m*m))
            Y2=(2*m*x2-(1-(m*m))*y2+2*c)/(1+(m*m))
    
            X3=(1-(m*m)*x3+2*m*(y3-c))/(1+(m*m))
            Y3=(2*m*x3-(1-(m*m)*y3+2*c)/(1+(m*m)))

            rgb =(0.0,1.0,0.0)
    
            triangle(X1,Y1,X2,Y2,X3,Y3,rgb) 

def main():



    choice=0
    x1=float(input('x1 Coordinate:'))
    y1=float(input("y1 Coordinate:"))
    x2=float(input('x2 Coordinate:'))
    y2=float(input("y2 Coordinate:"))
    x3=float(input('x3 Coordinate:'))
    y3=float(input("y3 Coordinate:"))


   
    while(choice!=5):
        glutInit()
        glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
        glutInitWindowSize(500,500)
        glutInitWindowPosition(200,200)
        choice=int(input("Choose the 2D Transformation Technique\n\t1.Translation\n\t2.Scaling\n\t3.Rotation\n\t4.Reflection\n\t5.exit\n"))
        if choice==1:

            tx=float(input('tx Coordinate:'))
            ty=float(input('ty Coordinate:'))

            
            glutCreateWindow("2D Translation")
            glutDisplayFunc(lambda: translation(x1, y1, x2, y2,x3,y3,tx,ty))
            glutIdleFunc(lambda: translation(x1, y1, x2, y2,x3,y3,tx,ty))

            clearscreen()
            glutMainLoop()



        elif choice==2:
            choice=int(input("Choose the Scaling Method\n\t1.About Origin \n\t2.About reference point\n\t"))

            sx=float(input('sx:'))
            sy=float(input('sy:'))

            if choice==1:
                glutCreateWindow("2D Scaling")
                glutDisplayFunc(lambda: Scaling(x1, y1, x2, y2,x3,y3,sx,sy))
                glutIdleFunc(lambda: Scaling(x1, y1, x2, y2,x3,y3,sx,sy))
            if choice==2:
                rx=float(input('rx:'))
                ry=float(input('ry:'))
                
                glutCreateWindow("2D Scaling")
                glutDisplayFunc(lambda: Scaling(x1, y1, x2, y2,x3,y3,sx,sy,rx,ry))
                glutIdleFunc(lambda: Scaling(x1, y1, x2, y2,x3,y3,sx,sy,rx,ry))

            clearscreen()
            glutMainLoop()


                

        elif choice==3:
            choice=int(input("Choose the Rotation Method\n\t1.About Origin \n\t2.About reference point\n\t"))

            angle=float(input('angle:'))

            if choice==1:

                glutCreateWindow("2D Rotation")
                glutDisplayFunc(lambda: Rotation(x1, y1, x2, y2,x3,y3,angle))
                glutIdleFunc(lambda: Rotation(x1, y1, x2, y2,x3,y3,angle))
            if choice==2:
                xr=float(input('xr:'))
                yr=float(input('yr:'))

                glutCreateWindow("2D Rotation")
                glutDisplayFunc(lambda: Rotation(x1, y1, x2, y2,x3,y3,angle,xr,yr))
                glutIdleFunc(lambda: Rotation(x1, y1, x2, y2,x3,y3,angle,xr,yr))

            clearscreen()
            glutMainLoop()


      
        elif choice==4:

            ch=int(input("Choose the Reflection Method\n\t1.About x axis \n\t2.About y axis \n\t3.About origin\n\t4.About y=x line\n\t5.About y=-x line\n\t6.About a Arbitary line\n\t"))
            if ch==6:
                x0=float(input('x0 Coordinate:'))
                y0=float(input("y0 Coordinate:"))
                x=float(input('x Coordinate:'))
                y=float(input("y Coordinate:"))

                glutCreateWindow("2D Reflection")
                glutDisplayFunc(lambda: reflection (x1, y1, x2, y2,x3,y3,ch,x0,y0,x,y))
                glutIdleFunc(lambda: reflection (x1, y1, x2, y2,x3,y3,ch,x0,y0,x,y))
            else:

                glutCreateWindow("2D Reflection")
                glutDisplayFunc(lambda: reflection (x1, y1, x2, y2,x3,y3,ch))
                glutIdleFunc(lambda: reflection (x1, y1, x2, y2,x3,y3,ch))
            clearscreen()
            glutMainLoop()



        else:
            print("Invalid Choice")    
main()   







