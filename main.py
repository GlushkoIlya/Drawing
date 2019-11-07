import turtle as t
def house(m, n, x):
    t.up()
    t.goto(m, n)
    t.fd(2 * x)
    t.down()
    t.right(120)
    t.fd(2 * x)
    t.left(120)
    t.fd(2 * x)
    t.left(120)
    t.fd(2 * x)
    t.left(180)
    t.fd(2 * x)
    t.right(30)
    t.fd(2 * x)
    t.right(90)
    t.fd(2 * x)
    t.right(90)
    t.fd(2 * x)
    t.up()
    t.right(180)
    t.fd(x // 3)
    t.left(90)
    t.fd(x // 3)
    t.down()
    y = x // 3 * 2
    t.fd(2 * y)
    t.right(90)
    t.fd(2 * y)
    t.right(90)
    t.fd(2 * y)
    t.right(90)
    t.fd(2 * y)
    t.right(90)
    t.fd(y)
    t.right(90)
    t.fd(y)
    t.right(90)
    t.fd(y)
    t.right(180)
    t.fd(2 * y)
    t.right(180)
    t.fd(y)
    t.right(90)
    t.fd(y)
    t.right(180)
    t.fd(2 * y)

def sneg(m, n, r):
    t.up()
    t.goto(m, n)
    t.fd(r)
    t.down()
    t.fd(2 * r)
    t.right(90)
    t.fd(3 * r)
    t.right(90)
    t.fd(2 * r)
    t.right(90)
    t.fd(r)
    t.up()
    t.goto(m + r, n + 4 * r)
    t.down()
    t.circle(r)
    t.up()
    t.goto(m + r, n + 7 * r)
    t.down()
    t.circle(r * 2)

def dog(m, n, x):
    t.up()
    t.goto(m, n)
    t.fd(4 * x)
    t.down()
    t.right(90)
    t.fd(2 * x)
    t.right(90)
    t.fd(2 * x)
    t.left(90)
    t.fd(2 * x)
    t.left(90)
    t.fd(x)
    t.left(90)
    t.fd(x)
    t.right(90)
    t.fd(x)
    t.right(90)
    t.fd(x)
    t.left(90)
    t.fd(x)
    t.left(90)
    t.fd(x * 2)
    t.right(90)
    t.fd(x)
    t.left(90)
    t.fd(x)
    t.left(90)
    t.fd(x)
    t.right(90)
    t.fd(x)
    t.left(90)
    t.fd(x)

def machine(m, n, x):
    t.up()
    t.goto(m, n)
    t.fd(4 * x)
    t.down()
    t.right(90)
    t.fd(x)
    t.right(90)
    t.fd(x)
    t.left(90)
    t.fd(x)
    t.right(90)
    t.fd(x)
    t.right(90)
    t.fd(x)
    t.left(90)
    t.fd(x)
    t.left(90)
    t.fd(x)
    t.right(90)
    t.fd(x)
    t.right(90)
    t.fd(x)
    t.left(90)
    t.fd(x)
    t.right(90)
    t.fd(x)
    t.right(90)
    t.fd(x)
    t.left(90)
    t.fd(x)
    t.right(90)
    t.fd(3 * x)
    t.right(90)
    t.fd(x)
    t.left(90)
    t.fd(x)
machine(100, 100, 100)