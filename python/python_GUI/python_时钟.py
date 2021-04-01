from turtle import *
from datetime import *
# 移动到指定位置


def skip(step):
    penup()
    forward(step)
    pendown()
# 画指针


def drawpointer(name, length):
    reset()
    skip(-length*0.1)
    begin_poly()
    forward(length*1.1)
    end_poly()
    handForm = get_poly()
    register_shape(name, handForm)
# 初始化


def init():
    global hrpointer, minpointer, secpointer, weektext
    # 设置turtle Logo模式，朝北
    mode("logo")
    drawpointer("hrpointer", 90)
    drawpointer("minpointer", 130)
    drawpointer("secpointer", 140)
    hrpointer = Turtle()
    hrpointer.shape("hrpointer")
    minpointer = Turtle()
    minpointer.shape("minpointer")
    secpointer = Turtle()
    secpointer.shape("secpointer")
    secpointer.pencolor("red")
    for pointer in hrpointer, minpointer, secpointer:
        pointer.shapesize(3, 1, 1)
        pointer.speed(0)
    # 文字输出
    weektext = Turtle()
    weektext.hideturtle()
    weektext.penup()
# 设置表盘形状


def setupClock(radius):
    reset()
#  clockPanel = Turtle()
    pensize(7)
    pencolor("blue")
    for i in range(60):
        skip(radius)
        if i % 5 == 0:
            forward(20)
            skip(-radius-20)
        else:
            dot(5)
            skip(-radius)
        right(6)

# 星期文本


def Week(t):
    week = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    return week[t.weekday()]
# 日期文本


def Date(t):
    y = t.year
    m = t.month
    d = t.day
    return "%s %d %d" % (y, m, d)
# 绘制表针动态显示


def tick():
    t = datetime.today()
    second = t.second + t.microsecond*0.0000001
    minute = t.minute + second/60.0
    hour = t.hour + minute/60.0
    secpointer.setheading(6*second)
    minpointer.setheading(6*minute)
    hrpointer.setheading(30*hour)
    tracer(False)
    weektext.forward(65)
    weektext.write(Week(t), align="center", font=("Courier", 14, "bold"))
    weektext.back(130)
    weektext.write(Date(t), align="center", font=("Courier", 14, "bold"))
    weektext.home()
    tracer(True)
    # 间隔100ms调用一次
    ontimer(tick, 100)


def main():
    tracer(False)
    init()
    setupClock(160)
    tracer(True)
    tick()
    mainloop()


if __name__ == '__main__':
    main()
