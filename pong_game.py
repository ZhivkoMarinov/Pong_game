import turtle
import time

window = turtle.Screen()
window.title('Lamav Pong')
window.setup(width=800, height=600)
window.bgcolor('black')
window.tracer(0)

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

paddle_a.penup()
paddle_a.goto(-350, 0)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)

# Values in pixels. Configure by CPU speed
ball.dx = 0.2
ball.dy = -0.2


# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard biding
window.listen()
window.onkeypress(paddle_a_up, 'w')
window.onkeypress(paddle_a_down, 's')
window.onkeypress(paddle_b_up, 'Up')
window.onkeypress(paddle_b_down, 'Down')

# Result
goals_a = 0
goals_b = 0


result_a = turtle.Turtle()
result_a.speed(0)
result_a.color('white')
result_a.penup()
result_a.goto(-380, 270)
result_a.write(0, align='left', font=('Arial', 16, 'bold'))
result_a.hideturtle()


result_b = turtle.Turtle()
result_b.speed(0)
result_b.color('white')
result_b.penup()
result_b.goto(380, 270)
result_b.write(0, align='right', font=('Arial', 16, 'bold'))
result_b.hideturtle()


print(goals_a)
# main loop
while True:
    window.update()    
   
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1        
        goals_a += 1
        result_a.clear()
        result_a.write(goals_a, align='left', font=('Arial', 16, 'bold'))
        

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        goals_b += 1
        result_b.clear()
        result_b.write(goals_b, align='right', font=('Arial', 16, 'bold'))
        
        
    # ball hitting the paddle
    # print(paddle_b.ycor(), int(ball.ycor()), int(ball.xcor()))
    if int(ball.xcor()) == 330 and int(ball.ycor()) in range(int(paddle_b.ycor() - 55), int(paddle_b.ycor() + 56)):
        ball.sety(ball.ycor())
        ball.dx *= -1

    if int(ball.xcor()) == -330 and int(ball.ycor()) in range(int(paddle_a.ycor() - 55), int(paddle_a.ycor() + 56)):
        ball.sety(ball.ycor())
        ball.dx *= -1   
    
    
    
