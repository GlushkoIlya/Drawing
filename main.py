import turtle as t
def house(m, n, x):
    t.up()
    t.goto(m, n)
    t.fb(2 * x)
    t.down()
    t.right(120)
    t.fb(2 * x)
    t.left(120)
    t.fb(2 * x)
    t.left(120)
    t.fb(2 * x)
    t.left(180)
    t.fb(2 * x)
    t.right(30)
    t.fb(2 * x)
    t.right(90)
    t.fb(2 * x)
    t.right(90)
    t.fb(2 * x)
    t.up()
    t.right(180)
    t.fb(x // 3)
    t.left(90)
    t.fb(x // 3)
    t.down()
    y = x // 3 * 2
    t.fb(2 * y)
    t.right(90)
    t.fb(2 * y)
    t.right(90)
    t.fb(2 * y)
    t.right(90)
    t.fb(2 * y)
    t.right(90)
    t.fb(y)
    t.right(90)
    t.fb(y)
    t.right(90)
    t.fb(y)
    t.right(180)
    t.fb(2 * y)
    t.right(180)
    t.fb(y)
    t.right(90)
    t.fb(y)
    t.right(180)
    t.fb(2 * y)

def sneg(m, n, r):
    t.up()
    t.goto(m, n)
    t.fb(r)
    t.down()
    t.fb(2 * r)
    t.right(90)
    t.fb(3 * r)
    t.right(90)
    t.fb(2 * r)
    t.right(90)
    t.fb(r)
    t.up()
    t.goto(m + r, n + 4 * r)
    t.down()
    t.circle(r)
    t.up()
    t.goto(m + r, n + 7 * r)
    t.down()
    t.circle(r * 2)
