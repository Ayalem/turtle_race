from turtle import Turtle,Screen
import random
colors=["violet","pale turquoise","medium sea green","light sky blue","yellow","orange"]
screen=Screen()
screen.setup(height=200,width=200)
turtles=[]
make_bet=screen.textinput(title="make your bet",prompt="bet on who will win the race,pick a color:")
print(make_bet)
for i in range(0,6):
 turtle=Turtle("turtle")
 turtle.color(colors[i])
 turtle.penup()
 turtle.goto(x=-180,y=-80+i*20)
 turtles.append(turtle)
race_is_on=True


while race_is_on:
 for turtle in turtles:
  movement = random.randint(0, 20)
  turtle.forward(movement)
  if turtle.xcor()>180:
   race_is_on=False
   color=turtle.pencolor()
   print(f"the{color} turtle won.")
   if color==make_bet:
         print("You win")
   else:
    print("you Lose")








screen.exitonclick()

