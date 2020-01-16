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
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle B

# Ball

# Main Game loop

while True:
     window.update()
