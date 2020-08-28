
import turtle
import random


wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0


#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.penup()
paddle_a.goto(-350,0)



#Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.penup()
paddle_b.goto(350,0)

#ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_wid = 1, stretch_len = 1)
ball.penup()
ball.goto(0,0)

ball.dx = .15
ball.dy = .15
#dx and dy is movment for the ball

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("player A: 0 Player B: 0", align = "center", font=("Courier",16, "normal"))









# Function
def paddle_a_up():
    y = paddle_a.ycor()
    # ycor is from the turtle library, is the y cordinate for the object
    y += 20
    paddle_a.sety(y)
    # if y => 300:
    #     y == 299

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)    

#movement for paddel b-------------------------------    

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)   




#keyboard binidng
wn.listen()
#this tells the window to liten to the keyboard
#padle a key sytokes----
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
#paddle b key strokes
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#this from the library, sets a key and then calls the function paddle_a_up



#main game loop
while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border check ball

    if ball.ycor() >290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1   

    #border check paddle    

    if paddle_a.ycor() >260:
        paddle_a.sety(260)
    if paddle_a.ycor() <-260:
        paddle_a.sety(-260)        
    
    if paddle_b.ycor() >260:
        paddle_b.sety(260)
    if paddle_b.ycor() <-260:
        paddle_b.sety(-260)  

    #bounce ball off paddle 
    
    # if ball.xcor() > 350:# and ball.ycor() == paddle_b.ycor():
    #     ball.setx(350)
    #     ball.dx *=-1    

    # ball out of range
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx = -.15
        if ball.dy < 0:
            ball.dy = -.15
        else:
             ball.dy = .15    
        score_a +=1
        pen.clear()  
        pen.write("player A: {} Player B: {}".format(score_a,score_b), align = "center", font=("Courier",16, "normal"))   

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx = .15
        if ball.dy < 0:
            ball.dy = -.15
        else:
            ball.dy = .15   
        score_b +=1  
        pen.clear()  
        pen.write("player A: {} Player B: {}".format(score_a,score_b), align = "center", font=("Courier",16, "normal"))      


    #paddle and ball colosion
    if ball.xcor() >340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx*=-1.1
        ball.dy*=1.1 

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx*=-1.1
        ball.dy*=1.1               





    