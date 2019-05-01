""" #1.
for sentence in range(100):
    print("We like Python's turtles!")

>>>>#2. ????

>>>>#3.
months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
for oneyear in list(months):
    print("One of the months of the year is", oneyear)

>>>>#4.
numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for rawnum in numbers:
    print(rawnum)

for sqnum in numbers:
    print(str(sqnum) + " squared is " + str(sqnum * sqnum))

>>>>#5.
import turtle
wn = turtle.Screen()
wn.setup(600,400)
wn.bgcolor("gray")

shelly = turtle.Turtle()
shelly.color("pink")

sheldon = turtle.Turtle()
sheldon.color("cyan")
sheldon.forward(-150)

for triangle in range(3):
    shelly.forward(50)
    shelly.right(120)

for square in range(4):
    shelly.left(90)
    shelly.forward(30)

for hexagon in range(6):
    sheldon.right(60)
    sheldon.forward(40)

for octagon in range(8):
    sheldon.left(45)
    sheldon.forward(25)

wn.exitonclick()

>>>>#6.
import turtle
wn = turtle.Screen()
polly = turtle.Turtle()

amount = int(input("How many sides will the shape have?"))
length = int(input("How long will the sides be?"))
lineColor = input("What color will the lines be?")
fillColor = input("What color will the inside of the shape be?")

polly.color(lineColor)
polly.begin_fill()

for polygon in range(amount):
    polly.left(360/amount)
    polly.forward(length)

polly.color(fillColor)
polly.end_fill()

wn.exitonclick()

>>>>#7. N/A
import turtle
wn = turtle.Screen()
wn.screensize(1200,400)
polly = turtle.Turtle()

polly.up()
polly.forward(-400)
polly.down()

angles = [160, 43, 270, 97, 43, 200, 940, 17, 86]

for wander in list(angles):
    polly.left(wander)
    polly.forward(100)
    polly.right(wander)
    polly.forward(100)

wn.exitonclick()

>>>>#8. N/A
>>>>#9.
import turtle
wn = turtle.Screen()
shelly = turtle.Turtle()

for star in range(5):
    shelly.right(144)
    shelly.forward(100)

wn.exitonclick()

>>>>#10.
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
sheldon = turtle.Turtle()
sheldon.shape("turtle")
sheldon.color("blue")
sheldon.up()

for hour in range(12):
    sheldon.forward(80)
    sheldon.down()
    sheldon.forward(10)
    sheldon.up()
    sheldon.forward(20)
    sheldon.stamp()
    sheldon.forward(-110)
    sheldon.right(30)

wn.exitonclick()

>>>>#11.
import turtle
wn = turtle.Screen()
wn.bgcolor("lightyellow")
sheldon = turtle.Turtle()
sheldon.shape("circle")
sheldon.color("blue")
sheldon.up()
sheldon.goto(-300,-50)
sheldon.down()

for wave in range(4):
    sheldon.left(35)
    sheldon.forward(40)
    sheldon.left(15)
    sheldon.forward(50)
    sheldon.right(15)
    sheldon.forward(40)
    sheldon.right(30)
    sheldon.forward(30)
    sheldon.right(150)
    sheldon.forward(30)
    sheldon.left(20)
    sheldon.forward(30)
    sheldon.left(30)
    sheldon.forward(20)
    sheldon.left(60)
    sheldon.forward(10)
    sheldon.left(10)
    sheldon.forward(50)
    sheldon.left(25)

sheldon.up()
sheldon.color("gray")
sheldon.goto(-300,300)
sheldon.down()

for gulls in range(2):
    sheldon.forward(15)
    sheldon.right(20)
    sheldon.forward(15)
    sheldon.left(40)
    sheldon.forward(15)
    sheldon.right(20)
    sheldon.forward(15)
    sheldon.up()
    sheldon.goto(-200,200)
    sheldon.down()

sheldon.up()
sheldon.color("orange")
sheldon.goto(250,300)
sheldon.stamp()

wn.exitonclick()

>>>>#12.
import turtle
wn = turtle.Screen()
shelly = turtle.Turtle()
print(type(shelly))

>>>>#13.
import turtle
wn = turtle.Screen()
sprite = turtle.Turtle()
sprite.shape("circle")
sprite.color("black")

legs = int(input("How many legs does this sprite have?"))

sprite.stamp()
for hatch in range(legs):
    sprite.forward(50)
    sprite.forward(-50)
    sprite.right(360/legs)

wn.exitonclick()
"""
