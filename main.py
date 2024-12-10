import turtle


screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor('aquamarine')

t = turtle.Turtle()
t.hideturtle()
t2 = turtle.Turtle()


t2.hideturtle()
t2.fillcolor('red')
t2.penup()
t2.goto(0, 100)


turtle.addshape("nova.gif")
t2.shape("nova.gif")


t2.goto(100,150)
a = t2.stamp()
t2.goto(100,-150)
b = t2.stamp()

t.penup()
t.goto(0, 50)
t.pendown()
t.write("Snapping Sniper", font=("Arial", 24, "bold"), align="center")
t.penup()
t.goto(0, -50)
t.pendown()
t.write("Villanova", font=("Arial", 24, "bold"), align="center")

enter = input("Press Enter to Start")
t.clear()
t2.clear()

screen.bgcolor("Blue")
t.pendown()
t.write("Favorite foods", font=("Arial", 24, "bold"), align="center")


turtle.addshape("waffle.gif")
t2.shape("waffle.gif")
t2.goto(100,150)
c = t2.stamp()
t2.goto(100,150)

turtle.addshape("bacon.gif")
t2.shape("bacon.gif")
t2.goto(-100,150)
d = t2.stamp()
t2.goto(-100,150)

turtle.addshape("taco.gif")
t2.shape("taco.gif")
t2.goto(-250,150)
e = t2.stamp()
t2.goto(-250,150)

t.penup()
enter = input("Press Enter to Start")
t.clear()
t2.clear()

screen.bgcolor("Green")
t.pendown()
t.write("Hobbies", font=("Arial", 24, "bold"), align="center")

turtle.addshape("madden.gif")
t2.shape("madden.gif")
t2.goto(100,150)
f = t2.stamp()
t2.goto(100,150)

turtle.addshape("basketball.gif")
t2.shape("basketball.gif")
t2.goto(-100,150)
g = t2.stamp()
t2.goto(-100,150)

turtle.addshape("cards.gif")
t2.shape("cards.gif")
t2.goto(270,150)
h = t2.stamp()
t2.goto(270,150)

turtle.addshape("coach.gif")
t2.shape("coach.gif")
t2.goto(60,-260)
i = t2.stamp()
t2.goto(60,-260)


t.penup()
enter = input("Press Enter to Start")
t.clear()
t2.clear()

screen.bgcolor("purple")
t.pendown()
t.write("Favorite movie", font=("Arial", 24, "bold"), align="center")

turtle.addshape("hustle.gif")
t2.shape("hustle.gif")
t2.goto(100,150)
j = t2.stamp()
t2.goto(100,150)


t.penup()
enter = input("Press Enter to Start")
t.clear()
t2.clear()

screen.bgcolor("red")
t.pendown()
t.write("Favorite sport", font=("Arial", 24, "bold"), align="center")


turtle.addshape("basketball (1).gif")
t2.shape("basketball (1).gif")
t2.goto(100,150)
k = t2.stamp()
t2.goto(100,150)



turtle.done()