# Simple Pong for beginners

import turtle

window = turtle.Screen()
window.title("Pong by Shayla Sexton")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

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

# Function to move Paddles
def paddle_a_up():
     y = paddle_a.ycor()
     y += 20
     paddle_a.sety(y)

def paddle_a_down():
     y = paddle_a.ycor()
     y -= 20
     paddle_a.sety(y)

# Keyboard Binding
window.listen()
window.onkey(paddle_a_up, "w") #Use "onkey" instead of "setonkeypress"
window.onkey(paddle_a_down, "s")



# Main Game loop
while True:
     window.update()
