# შექმენით ფუნქცია რომელიც მიიღებს x და y კორდინატს, შემდეგ კი გადაცემული კორდინატების ადგილას დახაზავს კვადრატს, დავალების შესასრულებლად გამოიყენეთ მოდული: from turtle import *
from turtle import*
def greet(x, y):
    penup()
    goto(x, y)
    pendown()

    side = 0
    while side < 4:
        forward(100)
        right(90)
        side += 1


greet(50, 100)
