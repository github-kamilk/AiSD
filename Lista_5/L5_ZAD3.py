from turtle import *

def hilbert_curve(level, angle, step):
    if level < 0:
        raise ValueError("The value of level of the recursion must be positive number")
    elif level == 0:
        return
    else:
        right(angle)
        hilbert_curve(level - 1, -angle, step)
        forward(step)
        left(angle)
        hilbert_curve(level - 1, angle, step)
        forward(step)
        hilbert_curve(level - 1, angle, step)
        left(angle)
        forward(step)
        hilbert_curve(level - 1, -angle, step)
        right(angle)

def draw_hilbert_curve(level = 3, size = 300):
    if not (isinstance(level, int) and isinstance(size, int)):
        raise TypeError("Wrong data given")
    if level == 0:
        raise ZeroDivisionError("Wrong data given")
    if size <= 0:
        raise ValueError("Size is too small")
    title("Hilbert Curve")
    bgcolor("#FFEBCD")
    speed(10)
    penup()
    goto(-size/2, size/2)
    pendown()
    hilbert_curve(level, 90, size/(2 ** level - 1))
    mainloop()

if __name__ == '__main__':
    draw_hilbert_curve(4)