import turtle as t


t.colormode(255)


def house(m, n, x):
    # TODO: Ilya
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
    t.left(90)


def rect(a1, a2, cl='black'):
    x1 = a1[0]
    y1 = a1[1]
    x2 = a2[0]
    y2 = a2[1]
    t.color(cl)
    t.up()
    t.goto(x1, y1)
    t.down()
    t.begin_fill()
    t.goto(x1, y2)
    t.goto(x2, y2)
    t.goto(x2, y1)
    t.goto(x1, y1)
    t.end_fill()
    t.color('black')


def triangle(a1, a2, a3, cl='black'):
    x1 = a1[0]
    y1 = a1[1]
    x2 = a2[0]
    y2 = a2[1]
    x3 = a3[0]
    y3 = a3[1]
    t.color(cl)
    t.up()
    t.goto(x1, y1)
    t.down()
    t.begin_fill()
    t.goto(x2, y2)
    t.goto(x3, y3)
    t.goto(x1, y1)
    t.end_fill()
    t.color('black')


def qr(a1, a2, a3, a4, cl='black'):
    x1 = a1[0]
    y1 = a1[1]
    x2 = a2[0]
    y2 = a2[1]
    x3 = a3[0]
    y3 = a3[1]
    x4 = a4[0]
    y4 = a4[1]
    t.color(cl)
    t.up()
    t.goto(x1, y1)
    t.down()
    t.begin_fill()
    t.goto(x2, y2)
    t.goto(x3, y3)
    t.goto(x4, y4)
    t.goto(x1, y1)
    t.end_fill()
    t.color('black')


def rocket(x, y, m):
    t1 = [x, y]
    t2 = [x - m, y - m]
    t3 = [x + m, y - m]
    t4 = [x - m, y - 3 * m]
    t5 = [x + m, y - 3 * m]
    t6 = [x - m // 2, y - 4 * m]
    t7 = [x + m // 2, y - 4 * m]
    t8 = [x - 1.5 * m, y - 4 * m]
    t9 = [x + 1.5 * m, y - 4 * m]
    t10 = [x - 1.5 * m, y - 5 * m]
    t11 = [x + 1.5 * m, y - 5 * m]
    t12 = [x - m // 2, y - 4.5 * m]
    t13 = [x + m // 2, y - 4.5 * m]
    t14 = [x + m // 2, y - m]
    t15 = [x - m // 2, y - 3 * m]
    t16 = [x + m // 2, y - 3 * m]
    triangle(t1, t2, t14, 'red')
    triangle(t1, t3, t14, 'blue')
    triangle(t2, t3, t4, 'yellow')
    triangle(t3, t5, t4, 'orange')
    triangle(t15, t16, t7, 'green')
    triangle(t15, t6, t7, 'blue')
    triangle(t15, t8, t10, 'pink')
    triangle(t15, t10, t12, 'purple')
    triangle(t16, t9, t7, 'grey')
    qr(t7, t9, t11, t13)


def tree(x, y, m):
    t1 = [x, y]
    t2 = [x - m, y - m]
    t3 = [x, y - m]
    t4 = [x + m // 2, y - m]
    t5 = [x + m, y - m]
    t6 = [x - 1.5 * m, y - 2.5 * m]
    t7 = [x - m // 2, y - 2.5 * m]
    t8 = [x, y - 2.5 * m]
    t9 = [x + 1.5 * m, y - 2.5 * m]
    t10 = [x - m, y - 3.5 * m]
    t11 = [x + m // 2, y - 3.5 * m]
    t12 = [x + m, y - 3.5 * m]
    t13 = [x - 2 * m, y - 4.5 * m]
    t14 = [x - m // 2, y - 4.5 * m]
    t15 = [x, y - 4.5 * m]
    t16 = [x + m // 2, y - 4.5 * m]
    t17 = [x + m, y - 4.5 * m]
    t18 = [x + 2 * m, y - 4.5 * m]
    t19 = [x - m // 2, y - 6 * m]
    t20 = [x + m // 2, y - 6 * m]
    cl = [(100, 255, 50), (50, 200, 100), (10, 150, 50), (30, 60, 10),
          (70, 230, 70), (100, 255, 200), (10, 50, 10), (150, 75, 0)]
    triangle(t1, t2, t4, cl[0])
    triangle(t1, t4, t5, cl[1])
    triangle(t3, t6, t7, cl[2])
    triangle(t3, t7, t9, cl[3])
    triangle(t8, t13, t17, cl[4])
    triangle(t8, t18, t17, cl[5])
    qr(t13, t10, t12, t15, cl[6])
    rect(t14, t20, cl[7])


def el(m, n, x):
    t.up()
    t.goto(m, n)
    t.fd(x / 2)
    t.down()
    for i in range(3):
        t.right(120)
        t.fd(x)
        t.left(120)
        t.fd(x)
        t.left(120)
        t.fd(x)
        t.left(120)
        t.fd(x)
        t.left(120)
        t.fd(x / 2)
        x += x / 2
    t.fd(x / 16)
    t.right(90)
    t.fd(x / 4)
    t.right(90)
    t.fd(x / 8)
    t.right(90)
    t.fd(x / 4)
    t.right(90)


def dog(m, n, x):
    # TODO: Platon
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
    # TODO: Platon
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


def liss(m, n, x):
    # TODO:Nadia
    t.up()
    t.goto(m, n)
    t.down()
    t.right(90)
    t.begin_fill()
    t.color("#FF6633")  # левое ухо
    t.goto(m, n - 4 * x)
    t.goto(m + 2 * x, n - 2 * x)
    t.goto(m, n)
    t.end_fill()
    t.up()
    t.goto(m + 4 * x, n)
    t.down()
    t.right(90)
    t.begin_fill()
    t.color("#FF6633")  # правое ухо
    t.goto(m, n - 4 * x)
    t.goto(m + 2 * x, n - 2 * x)
    t.goto(m+4*x, n-4*x)
    t.end_fill()
    t.begin_fill()
    t.color("#FF9900")  # голова
    t.goto(m + 2 * x, n - 2 * x)
    t.goto(m + 2 * x, n - 2 * x)
    t.goto(m, n - 4 * x)
    t.goto(m + 2 * x, n - 6 * x)
    t.goto(m + 4 * x, n - 4 * x)
    t.end_fill()
    t.goto(m + 3 * x, n - 5 * x)
    t.begin_fill()
    t.color("#FF3300")  # туловище_1
    t.goto(m - x, n - 9 * x)
    t.goto(m + 7 * x, n - 9 * x)
    t.end_fill()
    t.goto(m + 4 * x, n - 6 * x)
    t.begin_fill()
    t.color("#FF6666")  # туловище_2
    t.goto(m + 7 * x, n - 9 * x)
    t.goto(m + 10 * x, n - 6 * x)
    t.end_fill()
    t.begin_fill()
    t.color("#FF3366")  # туловище_3
    t.goto(m + 6 * x, n - 10 * x)
    t.goto(m + 15 * x, n - 10 * x)
    t.goto(m + 10 * x, n - 6 * x)
    t.end_fill()


def zaicc(m, n, x):
    # TODO: Nadia
    t.up()
    t.goto(m, n)
    t.down()
    t.right(90)
    t.begin_fill()
    t.color("#01796f")
    t.goto(m + 2 * x, n)
    t.goto(m + 4 * x, n - 3 * x)
    t.goto(m + 2 * x, n - 3 * x)
    t.goto(m, n)
    t.end_fill()
    t.goto(m + 4 * x, n - 3 * x)
    t.begin_fill()
    t.color("#022027")
    t.goto(m + 6 * x, n - 3 * x)
    t.goto(m + 6 * x, n - 5 * x)
    t.goto(m + 4 * x, n - 5 * x)
    t.goto(m + 4 * x, n - 3 * x)
    t.end_fill()
    t.goto(m + 4 * x, n - 5 * x)
    t.begin_fill()
    t.color("#01796f")
    t.up()
    t.goto(m + 6 * x, n - 3 * x)
    t.down()
    t.goto(m + 8 * x, n)
    t.goto(m + 10 * x, n)
    t.goto(m + 8 * x, n - 3 * x)
    t.goto(m + 6 * x, n - 3 * x)
    t.end_fill()
    t.up()
    t.goto(m + 2 * x, n - 5 * x)
    t.down()
    t.begin_fill()
    t.color("#1fffda")
    t.goto(m + 8 * x, n - 5 * x)
    t.goto(m + 5 * x, n - 8 * x)
    t.end_fill()
    t.begin_fill()
    t.color("#78dbe2")
    t.goto(m + 3 * x, n - 6 * x)
    t.goto(m + 3 * x, n - 10 * x)
    t.goto(m + 5 * x, n - 8 * x)
    t.end_fill()
    t.goto(m + 7 * x, n - 6 * x)
    t.begin_fill()
    t.color("#99ffff")
    t.goto(m + 7 * x, n - 10 * x)
    t.goto(m + 3 * x, n - 10 * x)
    t.goto(m + 7 * x, n - 6 * x)
    t.end_fill()


def car(x, y, m):
    t1 = [x, y]
    t2 = [x + 0.5 * m, y - m]
    t3 = [x - 2.5 * m, y]
    t4 = [x - 3 * m, y - m]
    t5 = [x - 2 * m, y - m]
    t6 = [x + m, y - m]
    t7 = [x - 3.5 * m, y - m]
    t8 = [x - 4.5 * m, y - 2 * m]
    t9 = [x - 2.5 * m, y - 2 * m]
    t10 = [x + 2 * m, y - 2 * m]
    qr(t2, t5, t3, t1, 'blue')
    triangle(t3, t4, t5, 'dark blue')
    triangle(t7, t8, t9, 'dark red')

    qr(t7, t9, t10, t6, 'red')

t.speed(100)
car(-600, 0, 70)

zaicc(450, 400, 40)
liss(450, -100, 30)
house(-800, 350, 50)
el(-725, 100, 50)
machine(-550, 250, 30)
dog(-650, 100, 30)
tree(0, 0, 50)
rocket(100, 500, 50)


# machine(100, 100, 100)

t.mainloop()
