import random
import turtle
from turtle import Turtle, Screen
screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make your Bet", prompt="Which turtle will win the race? Enter a color: ")

#----- Method to set the location of the Turtle ------
#tim = Turtle(shape="turtle")
#tim.penup()
#tim.goto(x=-230,y=-100)
#----------------------------

color = ["red", "blue", "green", "yellow", "purple", "orange"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(color[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(tim)


if user_input:
    game_is_on = True


while game_is_on:

    for t in all_turtles:
        if t.xcor() > 230:
            game_is_on = False
            winning_color = t.pencolor()
            if winning_color == user_input:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        t.forward(rand_distance)











screen.exitonclick()
