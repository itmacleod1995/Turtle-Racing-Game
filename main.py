import turtle
from turtle import Turtle, Screen
import random

#Set up screen
screen = Screen()
screen.setup(width=500, height=400)

#Random speeds the turtles can go
speeds = [5,10,15,20]

#Set up pop up box
bet = screen.textinput(title="Bet", prompt="Who will win?")

#red turtle
red_turtle = Turtle(shape="turtle")
red_turtle.color("red")
red_turtle.penup()
red_turtle.goto(-240,70)

#green turtle
green_turtle = Turtle(shape="turtle")
green_turtle.color("green")
green_turtle.penup()
green_turtle.goto(-240,40)

#yellow turtle
yellow_turtle = Turtle(shape="turtle")
yellow_turtle.color("yellow")
yellow_turtle.penup()
yellow_turtle.goto(-240,10)

#purple turtle
purple_turtle = Turtle(shape="turtle")
purple_turtle.color("purple")
purple_turtle.penup()
purple_turtle.goto(-240,-20)

#blue turtle
blue_turtle = Turtle(shape="turtle")
blue_turtle.color("blue")
blue_turtle.penup()
blue_turtle.goto(-240,-50)

#Game loop
while blue_turtle.xcor() < screen.window_width() - 260 and red_turtle.xcor() < screen.window_width() - 260 and yellow_turtle.xcor() < screen.window_width() - 260 and purple_turtle.xcor() < screen.window_width() - 260 and green_turtle.xcor() < screen.window_width() - 260:
    #select random speed for red turtle
    speedForRed = random.choice(speeds)
    red_turtle.forward(speedForRed)

    #select random speed for green turtle
    speedForGreen = random.choice(speeds)
    green_turtle.forward(speedForGreen)

    # select random speed for yellow turtle
    speedForYellow = random.choice(speeds)
    yellow_turtle.forward(speedForYellow)

    # select random speed for purple turtle
    speedForPurple = random.choice(speeds)
    purple_turtle.forward(speedForPurple)

    # select random speed for blue turtle
    speedForBlue = random.choice(speeds)
    blue_turtle.forward(speedForBlue)

#Decide winner
winner = ""
if red_turtle.xcor() > screen.window_width() - 260:
    print("Winner: Red")
    winner = "red"
elif green_turtle.xcor() > screen.window_width() - 260:
    print("Winner: Green")
    winner = "green"
elif yellow_turtle.xcor() > screen.window_width() - 260:
    print("Winner: Yellow")
    winner = "yellow"
elif purple_turtle.xcor() > screen.window_width() - 260:
    print("Winner: Purple")
    winner = "purple"
else:
    print("Winner: Blue")
    winner = "blue"

if bet == winner:
    print("You won the bet!")
else:
    print("You lose!")


screen.exitonclick()



