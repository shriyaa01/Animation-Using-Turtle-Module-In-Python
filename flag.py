import turtle
t=turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor("black")
#flag band 
def band(sp,colour):
    t.up()
    t.goto(0,sp)
    t.down()
    t.color(colour)
    t.begin_fill()
    t.fillcolor(colour)
    t.goto(300,sp)
    t.setheading(270)
    t.forward(70)
    t.setheading(180)
    t.goto(0,sp-70)
    t.goto(0,sp)
    t.end_fill()

t.pensize(4)
#flag stand
t.up()  
t.goto(0,-300)
t.down()
t.color("brown")
t.goto(0,300)
#flag outer design
band(300,"orange")
band(230,"white")
t.up()
t.goto(150,230)
t.down()
t.color("blue")
t.circle(35)
t.up()
t.goto(150,195)
t.down()
for j in range(24):
    t.forward(35)
    t.up()
    t.backward(35)
    t.down()
    t.left(15)
    
band(155,"green")

