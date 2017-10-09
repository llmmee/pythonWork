import turtle
import math 
def Angle1(T, size=50, num=5, color=None):
    if color:
        T.begin_fill()
        T.fillcolor(color)
    for i in range(num):
        T.forward(size)
        T.left(360.0/num)
        T.forward(size)
        T.right(2*360.0/num)
    if color:
        T.end_fill()
 
def Angle2(T=None, start_pos=(0,0), end_pos=(0,10), radius=100, color=None):
    T = T or turtle.Turtle()
    size = radius * math.sin(math.pi/5)/math.sin(math.pi*2/5)
    T.left(math.degrees(math.atan2(end_pos[1]-start_pos[1], end_pos[0]-start_pos[0])))
    T.penup()
    T.goto(start_pos)
    T.fd(radius)
    T.pendown()
    T.right(math.degrees(math.pi*9/10))
    Angle1(T, size, 5, color)
 
def stars(times=20.0):
    width, height = 30*times, 20*times
    window = turtle.Screen()
    T = turtle.Turtle()
    T.hideturtle()
    T.speed(10)
    T.color('red')
    T.penup()
    T.goto(-width/2, height/2)
    T.pendown()
    T.begin_fill()
    T.fillcolor('red')
    T.fd(width)
    T.right(90)
    T.fd(height)
    T.right(90)
    T.fd(width)
    T.right(90)
    T.fd(height)
    T.right(90)    
    T.end_fill()
    T.color('yellow')
    Angle2(T, start_pos=(-10*times, 5*times), end_pos=(-10*times, 8*times), radius=3*times, color='yellow')  
    stars_start_pos = [(-5, 8), (-3, 6), (-3, 3), (-5, 1)]
    for pos in stars_start_pos:
        Angle2(T, start_pos=(pos[0]*times, pos[1]*times), end_pos=(-10*times, 5*times), radius=1*times, color='yellow')  
    window.exitonclick()
 
if __name__ == '__main__':
        stars()
