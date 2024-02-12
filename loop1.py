from turtle import *

speed('fastest')
pencolor('blue')
pensize(4)

for i in range(9):
    fd(120)
    lt(40)
    write(f'n={i}')

hideturtle()
mainloop()
