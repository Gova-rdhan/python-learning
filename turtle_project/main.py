import example_turtle as t
import random
tu = t.Turtle()
sc = t.Screen()
def square():
    for _ in  range(4):
        tu.pencolor("blue")
        tu.forward(100)
        tu.left(90)


def dashed_line():
    for _ in range(10):
        tu.setx(-320)
        tu.sety(-270)
        tu.forward(10)
        tu.color("red")
        tu.forward(10)
        tu.color("black")
def triangle():
    for _ in range(3):
        tu.pencolor("red")
        tu.forward(100)
        tu.left(120)

def pentagon():
    for _ in range(5):
        tu.pencolor("blue")
        tu.forward(100)
        tu.left(72)
def hexaagon():
    for _ in range(6):
        tu.pencolor("yellow")
        tu.forward(100)
        tu.left(60)
def hpentagon():
    for _ in range(7):
        tu.pencolor("blue")
        tu.forward(100)
        tu.left(51.43)
def octagon():
    for _ in range(8):
        tu.pencolor("pink")
        tu.forward(100)
        tu.left(45)
def nonagon():
    for _ in range(9):
        tu.pencolor("red")
        tu.forward(100)
        tu.left(40)
def decagon():
    for _ in range(10):
        tu.pencolor("red")
        tu.forward(100)
        tu.left(36)
def shapes():
    color = ['red','blue','green','yellow','black','red','blue','green','yellow','black']
    for i in range(3,11):
        angle = 360 / i
        for j in range(i):
            tu.speed(40)
            tu.pencolor("red")
            tu.forward(100)
            tu.left(angle)
def random_walk():
    dir = [90,180,270,0]
    t.colormode(255)
    def random_colr():
        r  = random.randint(0,255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        tup = (r,g,b)
        return tup
    tu.speed(0)
    tu.pensize(10)
    for _ in range(1,200):
        tu.pencolor(random_colr())
        tu.forward(10)
        tu.setheading(random.choice(dir))
        tu.forward(10)
def spirograph():
    t.colormode(255)

    def random_colr():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        tup = (r, g, b)
        return tup
    tu.speed('fastest')
    for i in range(0,29):
        tu.circle(50)
        tu.color(random_colr())
        tu.left(i)

t.colormode(255)
def random_colr():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tup = (r, g, b)
    return tup

t.setheading(225)
t.forward(300)
t.setheading(0)
no_of_dots = 100
for i in range(1,no_of_dots):
    tu.dot(20,random_colr())
    tu.forward(50)

sc.exitonclick()