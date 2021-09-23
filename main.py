import turtle

def rectangle(width, height):
  for i in range(2):
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)

def octagon (len):
  for i in range(8):
    turtle.forward(len)
    turtle.left(45)

def stop(len):
  octagon(len)
  turtle.forward(3/8 * len)
  rectangle(1/5 * len, 2 * len)


def main():
  turtle.speed(1)
  turtle.color("red")
  stop(50)
  turtle.color("red")
  turtle.penup()
  turtle.forward(210)
  turtle.pendown()
  turtle.color("green")
  stop(80)


main()
turtle.screen().exitonclick()