import turtle

turtle.Screen().bgcolor("")
board = turtle.Turtle()

# drawing a hexagon
for i in range (6):
    board.forward(90)
    board.left(90)
    board.forward(90)
    board.left(90)
    board.forward(90)
    board.left(90)