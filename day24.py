import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle to draw the stars
star_turtle = turtle.Turtle()
star_turtle.speed(0)
star_turtle.hideturtle()

# Function to draw a star
def draw_star(x, y, size, color):
    star_turtle.penup()
    star_turtle.goto(x, y)
    star_turtle.pendown()
    star_turtle.color(color)
    star_turtle.begin_fill()
    for _ in range(5):
        star_turtle.forward(size)
        star_turtle.right(144)
    star_turtle.end_fill()

# Function to create a star show
def star_show(number_of_stars):
    colors = ["white", "yellow", "blue", "red", "green"]
    for _ in range(number_of_stars):
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        size = random.randint(10, 50)
        color = random.choice(colors)
        draw_star(x, y, size, color)

# Run the star show with 50 stars
star_show(50)

# Keep the window open until clicked
screen.exitonclick()