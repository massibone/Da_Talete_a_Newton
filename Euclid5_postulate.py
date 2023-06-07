
'''
Quinto postulato Euclide. Se una retta taglia altre due rette e forma dalla stessa parte angoli interni la cui somma 
è minore dei due angoli retti allora le due rette si incontreranno dalla parte di tali angoli
'''

import turtle

# disegna le tre rette
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
turtle.goto(200, 0)
turtle.penup()
turtle.goto(-100, -200)
turtle.pendown()
turtle.goto(-100, 200)
turtle.penup()
turtle.goto(100, -200)
turtle.pendown()
turtle.goto(100, 200)

# calcola gli angoli interni
angle1 = turtle.towards(-100, -200) - turtle.heading()
angle2 = turtle.towards(100, -200) - turtle.towards(-100, -200)
angle3 = turtle.towards(100, 200) - turtle.towards(100, -200)

# visualizza gli angoli interni
turtle.penup()
turtle.goto(-120, -120)
turtle.pendown()
turtle.write(str(angle1) + "°")
turtle.left(angle1)
turtle.forward(50)
turtle.backward(50)
turtle.right(angle1)
turtle.penup()
turtle.goto(-100, 20)
turtle.pendown()
turtle.write(str(angle2) + "°")
turtle.back(50)
turtle.left(90)
turtle.forward(50)
turtle.backward(50)
turtle.right(90)
turtle.penup()
turtle.goto(70, -120)
turtle.pendown()
turtle.write(str(angle3) + "°")
turtle.back(50)
turtle.right(90)
turtle.forward(50)
turtle.backward(50)
turtle.left(90)

# controlla se le due rette si incontrano
if angle2 + angle3 < 90 or angle1 + angle3 < 90:
    turtle.penup()
    turtle.goto(0, 0)
    turtle.write("Le due rette si incontrano dalla parte degli angoli interni.")
else:
    turtle.penup()
    turtle.goto(0, 0)
    turtle.write("Le due rette non si incontrano dalla parte degli angoli interni.")

turtle.done()