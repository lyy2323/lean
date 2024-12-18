import turtle as t
t.setup(500,400,0,0)
t.seth(180)
t.pensize(1)
t.pencolor("blue")
for i in range(4):
    t.fd(100)
    t.left(90)
    t.circle(100,45)
    t.left(90)
    t.fd(100)
    t.right(135)
t.done()