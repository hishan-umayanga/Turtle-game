from turtle import Turtle,Screen
import random


is_race_on = False

screen = Screen()


#custermize the windows size

screen.setup(width=600,height=400)



#get user input
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle  will win the race ? Enter a color: [red, orange, green, yellow, blue, silver] ")

#turtle colors
color = ["red","orange","green", "yellow", "blue", "silver"]

#turtle y position
y_position = [-70, -40, -10, 20, 50, 80]



#create a list for all newly created turtle

all_turtles = []

for number_of_turtle in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[number_of_turtle])
    new_turtle.penup()
    new_turtle.goto(x=-280, y=y_position[number_of_turtle])
    all_turtles.append(new_turtle)

#check  the  user is input value
if user_bet:
    is_race_on = True

while is_race_on:
     for turtle in all_turtles:
          if turtle.xcor() > 270:
              is_race_on = False
              winning_color = turtle.pencolor()
              if winning_color == user_bet:
                   screen.textinput(title="win ", prompt=f"You have won ! The {winning_color} turtle is the winner!")
              else:
                    screen.textinput(title="loss" , prompt=f"You have loss ! The {winning_color} turtle is the winner!")
    
#make each turtle move random distance
          random_distance = random.randint(0, 10)
          turtle.forward(random_distance)

screen.exitonclick()