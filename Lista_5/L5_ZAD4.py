from turtle import *

def koch_curve(level, angle, step):
    if level < 0:
        raise ValueError("The value of level of the recursion must be positive number")
    elif level == 0:
        forward(step)
        return
    else:
        step /= 3
        koch_curve(level - 1, angle, step)
        left(angle)
        koch_curve(level - 1, angle, step)
        right(180-angle)
        koch_curve(level - 1, angle, step)
        left(angle)
        koch_curve(level - 1, angle, step)

def draw_koch(level = 3, size = 300):
    if not (isinstance(level, int) and isinstance(size, int)):
        raise TypeError("Wrong data given")
    if size <= 0:
        raise ValueError("Size is too small")
    title("Koch Curve")
    bgcolor("#FFEBCD")
    speed(1000)
    penup()
    goto(-size/2, size/2)
    pendown()
    koch_curve(level, 60, size)
    mainloop()

def draw_snowflake_koch(level = 3, size = 300):
    if not (isinstance(level, int) and isinstance(size, int)):
        raise TypeError("Wrong data given")
    if size <= 0:
        raise ValueError("Size is too small")
    title("Snowflake Koch")
    bgcolor("#FFEBCD")
    speed(1000)
    penup()
    goto(-size/2, size/2)
    pendown()
    for i in range(3):
        koch_curve(level, 60, size)
        right(120)
    mainloop()

if __name__ == "__main__":
    #draw_koch(4)
    draw_snowflake_koch(4)