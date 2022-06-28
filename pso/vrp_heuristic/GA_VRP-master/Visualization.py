import turtle
from turtle import Turtle, Screen
import random
import numpy


# Solution = [[40, 11, 50, 10, 51, 17, 12, 39, 6, 13], [49, 7, 24, 8, 27, 9, 23, 2, 28, 47, 48], [31, 35, 22, 30, 21, 36, 37, 4, 32, 29], [46, 34, 16, 45, 38, 18, 5, 43, 20, 42, 41, 14], [44, 25, 15, 26, 19, 3, 33]],
X=0
Y=0
turtle_1 = Turtle()
turtle_2 = Turtle()
turtle_1.shape("circle")
turtle_2.shape("circle")
turtle_2.color("Black")
turtle_2.hideturtle()
turtle_2.penup()

turtle.colormode(255)


colours = ["Red", "Blue", "Purple", "Orange","Yellow", "Green", "Pink", "Black", "Violet","Cyan","Grey","green yellow","dark cyan","medium violet red","Grey","orange red","light sky blue"]

graph={}

def show_path(solution,no_of_trucks,fileName,depot):
    with open(fileName) as f:
        for _ in range(7):
            next(f)
        for line in f:
            (city, x, y) = line.split()
            graph[city]=[float(x),float(y)]

    print("////")
    print(depot.name)
    X= depot.x
    Y= depot.y
    X = X * -5
    Y = Y * 5

    print(graph)
    print(solution)
    turtle_1.pensize(2)
    turtle_1.penup()
    turtle_1.goto(X, Y)
    turtle_1.pendown()





    for j in range(0,no_of_trucks):
        turtle_1.color(colours[j])
        turtle_1.goto(X, Y)
        turtle_1.pendown()
        print("Length="+str(len(solution[j])))
        for i in range(0,len(solution[j])):
            k=solution[j][i]
            print(str(k) + "... ")
            print(i)
            if str(k) != '9999':
                print(str(k) + "+++")

                x, y = graph[str(k)]
                turtle_1.goto(x*-5, y*5)
                turtle_2.goto(x*-5, y*5)
                turtle_2.pendown()
                turtle_2.pensize(1)
                turtle_2.write(f" {i} ({x}, {y})", align="center", font=("poppins", 5, "normal"))
                turtle_2.penup()
        turtle_1.goto(X, Y)
        turtle_1.penup()





