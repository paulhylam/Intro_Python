import turtle

def draw_square(some_turtle):
    for j in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_trangle(some_turtle):
    for i in range(1,3):
        some_turtle.forward(100)
        some_turtle.left(120)
        some_turtle.forward(100)
        some_turtle.left(120)
    some_turtle.forward(100)

def draw_circle():

    window = turtle.Screen()
    window.bgcolor("red")

    # define the class for turtle - which is used to create different turtle-based objects (instances)
    brad = turtle.Turtle()

    # now the attributes for 'brad' is changed
    brad.color("yellow")
    brad.shape("turtle")
    brad.speed(50)

#loop the square to create a circle

    for i in range(1,72):
        draw_square(brad)
        brad.right(5)

    # Another object based on the class turtle, called angie

    # angie = turtle.Turtle()
    # angie.color("blue")
    # angie.speed(2)
    # angie.circle(100)
    # angie.shape("arrow")

    window.exitonclick()

def draw_flower():

    window = turtle.Screen()
    window.bgcolor("red")

    top = turtle.Turtle()
    top.shape("arrow")
    top.speed(40)

    stem = turtle.Turtle()

    for i in range(1,36):
        draw_trangle(top)
        top.right(10)

    stem.right(90)
    stem.forward(225)

    window.exitonclick()

# draw_circle()
draw_flower()

