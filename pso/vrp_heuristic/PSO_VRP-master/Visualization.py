import turtle
from turtle import Turtle, Screen
import random
import RegExService
import numpy

# initializing deport coordinates
X=0
Y=0

# initializing turtle characters
turtle_1 = Turtle()
turtle_2 = Turtle()
turtle_1.shape("circle")
turtle_2.shape("circle")
turtle_2.color("Black")
turtle_2.hideturtle()
turtle_2.penup()

turtle.colormode(255)

# path colors
colours = ["Red", "Blue", "Purple", "Orange","Yellow", "Green", "Pink", "Black", "Violet","Cyan","Grey","green yellow","dark cyan","medium violet red","Grey","orange red","light sky blue"]

# function to visualize the best path
def show_path(solution,no_of_trucks,fileName):
    capacityLimit, graph, demand, optimalValue,trucks = RegExService.getData(fileName)
    print(solution)

    #solution=([[1], [42, 18, 3], [22, 5, 7, 14, 38, 9], [35, 46, 27, 47, 28, 43], [45, 21, 16, 44, 10, 17], [12, 24, 33, 6, 36, 19, 8], [40, 41, 30, 29, 20, 13], [32, 39, 2, 4], [48, 34, 11, 31, 49, 26], [15, 37, 23, 25]],1394.888)
    X,Y=graph[1]
    X=X*-5
    Y=Y*-5
    vertices = list(graph.keys())
    vertices.remove(1)
    turtle_1.pensize(2)
    turtle_1.penup()
    turtle_1.goto(X,Y)
    turtle_1.pendown()

    # loop to draw each truck path
    for j in range(0,trucks):
        turtle_1.color(colours[j])
        turtle_1.goto(X,Y)
        turtle_1.pendown()
        for i in solution[j]:
            x, y = graph[i]
            turtle_1.goto(x*-5, y*-5)
            turtle_2.goto(x*-5, y*-5)
            turtle_2.pendown()
            turtle_2.pensize(1)
            turtle_2.write(f" {i} ({x}, {y})", align="center", font=("poppins", 5, "normal"))
            turtle_2.penup()
        turtle_1.goto(X, Y)
        turtle_1.penup()




