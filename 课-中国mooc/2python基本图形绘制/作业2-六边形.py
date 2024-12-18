import turtle as t
t.setup(500,400,0,0)
t.penup()
t.seth(240)
t.fd(150)
t.seth(0)
t.pendown()
t.pencolor("black")
for i in range(6):
    t.fd(100)
    t.left(60)
t.done()