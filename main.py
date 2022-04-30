import turtle
from turtle import Turtle, Screen

#Set up screen
screen = Screen()
screen.setup(width=500, height=400)

#Set up pop up box
#bet = screen.textinput(title="Bet", prompt="Who will win?")


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


screen.exitonclick()



