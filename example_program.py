import stressless as sl
import turtle


def tuple_to_color(tup):
    col = '#%02x%02x%02x' % tup
    return col

ball = sl.StressLess()
ball.adjust_threshold(-10)
i = 0
while True:
    i = (i + 0.01) % 2

    freq = ball.getFrequency(100)
    freq = min(2, freq)

    wn = turtle.Screen()
    wn.bgcolor(tuple_to_color((int(freq * 127), int(127 * (2-freq)), 127)))
    wn.title("Testing in progress")
    if freq < 0.05:
        wn.title("Squeezing too slow")


