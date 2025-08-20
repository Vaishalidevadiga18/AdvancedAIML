import turtle

# Set up window
screen = turtle.Screen()
screen.title("Shapes: Triangle, Rectangle, Circle")
screen.bgcolor("lightyellow")

pen = turtle.Turtle()
pen.pensize(3)

# Function to draw a rectangle
def draw_rectangle(x, y, width, height):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    for _ in range(2):
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)

# Function to draw a triangle
def draw_triangle(x, y, size):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    for _ in range(3):
        pen.forward(size)
        pen.left(120)

# Function to draw a circle
def draw_circle(x, y, radius):
    pen.penup()
    pen.goto(x, y - radius)  # Move to bottom of circle
    pen.pendown()
    pen.circle(radius)

# Draw shapes
pen.color("blue")
draw_rectangle(-200, 0, 120, 80)   # rectangle

pen.color("green")
draw_triangle(50, 0, 100)          # triangle

pen.color("red")
draw_circle(200, 0, 60)            # circle

# Hide turtle
pen.hideturtle()
screen.mainloop()
