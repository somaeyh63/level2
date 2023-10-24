# from turtle import *
# for steps in range(right(33))
#         while True:
#             forward(200)
#             left(170)
#             if abs(pos()) < 1:
#                 break

from  turtle import  Turtle
from  random import  random

t = Turtle()
for i in range(100):
    steps = int(random()*100)
    angle = int(random()*360)
    t.right(angle)
    t.fd(steps)
t.screen.mainloop()