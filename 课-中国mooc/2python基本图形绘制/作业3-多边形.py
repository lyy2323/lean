import turtle as t
t.setup(500,400,0,0)
t.penup()
t.seth(240)
t.fd(150)
t.pendown()
t.pensize(2)
t.pencolor('black')
t.seth(0)
for i in range(9):
    t.fd(100)
    t.left(80)
t.done()