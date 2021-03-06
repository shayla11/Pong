# Simple Pong for beginners
# Shayla Sexton

import turtle
import os

window = turtle.Screen()
window.title("Pong by Shayla Sexton")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 2     # d means delta or change, everytime
ball.dy = -2     # the ball moves it will move up 2 and over 2

# Pen
pen = turtle.Turtle() #Just like turtle Tina
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24)) #No Type Parameter



# Function to move Paddles
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

# Keyboard Binding
window.listen()
window.onkey(paddle_a_up, "w") #Use "onkey" instead of "onkeypress"
window.onkey(paddle_a_down, "s")
window.onkey(paddle_b_up, "Up" ) #Up, Down, Left, Right are the arrow keys
window.onkey(paddle_b_down, "Down")


# Main Game loop
while True:
     window.update()

     # Move the Ball
     ball.setx(ball.xcor() + ball.dx)
     ball.sety(ball.ycor() + ball.dy)

     # Border Check
     if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 # Reverses direction

     if ball.ycor() < -290:
         ball.sety(-290)
         ball.dy *= -1

     if ball.xcor() > 390: # Ball goes off  Right Side
         ball.goto(0,0)
         ball.dx *= -1
         score_a += 1
         pen.clear()
         pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24))  # No Type Parameter
         # The "{}" just mean when you use the format method those values, score_a and score_b will be places inside.
         os.system("afplay point.mp3&")

         # 'afplay' is required for mac systems to play sound files. The '&' sign at the end is included so the sound can play during the action.

     if ball.xcor() < -390: # Ball goes off Left Side
         ball.goto(0,0)
         ball.dx *= -1
         score_b += 1
         pen.clear()
         pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24))  # No Type Parameter
         os.system("afplay point.mp3&")



     # Paddle + Ball Collision
     if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
         ball.setx(340)
         ball.dx *= -1
         os.system("afplay hit.mp3&")

     if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
         ball.setx(-340)
         ball.dx *= -1
         os.system("afplay hit.mp3&")