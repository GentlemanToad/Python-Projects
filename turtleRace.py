import turtle
from random import randint
wn = turtle.Screen()
wn.title('Turtle Race')

t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-140, 140)
for step in range(15):
    t.write(step, align='center')
    t.right(90)
    t.forward(10)
    t.pendown()
    t.forward(150)
    t.penup()
    t.backward(160)
    t.left(90)
    t.forward(20)

ada = turtle.Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-160, 100)
ada.pendown()

jeff = turtle.Turtle()
jeff.color('green')
jeff.shape('turtle')

jeff.penup()
jeff.goto(-160, 80)
jeff.pendown()

jeremy = turtle.Turtle()
jeremy.color('purple')
jeremy.shape('turtle')

jeremy.penup()
jeremy.goto(-160, 60)
jeremy.pendown()

for turn in range(100):
    ada.forward(randint(1, 5))
    jeff.forward(randint(1, 5))
    jeremy.forward(randint(1, 5))
wn.exitonclick()