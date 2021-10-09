import random
from turtle import Turtle, Screen
is_race_on = False


all_turtles = []

screen = Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput(title="which is your favorite", prompt="Choose the color of turtle")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-125, -75, -25, 25, 75, 125]

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_choice:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_choice:
                print(f"Your {winning_color} turtle came first")
            else:
                print(f"Your turtle lost, {winning_color} turtle wins")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()

