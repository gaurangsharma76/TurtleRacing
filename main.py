from turtle import Turtle, Screen
import random

is_race_on=False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
user_choice = screen.textinput(title="Bet on turtle", prompt="Which turtle will win the race? Enter a color from "
                                                             "VIBGYOR: ").lower()
all_turtles = []

for i in range(len(colors)):
    tur = Turtle(shape='turtle')
    tur.penup()
    tur.color(colors[i])
    tur.goto(x=-230, y=y_pos[i])
    all_turtles.append(tur)

if user_choice:
    is_race_on = True

while is_race_on:
    for i in all_turtles:
        if i.xcor() >= 230:
            is_race_on = False
            color = i.pencolor()
            if color == user_choice:
                print("Congratulations!You Won!!")
            else:
                print(f"You lost. The {color} turtle won")
        else:
            i.forward(random.randint(0, 10))

screen.exitonclick()
