from turtle import Turtle, Screen

#Set up screen
screen = Screen()
screen.setup(width=500, height=400)

#Set up pop up box
bet = screen.textinput(title="Bet", prompt="Who will win?")
print(bet)

#create turtles

screen.exitonclick()



