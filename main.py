# def fun(a):
#   return a+3*2
# def mul(b,f):
#   return f(b)*100
# a=mul(10,fun)
# print(a)


# from turtle import Turtle,Screen
# import turtle as t
# tim=t.Turtle()
# tim.shape("turtle")
# screen=Screen()
# def mov():
#   tim.forward(5)
#   # ld(10)
# def back():
#   tim.bk(5)
# def clc():
#   r=tim.heading() +10
#   tim.setheading(r)
# def aclc():
#   tim.left(10)
# def clear():
#   tim.clear()
#   tim.penup()
#   tim.home()
#   tim.pendown()
# screen.listen()
# screen.onkey(mov,"Up")
# screen.onkey(back,"Down")
# screen.onkey(clc,"Right")
# screen.onkey(aclc,"Left")
# screen.onkey(clear,"space")
# screen.exitonclick()














import random
from turtle import Turtle,Screen
import turtle as t
clr=["red","yellow","blue","pink","green","violet","orange"]
screen=Screen()
screen.setup(500,400)
bet=screen.textinput(title="Bet A Turtle",prompt="Which Colour Turtle do you choose: ")
all=[]
y=130
for i in clr:
  tim=t.Turtle(shape="turtle")
  tim.color(i)
  tim.penup()
  tim.goto(-230,y)
  all.append(tim)
  y-=40

empire=t.Turtle("turtle")
empire.color("cyan")
empire.penup()
empire.left(90)
empire.goto(230,150)
empire.pendown()
empire.backward(305)
# print(empire.ycor())
empire.penup()
empire.goto(-35,155)
empire.pendown()
empire.write("start")
empire.penup()
empire.goto(-130,-155)
empire.hideturtle()
empire.pendown()
# print(empire.color())

race_on=False
if bet:
  race_on=True

while race_on:
  for t in all:
    if t.xcor()>210:
      win=t.pencolor() # win=t.color()
      empire.write(f"{win} Turtle Won",font="12")
      empire.penup()
      empire.goto(-130,-100)
      empire.pendown()
      if win==bet:
        print(f" ✨Yeeaah!! your {bet} 🐢 is the winner")
        screen.title(f"Yeaah..Your {win} Turtle WON!!")
      else:
        print(f"OOOH..You lose🥺\n {win} 🐢 is the winner")
        screen.title(f"You lose {win} turtle is the winner")
      race_on=False
    dis=random.randint(0,10)
    t.forward(dis)
    
screen.exitonclick