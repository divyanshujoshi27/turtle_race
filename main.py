from turtle import Turtle, Screen
import random

def draw_lines():
    line = Turtle()
    line.hideturtle()
    line.penup()
    line.goto(-240, 100)
    line.pendown()
    line.goto(-240, -100)
    line.penup()
    line.goto(240, 100)
    line.pendown()
    line.goto(240, -100)

def create_turtles(colors, y_positions):
    turtles = []
    for index in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[index])
        new_turtle.penup()
        new_turtle.goto(-238, y_positions[index])
        turtles.append(new_turtle)
    return turtles

def start_race(turtles, user_bet):
    is_race_on = True
    while is_race_on:
        for turtle in turtles:
            if turtle.xcor() > 230:
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You win! The {winning_color} turtle is the winner!")
                else:
                    print(f"You lose. The {winning_color} turtle is the winner.")
                is_race_on = False
                turtle.shapesize(stretch_wid=2, stretch_len=2)
                break
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

draw_lines()
all_turtles = create_turtles(colors, y_positions)

if user_bet:
    start_race(all_turtles, user_bet)

screen.exitonclick()
