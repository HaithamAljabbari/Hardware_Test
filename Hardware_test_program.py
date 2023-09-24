import turtle as t
from itertools import cycle

färg = cycle(["blue", "black"])

färg2 = cycle(["blue", "black"])

rang = range(360)
rang2 = range(360)

t.bgcolor("black")

t.hideturtle()

while True:
    for i in rang:
        t.speed("fastest")
        t.goto(0, -20)
        t.pensize(0.1)
        t.setheading(90 + i)
        t.pencolor(next(färg))
        t.forward(100)
   
    while True:
        for i in rang2:
            t.speed("fastest")
            t.goto(100, -20)
            t.pensize(0.1)
            t.setheading(90 + i)
            t.pencolor(next(färg2))
            t.circle(100)
        while True:
            for i in rang2:
                t.speed("fastest")
                t.goto(100, -20)
                t.pensize(0.1)
                t.setheading(90 + i + i)
                t.pencolor(next(färg2))
                t.circle(1000)
                if rang2 == 360:
                    break

                
    
